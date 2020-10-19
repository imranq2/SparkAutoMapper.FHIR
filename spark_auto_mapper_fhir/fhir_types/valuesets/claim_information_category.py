from typing import Callable, Type, Any

from spark_auto_mapper_fhir.fhir_types.valuesets.FhirValueSetBase import FhirValueSetBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class FhirClaimInformationCategoryCode(FhirValueSetBase):
    """
    https://hl7.org/FHIR/valueset-claim-informationcategory.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(
            self, f: Callable[..., 'FhirClaimInformationCategoryCode']
        ) -> None:
            self.f: Callable[..., 'FhirClaimInformationCategoryCode'] = f

        def __get__(
            self, obj: Any, owner: Type['FhirClaimInformationCategoryCode']
        ) -> 'FhirClaimInformationCategoryCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'FhirClaimInformationCategoryCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return FhirClaimInformationCategoryCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "http://terminology.hl7.org/CodeSystem/claiminformationcategory"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        return "2.16.840.1.113883.4.642.3.582"
