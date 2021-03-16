from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CareTeamCategoryCode(FhirValueSetBase):
    """
    IMPORTANT: To comply with the Spark mapping mechanism, please make sure you add all existing FHIR
                properties not just the ones you need
    https://www.hl7.org/fhir/valueset-care-team-category.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'CareTeamCategoryCode']) -> None:
            self.f: Callable[..., 'CareTeamCategoryCode'] = f

        def __get__(
            self, obj: Any, owner: Type['CareTeamCategoryCode']
        ) -> 'CareTeamCategoryCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'CareTeamCategoryCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CareTeamCategoryCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://loinc.org
        """
        return "http://loinc.org"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.155
        """
        return "2.16.840.1.113883.4.642.3.155"
