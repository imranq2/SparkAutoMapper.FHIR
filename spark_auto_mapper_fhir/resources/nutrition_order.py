from typing import Optional, Union
from pyspark.sql.types import StructType, DataType
from spark_fhir_schemas.r4.resources.nutritionorder import NutritionOrderSchema

from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta


class NutritionOrder(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        extension: Optional[FhirList[Extension]] = None
    ) -> None:
        """
        NutritionOrder Resource in FHIR
        https://www.hl7.org/fhir/nutritionorder.html
        TODO: Fill this

        :param id_: id of resource
        """
        super().__init__(
            resourceType="NutritionOrder",
            id_=id_,
            meta=meta,
            extension=extension
        )

    def get_schema(
        self, include_extension: bool
    ) -> Optional[Union[StructType, DataType]]:
        return NutritionOrderSchema.get_schema(
            include_extension=include_extension
        )
