from abc import ABC


class ElectoralSystem(ABC):
    """Common interface for all electoral systems."""

    def __init__(self, candidates):
        self.candidates = candidates


class FirstPastThePost(ElectoralSystem):
    # TODO
    pass


class ApprovalVoting(ElectoralSystem):
    # TODO
    pass


class RankedChoiceVoting(ElectoralSystem):
    # TODO
    pass


class PopularVote(ElectoralSystem):
    # TODO
    pass
