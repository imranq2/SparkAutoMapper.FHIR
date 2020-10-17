from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase
from spark_auto_mapper.type_definitions.defined_types import AutoMapperTextInputType

from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
# noinspection SpellCheckingInspection
from spark_auto_mapper_fhir.fhir_types.organization import FhirOrganization
from spark_auto_mapper_fhir.fhir_types.period import FhirPeriod

from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FhirIdentifier(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    from spark_auto_mapper_fhir.fhir_types.reference import FhirReference

    @classmethod
    def map(cls,
            use: Optional[FhirCode] = None,
            type_: Optional[FhirCodeableConcept] = None,
            system: Optional[FhirUri] = None,
            value: Optional[AutoMapperTextInputType] = None,
            period: Optional[FhirPeriod] = None,
            assigner: Optional['FhirReference[FhirOrganization]'] = None
            ) -> 'FhirIdentifier':
        """
        Identifier Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Identifier
        An identifier intended for computation


        :param use: usual | official | temp | secondary | old (If known) (https://hl7.org/FHIR/valueset-identifier-use.html)
        :param type_: Description of identifier https://hl7.org/FHIR/valueset-identifier-type.html
        :param system: 	The namespace for the identifier value
        :param value: The value that is unique
        :param period: Time period when id is/was valid for use
        :param assigner: Organization that issued id (may be just text)
        """
        return FhirIdentifier(
            use=use,
            type_=type_,
            system=system,
            value=value,
            period=period,
            assigner=assigner
        )
