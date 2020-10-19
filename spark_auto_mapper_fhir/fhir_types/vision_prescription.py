from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase


class FhirVisionPrescription(FhirResourceBase):
    def __init__(self) -> None:
        """
        VisionPrescription Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#VisionPrescription
        """
        super().__init__()
