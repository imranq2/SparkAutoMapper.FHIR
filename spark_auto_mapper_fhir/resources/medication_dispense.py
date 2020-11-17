from typing import Optional

from spark_auto_mapper_fhir.complex_types.identifier import Identifier
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.resources.fhir_resource_base import FhirResourceBase
from spark_auto_mapper_fhir.resources.procedure import Procedure
from spark_auto_mapper_fhir.complex_types.reference import Reference


class MedicationDispense(FhirResourceBase):
    # noinspection PyPep8Naming
    def __init__(
        self,
        id_: FhirId,
        identifier: Optional[FhirList[Identifier]] = None,
        partOf: Optional[FhirList[Reference[Procedure]]] = None,
        extension: Optional[FhirList[ExtensionBase]] = None
    ) -> None:
        """
        MedicationDispense Resource in FHIR
        https://www.hl7.org/fhir/medicationdispense.html
        Dispensing a medication to a named patient
        + Rule: whenHandedOver cannot be before whenPrepared


        :param id_: id of resource
        :param identifier: External identifier
        :param partOf: Event that dispense is part of

        """
        super().__init__(
            resourceType="MedicationDispense",
            id_=id_,
            identifier=identifier,
            partOf=partOf,
            extension=extension
        )
