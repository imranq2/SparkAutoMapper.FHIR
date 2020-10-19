from typing import Dict

from pyspark.sql import SparkSession, Column, DataFrame
# noinspection PyUnresolvedReferences
from pyspark.sql.functions import col
from pyspark.sql.functions import lit, struct, array, coalesce, to_date
from spark_auto_mapper.automappers.automapper import AutoMapper
from spark_auto_mapper.helpers.automapper_helpers import AutoMapperHelpers as A

from spark_auto_mapper_fhir.fhir_types.human_name import FhirHumanName
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.patient import FhirPatient
from spark_auto_mapper_fhir.fhir_types.valuesets.administrative_gender import AdministrativeGenderCode
from spark_auto_mapper_fhir.fhir_types.valuesets.name_use import NameUseCode


def test_auto_mapper_fhir_patient_resource(
    spark_session: SparkSession
) -> None:
    # Arrange
    spark_session.createDataFrame(
        [
            (1, 'Qureshi', 'Imran', '1970-01-01', "female"),
            (2, 'Vidal', 'Michael', '1970-02-02', "male"),
        ],
        ['member_id', 'last_name', 'first_name', 'date_of_birth', "my_gender"]
    ).createOrReplaceTempView("patients")

    source_df: DataFrame = spark_session.table("patients")

    df = source_df.select("member_id")
    df.createOrReplaceTempView("members")

    # Act
    mapper = AutoMapper(
        view="members", source_view="patients", keys=["member_id"]
    ).complex(
        FhirPatient(
            id_=A.column("a.member_id"),
            birthDate=A.date(A.column("date_of_birth")),
            name=FhirList(
                FhirHumanName(
                    use=NameUseCode("usual"), family=A.column("last_name")
                )
            ),
            gender=AdministrativeGenderCode(A.column("my_gender"))
        )
    )

    assert isinstance(mapper, AutoMapper)
    sql_expressions: Dict[str, Column] = mapper.get_column_specs(
        source_df=source_df
    )
    for column_name, sql_expression in sql_expressions.items():
        print(f"{column_name}: {sql_expression}")

    result_df: DataFrame = mapper.transform(df=df)

    # Assert
    assert len(sql_expressions) == 4
    assert str(sql_expressions["id"]) == str(col("a.member_id").alias("id"))
    assert str(sql_expressions["birthDate"]) == str(
        coalesce(
            to_date(col("date_of_birth"), 'yyyy-MM-dd'),
            to_date(col("date_of_birth"), 'yyyyMMdd'),
            to_date(col("date_of_birth"), 'MM/dd/yy')
        ).alias("birthDate")
    )
    assert str(sql_expressions["name"]) == str(
        array(
            struct(
                lit("usual").alias("use"),
                col("last_name").alias("family"),
            )
        ).alias("name")
    )
    assert str(sql_expressions["gender"]
               ) == str(col("my_gender").alias("gender"))

    result_df.printSchema()
    result_df.show()

    assert result_df.where("member_id == 1").selectExpr("name[0].use").collect(
    )[0][0] == "usual"
    assert result_df.where("member_id == 1").selectExpr(
        "name[0].family"
    ).collect()[0][0] == "Qureshi"

    assert result_df.where("member_id == 2").selectExpr("name[0].use").collect(
    )[0][0] == "usual"
    assert result_df.where("member_id == 2").selectExpr(
        "name[0].family"
    ).collect()[0][0] == "Vidal"
