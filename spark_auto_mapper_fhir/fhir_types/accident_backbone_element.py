from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.address import FhirAddress
from spark_auto_mapper_fhir.fhir_types.codeableConcept import FhirCodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.accident_incident import AccidentIncidentCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.location import FhirLocation
from spark_auto_mapper_fhir.fhir_types.reference import FhirReference


class FhirAccidentBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        date: Optional[FhirDate] = None,
        type_: Optional[FhirCodeableConcept[AccidentIncidentCode]] = None,
        locationAddress: Optional[FhirAddress] = None,
        locationReference: Optional[FhirReference[FhirLocation]] = None
    ) -> None:
        """
        AccidentBackboneElement Resource in FHIR
        https://hl7.org/FHIR/explanationofbenefit-definitions.html#ExplanationOfBenefit.accident
        Details of the event

        :param date: When the incident occurred
        :param type_: The nature of the accident.  https://hl7.org/FHIR/v3/ActIncidentCode/vs.html
        :param locationAddress: Where the event occurred
        :param locationReference: Where the event occurred
        """
        super().__init__(
            date=date,
            type_=type_,
            locationAddress=locationAddress,
            locationReference=locationReference
        )
