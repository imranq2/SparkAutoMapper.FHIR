from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class QuantityComparatorCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-quantity-comparator.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'QuantityComparatorCode']) -> None:
            self.f: Callable[..., 'QuantityComparatorCode'] = f

        def __get__(
            self, obj: Any, owner: Type['QuantityComparatorCode']
        ) -> 'QuantityComparatorCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'QuantityComparatorCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return QuantityComparatorCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/quantity-comparator"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.59"
