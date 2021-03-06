from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class DataAbsentReasonCode(FhirValueSetBase):
    """
    Used to specify why the normally expected content of the data element is missing.
    https://www.hl7.org/fhir/valueset-data-absent-reason.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'DataAbsentReasonCode']) -> None:
            self.f: Callable[..., 'DataAbsentReasonCode'] = f

        def __get__(
            self, obj: Any, owner: Type['DataAbsentReasonCode']
        ) -> 'DataAbsentReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'DataAbsentReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return DataAbsentReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/data-absent-reason
        """
        return "http://terminology.hl7.org/CodeSystem/data-absent-reason"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.5
        """
        return "2.16.840.1.113883.4.642.3.5"
