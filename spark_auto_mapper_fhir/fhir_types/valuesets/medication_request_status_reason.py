from typing import Callable, Type, Any

from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirMedicationRequestStatusReasonCode(AutoMapperDataTypeLiteral):
    """
    https://hl7.org/FHIR/valueset-medicationrequest-status-reason.html
    """

    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirMedicationRequestStatusReasonCode':
        return cls(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'FhirMedicationRequestStatusReasonCode']) -> None:
            self.f: Callable[..., 'FhirMedicationRequestStatusReasonCode'] = f

        def __get__(self, obj: Any,
                    owner: Type['FhirMedicationRequestStatusReasonCode']) -> 'FhirMedicationRequestStatusReasonCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirMedicationRequestStatusReasonCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirMedicationRequestStatusReasonCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/medicationrequest-status-reason"