from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.duration import Duration
from spark_auto_mapper_fhir.fhir_types.quantity import Quantity


class Fill(FhirResourceBase):
    def __init__(
        self,
        quantity: Optional[Quantity] = None,
        duration: Optional[Duration] = None
    ):
        """
        Fill Resource in FHIR
        https://hl7.org/FHIR/medicationrequest.html


        :param quantity: fill quantity
        :param duration: fill duration
        """
        super().__init__(quantity=quantity, duration=duration)
