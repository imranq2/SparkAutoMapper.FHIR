from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirServiceUSCLSCode(AutoMapperDataTypeLiteral):
    """
    https://hl7.org/FHIR/valueset-service-uscls.html
    """

    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirServiceUSCLSCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirServiceUSCLSCode']) -> None:
            self.f: Callable[..., 'FhirServiceUSCLSCode'] = f

        def __get__(self, obj: Any,
                    owner: Type['FhirServiceUSCLSCode']
                    ) -> 'FhirServiceUSCLSCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirServiceUSCLSCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirServiceUSCLSCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/ex-USCLS"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.542"