from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirObservation(FhirResourceBase):
    def __init__(self) -> None:
        """
        Observation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Observation
        """
        super().__init__()
