from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirEncounter(FhirResourceBase):
    def __init__(self) -> None:
        """
        Encounter Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Encounter
        """
        super().__init__()
