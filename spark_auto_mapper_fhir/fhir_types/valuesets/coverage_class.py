from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirCoverageClassCode(AutoMapperDataTypeLiteral):
    """
    https://hl7.org/FHIR/valueset-coverage-class.html
    """

    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirCoverageClassCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirCoverageClassCode']) -> None:
            self.f: Callable[..., 'FhirCoverageClassCode'] = f

        def __get__(self, obj: Any,
                    owner: Type['FhirCoverageClassCode']
                    ) -> 'FhirCoverageClassCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirCoverageClassCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirCoverageClassCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/coverage-class"