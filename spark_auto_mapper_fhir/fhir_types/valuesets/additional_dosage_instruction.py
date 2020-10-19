from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirAdditionalDosageInstructionCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-additional-instruction-codes.html
    """
    @classmethod
    def map(
        cls, value: AutoMapperNativeSimpleType
    ) -> 'FhirAdditionalDosageInstructionCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
                self,
                f: Callable[...,
                            'FhirAdditionalDosageInstructionCode']) -> None:
            self.f: Callable[..., 'FhirAdditionalDosageInstructionCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirAdditionalDosageInstructionCode']
        ) -> 'FhirAdditionalDosageInstructionCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirAdditionalDosageInstructionCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirAdditionalDosageInstructionCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://snomed.info/sct "
