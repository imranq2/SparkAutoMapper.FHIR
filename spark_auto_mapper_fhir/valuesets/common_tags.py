from typing import Callable, Type, Any

from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


# noinspection PyMethodParameters
# noinspection PyPep8Naming
class CommonTagsCode(FhirValueSetBase):
    """
    https://www.hl7.org/fhir/valueset-common-tags.html
    """
    def __init__(self, value: AutoMapperTextInputType):
        super().__init__(value=value)

    # noinspection PyPep8Naming,SpellCheckingInspection
    class classproperty(object):
        def __init__(self, f: Callable[..., 'CommonTagsCode']) -> None:
            self.f: Callable[..., 'CommonTagsCode'] = f

        def __get__(
            self, obj: Any, owner: Type['CommonTagsCode']
        ) -> 'CommonTagsCode':
            return self.f(owner)

    @classproperty
    def NameOfYourFirstValue(cls) -> 'CommonTagsCode':
        """
        Comment
        """
        # noinspection PyCallingNonCallable
        return CommonTagsCode("A")

    @genericclassproperty
    def codeset(cls) -> FhirUri:
        """
        http://terminology.hl7.org/CodeSystem/common-tags
        """
        return "http://terminology.hl7.org/CodeSystem/common-tags"

    @genericclassproperty
    def oid(cls) -> FhirUri:
        """
        2.16.840.1.113883.4.642.3.79
        """
        return "2.16.840.1.113883.4.642.3.79"
