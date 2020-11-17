from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Procedure(FhirResourceBase):
    def __init__(
        self,
        id_: FhirId,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        Procedure Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Procedure


        :param id_: id of resource
        """
        super().__init__(
            resourceType="Procedure", id_=id_, extension=extension
        )
