from typing import Optional

from spark_auto_mapper_fhir.fhir_types.fhir_resource_base import FhirResourceBase

from spark_auto_mapper_fhir.fhir_types.codeableConcept import CodeableConcept
from spark_auto_mapper_fhir.fhir_types.valuesets.ex_procedure_type import ExProcedureTypeCode
from spark_auto_mapper_fhir.fhir_types.valuesets.icd10_procedure import Icd10ProcedureCode
from spark_auto_mapper_fhir.fhir_types.date import FhirDate
from spark_auto_mapper_fhir.fhir_types.list import FhirList
from spark_auto_mapper_fhir.fhir_types.positive_int import FhirPositiveInt
from spark_auto_mapper_fhir.fhir_types.procedure import Procedure
from spark_auto_mapper_fhir.fhir_types.reference import Reference


class ProcedureBackboneElement(FhirResourceBase):
    # noinspection PyPep8Naming,SpellCheckingInspection
    def __init__(
        self,
        sequence: FhirPositiveInt,
        procedureCodeableConcept: CodeableConcept[Icd10ProcedureCode],
        type_: Optional[FhirList[CodeableConcept[ExProcedureTypeCode]]] = None,
        date: Optional[FhirDate] = None,
        procedureReference: Optional[Reference[Procedure]] = None
    ):
        """
        ProcedureBackboneElement Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#ProcedureBackboneElement
        Clinical procedures performed

        :param sequence: Procedure instance identifier
        :param procedureCodeableConcept: Specific clinical procedure.
                                        https://hl7.org/FHIR/valueset-icd-10-procedures.html
        :param type_: Category of Procedure. https://hl7.org/FHIR/valueset-ex-procedure-type.html
        :param date: When the procedure was performed
        :param procedureReference:
        """
        super().__init__(
            sequence=sequence,
            procedureCodeableConcept=procedureCodeableConcept,
            type_=type_,
            date=date,
            procedureReference=procedureReference
        )
