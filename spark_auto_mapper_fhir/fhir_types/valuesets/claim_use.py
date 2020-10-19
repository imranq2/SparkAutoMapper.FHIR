from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirClaimUseCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-use.html
    """
    @classmethod
    def map(cls, value: AutoMapperTextInputType) -> 'FhirClaimUseCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirClaimUseCode']) -> None:
            self.f: Callable[..., 'FhirClaimUseCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirClaimUseCode']
        ) -> 'FhirClaimUseCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirClaimUseCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirClaimUseCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/claim-use"
