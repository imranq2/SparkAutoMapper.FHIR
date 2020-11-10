from typing import Optional

from spark_auto_mapper_fhir.classproperty import genericclassproperty
from spark_auto_mapper_fhir.extensions.custom.insurance_plan_item import InsurancePlanItemExtension
from spark_auto_mapper_fhir.extensions.fhir_extension_base import FhirExtensionBase
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class InsurancePlanExtension(FhirExtensionBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        url: Optional[FhirUri] = None,
        extension: Optional[FhirList[InsurancePlanItemExtension]] = None
    ) -> None:
        """
        InsurancePlanExtension Extension type in FHIR
        """
        super().__init__(
            url=url or InsurancePlanExtension.codeset, extension=extension
        )

    # noinspection PyMethodParameters
    @genericclassproperty
    def codeset(cls) -> FhirUri:
        return "https://raw.githubusercontent.com/imranq2/SparkAutoMapper.FHIR/main/StructureDefinition/insurance_plan"