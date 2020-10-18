from typing import Optional

from spark_auto_mapper.data_types.complex.complex_base import AutoMapperDataTypeComplexBase

from spark_auto_mapper_fhir.fhir_types.base64Binary import FhirBase64Binary
from spark_auto_mapper_fhir.fhir_types.code import FhirCode
from spark_auto_mapper_fhir.fhir_types.date_time import FhirDateTime
from spark_auto_mapper_fhir.fhir_types.string import FhirString
from spark_auto_mapper_fhir.fhir_types.unsigned_int import FhirUnsignedInt
from spark_auto_mapper_fhir.fhir_types.uri import FhirUri


class FhirAttachment(AutoMapperDataTypeComplexBase):
    # noinspection PyPep8Naming
    @classmethod
    def map(cls,
            contentType: Optional[FhirCode] = None,
            language: Optional[FhirCode] = None,
            data: Optional[FhirBase64Binary] = None,
            url: Optional[FhirUri] = None,
            size: Optional[FhirUnsignedInt] = None,
            hash_: Optional[FhirBase64Binary] = None,
            title: Optional[FhirString] = None,
            creation: Optional[FhirDateTime] = None
            ) -> 'FhirAttachment':
        """
        Attachment Resource in FHIR
        https://hl7.org/FHIR/datatypes.html#Attachment
        Content in a format defined elsewhere
        + Rule: If the Attachment has data, it SHALL have a contentType

        :param contentType: Mime type of the content, with charset etc. https://hl7.org/FHIR/valueset-mimetypes.html
        :param language: Human language of the content (BCP-47). https://hl7.org/FHIR/valueset-languages.html
        :param data: Data inline, base64ed
        :param url: Uri where the data can be found
        :param size: Number of bytes of content (if url provided)
        :param hash_: Hash of the data (sha-1, base64ed)
        :param title: Label to display in place of the data
        :param creation: Date attachment was first created
        """
        return FhirAttachment(
            contentType=contentType,
            language=language,
            data=data,
            url=url,
            size=size,
            hash_=hash_,
            title=title,
            creation=creation
        )