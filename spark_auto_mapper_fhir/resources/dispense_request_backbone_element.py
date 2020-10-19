from typing import Optional

from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.resources.duration import Duration
from spark_auto_mapper_fhir.resources.fill import Fill
from spark_auto_mapper_fhir.resources.organization import Organization
from spark_auto_mapper_fhir.resources.period import Period
from spark_auto_mapper_fhir.resources.reference import Reference
from spark_auto_mapper_fhir.resources.simple_quantity import SimpleQuantity
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt


class DispenseRequestBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        initialFill: Optional[Fill] = None,
        dispenseInterval: Optional[Duration] = None,
        validityPeriod: Optional[Period] = None,
        numberOfRepeatsAllowed: Optional[FhirUnsignedInt] = None,
        quantity: Optional[SimpleQuantity] = None,
        expectedSupplyDuration: Optional[Duration] = None,
        performer: Optional[Reference[Organization]] = None
    ):
        """
        DispenseRequestBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#DispenseRequestBackboneElement
        Medication supply authorization

        :param initialFill: First fill details
        :param dispenseInterval: Minimum period of time between dispenses
        :param validityPeriod: Time period supply is authorized for
        :param numberOfRepeatsAllowed: Number of refills authorized
        :param quantity: Amount of medication to supply per dispense
        :param expectedSupplyDuration: Number of days supply per dispense
        :param performer: Intended dispenser
        """
        super().__init__(
            initialFill=initialFill,
            dispenseInterval=dispenseInterval,
            validityPeriod=validityPeriod,
            numberOfRepeatsAllowed=numberOfRepeatsAllowed,
            quantity=quantity,
            expectedSupplyDuration=expectedSupplyDuration,
            performer=performer
        )