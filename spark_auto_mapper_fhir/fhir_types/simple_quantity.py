from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


class FhirSimpleQuantity(FhirResourceBase):
    def __init__(
        self,
        value: Optional[FhirDecimal] = None,
        unit: Optional[FhirString] = None,
        system: Optional[FhirUri] = None,
        code: Optional[FhirValueSetBase] = None
    ):
        """
        SimpleQuantity Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#SimpleQuantity
        The comparator is not used on a SimpleQuantity

        :param value: Numerical value (with implicit precision)
        :param unit: Unit representation
        :param system: System that defines coded unit form
        :param code: Coded form of the unit
        """
        super().__init__(value=value, unit=unit, system=system, code=code)
