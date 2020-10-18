from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMedicationRequestIntent(AutoMapperDataTypeLiteral):
    """
    https://hl7.org/FHIR/valueset-medicationrequest-intent.html
    """

    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirMedicationRequestIntent':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirMedicationRequestIntent']) -> None:
            self.f: Callable[..., 'FhirMedicationRequestIntent'] = f

        def __get__(self, obj: Any, owner: Type['FhirMedicationRequestIntent']) -> 'FhirMedicationRequestIntent':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirMedicationRequestIntent':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirMedicationRequestIntent("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://hl7.org/fhir/CodeSystem/medicationrequest-intent"