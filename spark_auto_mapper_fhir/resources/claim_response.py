from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase


class ClaimResponse(FhirResourceBase):
    def __init__(self) -> None:
        """
        ClaimResponse Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ClaimResponse
        """
        super().__init__()
