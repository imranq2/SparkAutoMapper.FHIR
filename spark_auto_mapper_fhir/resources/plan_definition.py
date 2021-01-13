from typing import Optional
from pyspark.sql.types import StructType

from spark_fhir_schemas.r4.resources.plandefinition import PlanDefinitionSchema

from spark_auto_mapper_fhir.backbone_elements.action_backbone_element import ActionBackboneElement
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.complex_types.meta import Meta
from spark_auto_mapper_fhir.valuesets.publication_status import PublicationStatusCode


class PlanDefinition(FhirResourceBase):
    def __init__(
        self,
        status: PublicationStatusCode,
        id_: Optional[FhirId] = None,
        meta: Optional[Meta] = None,
        action: Optional[FhirList[ActionBackboneElement]] = None,
        extension: Optional[FhirList[Extension]] = None
    ) -> None:
        """
        PlanDefinition Resource in FHIR
        https://www.hl7.org/fhir/plandefinition.html


        :param id_: id of resource
        """
        super().__init__(
            resourceType="PlanDefinition",
            id_=id_,
            meta=meta,
            extension=extension,
            status=status,
            action=action
        )

    def get_schema(self, include_extension: bool) -> Optional[StructType]:
        return PlanDefinitionSchema.get_schema(
            include_extension=include_extension
        )
