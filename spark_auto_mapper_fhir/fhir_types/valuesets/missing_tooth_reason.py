from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMissingToothReasonCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-missing-tooth-reason.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirMissingToothReasonCode']
        ) -> None:
            self.f: Callable[..., 'FhirMissingToothReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirMissingToothReasonCode']
        ) -> 'FhirMissingToothReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirMissingToothReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirMissingToothReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/missingtoothreason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.534"
