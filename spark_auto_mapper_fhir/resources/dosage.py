from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.additional_dosage_instruction import AdditionalDosageInstructionCode
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class Dosage(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        sequence: Optional[FhirPositiveInt] = None,
        text: Optional[FhirString] = None,
        additionalInstruction: Optional[
            CodeableConcept[AdditionalDosageInstructionCode]] = None,
        patientInstruction: Optional[FhirString] = None,
    ):
        """
        Dosage Resource in FHIR
        https://hl7.org/FHIR/dosage.html#Dosage
        How the medication is/was taken or should be taken

        :param sequence: The order of the dosage instructions
        :param text: Free text dosage instructions e.g. SIG
        :param additionalInstruction: Supplemental instruction or warnings to the patient -
                                        e.g. "with meals", "may cause drowsiness".
                                        https://hl7.org/FHIR/valueset-additional-instruction-codes.html
        :param patientInstruction: Patient or consumer oriented instructions
        """
        super().__init__(
            sequence=sequence,
            text=text,
            additionalInstruction=additionalInstruction,
            patientInstruction=patientInstruction
        )