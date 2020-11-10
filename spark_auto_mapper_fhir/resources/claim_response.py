from typing import Optional

from spark_auto_mapper_fhir.extensions.extension import Extension
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class ClaimResponse(FhirResourceBase):
    def __init__(
        self,
        id_: Optional[FhirId] = None,
        extension: Optional[FhirList[Extension]] = None
    ) -> None:
        """
        ClaimResponse Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ClaimResponse


        :param id_: id of resource
        """
        super().__init__(
            resourceType="ClaimResponse", id_=id_, extension=extension
        )
