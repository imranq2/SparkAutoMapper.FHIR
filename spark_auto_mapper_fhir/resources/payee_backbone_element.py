from typing import Optional, Union

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.valuesets.claim_payee_type import ClaimPayeeTypeCode
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.patient import Patient
from spark_auto_mapper_fhir.resources.practitioner import Practitioner
from spark_auto_mapper_fhir.resources.practitioner_role import PractitionerRole
from spark_auto_mapper_fhir.resources.reference import Reference
from spark_auto_mapper_fhir.resources.related_person import RelatedPerson


class PayeeBackboneElement(FhirResourceBase):
    def __init__(
        self,
        type_: Optional[CodeableConcept[ClaimPayeeTypeCode]] = None,
        party: Optional[Reference[Union[Practitioner, PractitionerRole,
                                        Organization, Patient,
                                        RelatedPerson]]] = None
    ):
        """
        PayeeBackboneElement Resource in FHIR
        http://hl7.org/fhir/claim-definitions.html#Claim.payee
        Recipient of benefits payable

        :param type_: Category of recipient https://hl7.org/FHIR/valueset-payeetype.html
        :param party: Recipient reference
        """
        super().__init__(type_=type_, party=party)
