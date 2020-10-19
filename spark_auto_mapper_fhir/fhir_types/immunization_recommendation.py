from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirImmunizationRecommendation(FhirResourceBase):
    def __init__(self) -> None:
        """
        ImmunizationRecommendation Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ImmunizationRecommendation
        """
        super().__init__()
