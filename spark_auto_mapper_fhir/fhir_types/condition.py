from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirCondition(FhirResourceBase):
    @classmethod
    def map(cls, ) -> 'FhirCondition':
        """
        Condition Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Condition
        """
        return FhirCondition()
