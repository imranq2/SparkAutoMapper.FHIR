from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.boolean import FhirBoolean
from spark_auto_mapper_fhir.fhir_types.coverage import Coverage
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class InsuranceBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        focal: FhirBoolean,
        coverage: Reference[Coverage],
        preAuthRef: Optional[FhirList[FhirString]] = None
    ):
        """
        InsuranceBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#InsuranceBackboneElement
        Patient insurance information


        :param focal: Coverage to be used for adjudication
        :param coverage: Insurance information
        :param preAuthRef: 	Prior authorization reference number
        """
        super().__init__(focal=focal, coverage=coverage, preAuthRef=preAuthRef)
