from enum import Enum

class Decision(Enum):
    pass

class CloneMergeDecision(Decision):
    NOTHING = 1
    CLONE = 2
    SQUASH = 3
    MERGE = 4

class DecisionModel(object):

    def decide(self, novelties):
        raise NotImplementedError


class NoCloneMerge(DecisionModel):
    """Example stub for a DecisionModel subclass, always returns a NOTHING
    decision for all inputs."""

    def decide(self, novelties):
        return [Decision.NOTHING for i in novelties]

class RandomCloneMerge(DecisionModel):

    def __init__(self, seed):
        raise NotImplementedError

class WExplore2(DecisionModel):
    # Nazanin Put your code here!!
    pass

