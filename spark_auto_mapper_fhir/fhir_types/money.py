from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.decimal import FhirDecimal
from spark_auto_mapper_fhir.fhir_types.valuesets.currency import FhirCurrencyCode


class FhirMoney(FhirResourceBase):
    def __init__(
        self,
        value: Optional[FhirDecimal] = None,
        currency: Optional[FhirCurrencyCode] = None
    ):
        """
        Money Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Money
        An amount of economic utility in some recognized currency

        :param value: Numerical value (with implicit precision)
        :param currency: ISO 4217 Currency Code. https://hl7.org/FHIR/valueset-currencies.html
        """
        super().__init__(value=value, currency=currency)
