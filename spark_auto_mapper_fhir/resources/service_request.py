from typing import Optional

from pyspark.sql.types import StructType
from spark_fhir_schemas.r4.resources.servicerequest import ServiceRequestSchema

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class ServiceRequest(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        ServiceRequest Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ServiceRequest


        :param id_: id of resource
        """
        super().__init__(
            resourceType="ServiceRequest", id_=id_, extension=extension
        )

    def get_schema(self) -> Optional[StructType]:
        return ServiceRequestSchema.get_schema()
