from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.coverage_class import CoverageClassCode
from spark_auto_mapper_fhir.fhir_types.string import FhirString


class FhirCoverageClassificationBackboneElement(FhirResourceBase):
    def __init__(
        self,
        type_: FhirCodeableConcept[CoverageClassCode],
        value: FhirString,
        name: Optional[FhirString] = None
    ):
        """
        CoverageClassificationBackboneElement Resource in FHIR
        https://hl7.org/FHIR/coverage-definitions.html#Coverage.class
        Additional coverage classifications

        :param type_: Type of class such as 'group' or 'plan'. https://hl7.org/FHIR/valueset-coverage-class.html
        :param value: Value associated with the type
        :param name: Human readable description of the type and value
        """
        super().__init__(type_=type_, value=value, name=name)
