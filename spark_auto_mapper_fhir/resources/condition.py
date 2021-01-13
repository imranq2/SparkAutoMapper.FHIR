from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.condition import ConditionSchema

from spark_auto_mapper_fhir.complex_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.valuesets.condition import ConditionCode


class Condition(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        meta: Optional[Meta] = None,
        identifier: Optional[FhirList[Identifier]] = None,
        code: Optional[CodeableConcept[ConditionCode]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition


        :param id_: id of resource
        """
        super().__init__(
            resourceType="Condition",
            id_=id_,
            meta=meta,
            extension=extension,
            identifier=identifier,
            code=code,
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return ConditionSchema.get_schema(include_extension=include_extension)
