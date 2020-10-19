from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirIcd10ProcedureCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-icd-10-procedures.html
    """
    @classmethod
    def map(cls, value: AutoMapperTextInputType) -> 'FhirIcd10ProcedureCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirIcd10ProcedureCode']) -> None:
            self.f: Callable[..., 'FhirIcd10ProcedureCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirIcd10ProcedureCode']
        ) -> 'FhirIcd10ProcedureCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirIcd10ProcedureCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirIcd10ProcedureCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/sid/ex-icd-10-procedures"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.574"
