from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirBenefitTermCode(AutoMapperDataTypeLiteral):
    """
    https://hl7.org/FHIR/valueset-benefit-term.html
    """

    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirBenefitTermCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirBenefitTermCode']) -> None:
            self.f: Callable[..., 'FhirBenefitTermCode'] = f

        def __get__(self, obj: Any,
                    owner: Type['FhirBenefitTermCode']
                    ) -> 'FhirBenefitTermCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirBenefitTermCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirBenefitTermCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/benefit-term"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.612"
