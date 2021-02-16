# TODO: we need a robust way to check for circular dependency


def test_condition_import_cycle() -> None:
    from spark_auto_mapper_fhir.resources.condition import Condition

    print(Condition.__name__)


def test_cliam_import_cycle() -> None:
    from spark_auto_mapper_fhir.backbone_elements.related_claim_backbone_element import RelatedClaimBackboneElement
    from spark_auto_mapper_fhir.resources.claim import Claim

    print(RelatedClaimBackboneElement.__name__)
    print(Claim.__name__)
