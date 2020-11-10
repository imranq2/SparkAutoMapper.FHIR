from typing import Optional

from spark_auto_mapper_fhir.extensions.extension_base import FhirExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class Device(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[FhirExtensionBase]] = None
    ) -> None:
        """
        Device Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Device


        :param id_: id of resource
        """
        super().__init__(resourceType="Device", id_=id_, extension=extension)
