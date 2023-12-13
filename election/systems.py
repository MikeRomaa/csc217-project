from abc import ABC, abstractmethod

from election.candidate import Candidate
from election.demographic import Demographic


class Election:
    """Runs the simulation and exposes the data for `ElectoralSystem` classes to consume."""

    candidates: dict[str, Candidate]
    results: dict[str, list[int]]

    def __init__(self, candidates: list[Candidate], population: Demographic):
        """Performs what is essentially a ranked choice election.

        All the data we need for our four political system can be derived
        from the results of a ranked choice election.
        """
        self.candidates = {candidate.name: candidate for candidate in candidates}
        # For each candidate, there is an array that represents how many votes they got for each rank.
        # For example, the 2nd entry in a candidate's array is the amount of 2nd rank votes they received.
        self.results = {candidate.name: [0] * len(candidates) for candidate in candidates}

        for person in population:
            choices = sorted(
                candidates,
                key=lambda candidate: candidate.approval(person),
            )
            for i, choice in enumerate(choices):
                self.results[choice.name][i] += 1


class ElectoralSystem(ABC):
    """Common interface for electoral systems."""

    @staticmethod
    @abstractmethod
    def tally(election: Election) -> Candidate:
        """Tallies up the election results and returns the winning candidate."""


class PopularVote(ElectoralSystem):
    """In a popular vote election, the candidate with the most first-choice votes is declared the winner."""

    @staticmethod
    def tally(election: Election) -> Candidate:
        winner, _ = max(
            election.results.items(),
            key=lambda item: item[1][0],
        )

        return election.candidates[winner]


class FirstPastThePost(ElectoralSystem):
    # TODO
    pass


class ApprovalVoting(ElectoralSystem):
    # TODO
    pass


class RankedChoiceVoting(ElectoralSystem):
    # TODO
    pass
