from typing import Optional

from spark_auto_mapper_fhir.complex_types.expression import Expression
from spark_auto_mapper_fhir.extensions.extension_base import ExtensionBase
from spark_auto_mapper_fhir.fhir_types.id import FhirId
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.backbone_elements.fhir_backbone_element_base import (
    FhirBackboneElementBase,
)
from spark_auto_mapper_fhir.valuesets.action_condition_kind import (
    ActionConditionKindCode,
)


class ConditionBackboneElement(FhirBackboneElementBase):
    def __init__(
        self,
        kind: ActionConditionKindCode,
        id_: Optional[FhirId] = None,
        expression: Optional[Expression] = None,
        extension: Optional[FhirList[ExtensionBase]] = None,
    ) -> None:
        """
        ConditionBackboneElement Backbone Element in FHIR
        https://www.hl7.org/fhir/backboneelement.html
        """
        super().__init__(kind=kind, id_=id_,expression=expression, extension=extension)
