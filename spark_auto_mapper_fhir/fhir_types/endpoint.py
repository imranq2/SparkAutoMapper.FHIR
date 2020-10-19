from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirEndpoint(FhirResourceBase):
    def __init__(self) -> None:
        """
        Endpoint Resource in FHIR
        http://hl7.org/fhir/endpoint.html
        """
        super().__init__()
