from spark_auto_mapper.data_types.literal import AutoMapperDataTypeLiteral
from spark_auto_mapper.type_definitions.native_types import AutoMapperNativeSimpleType

from spark_auto_mapper_fhir.classproperty import classproperty


class FhirAdministrativeGenderCode(AutoMapperDataTypeLiteral):
    @classmethod
    def map(cls,
            value: AutoMapperNativeSimpleType
            ) -> 'FhirAdministrativeGenderCode':
        assert value in ["male", "female", "other", "unknown"]
        return cls(value=value)

    # noinspection PyMethodParameters
    @classproperty
    def male(cls):
        """
        Male
        """
        # noinspection PyCallingNonCallable
        return cls("male")

    # noinspection PyMethodParameters
    @classproperty
    def female(cls):
        """
        Female
        """
        # noinspection PyCallingNonCallable
        return cls("female")

    # noinspection PyMethodParameters
    @classproperty
    def other(cls):
        """
        Other
        """
        # noinspection PyCallingNonCallable
        return cls("other")

    # noinspection PyMethodParameters
    @classproperty
    def unknown(cls):
        """
        Unknown
        """
        # noinspection PyCallingNonCallable
        return cls("unknown")
