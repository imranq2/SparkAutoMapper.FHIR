from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class ClaimUseCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-use.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'ClaimUseCode']) -> None:
            self.f: Callable[..., 'ClaimUseCode'] = f

        def __get__(
            self, obj: Any, owner: Type['ClaimUseCode']
        ) -> 'ClaimUseCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'ClaimUseCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return ClaimUseCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/claim-use"
