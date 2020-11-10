from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.fhir_extension_base import FhirExtensionBase
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri
from spark_auto_mapper_fhir.valuesets.FhirValueSetBase import FhirValueSetBase


class ${Class}(FhirExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        valueCode: Optional[FhirValueSetBase] = None
    ) -> None:
        """
        ${Class} Extension type in FHIR
        """
        super().__init__(url=url or ${Class}.codeset, valueCode=valueCode)

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "${codeset}"