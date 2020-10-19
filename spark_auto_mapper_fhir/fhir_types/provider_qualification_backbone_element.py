from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.identifier import Identifier
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.organization import Organization
from spark_auto_mapper_fhir.fhir_types.period import Period
from spark_auto_mapper_fhir.fhir_types.reference import Reference
from spark_auto_mapper_fhir.fhir_types.valuesets.provider_qualification import ProviderQualificationCode


class ProviderQualificationBackboneElement(FhirResourceBase):
    def __init__(
        self,
        code: CodeableConcept[ProviderQualificationCode],
        identifier: Optional[FhirList[Identifier]] = None,
        period: Optional[Period] = None,
        issuer: Optional[Reference[Organization]] = None
    ):
        """
        ProviderQualificationBackboneElement Resource in FHIR
        http://hl7.org/fhir/practitioner-definitions.html#Practitioner.qualification
        Certification, licenses, or training pertaining to the provision of care

        :param code: Coded representation of the qualification. http://hl7.org/fhir/v2/0360/2.7/index.html
        :param identifier: An identifier for this qualification for the practitioner
        :param period: Period during which the qualification is valid
        :param issuer: Organization that regulates and issues the qualification
        """
        super().__init__(
            code=code, identifier=identifier, period=period, issuer=issuer
        )
