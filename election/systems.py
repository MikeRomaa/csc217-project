from abc import ABC, abstractmethod

import numpy as np
from matplotlib import pyplot as plt

from election import constants
from election.candidate import Candidate
from election.demographic import Demographic


class Election:
    """Runs the simulation and exposes the data for `ElectoralSystem` classes to consume."""

    candidates: dict[str, Candidate]
    results: list[list[float]]

    def __init__(self, candidates: list[Candidate], population: Demographic):
        """Performs what is essentially a ranked choice election.

        All the data we need for our four political system can be derived
        from the results of a ranked choice election.
        """
        self.candidates = {candidate.name: candidate for candidate in candidates}
        # For each candidate, there is an array that represents how many votes they got for each rank.
        # For example, the 2nd entry in a candidate's array is the amount of 2nd rank votes they received.
        self.results = []

        for person in population:
            self.results.append([
                candidate.approval(person)
                for candidate in self.candidates.values()
            ])


class ElectoralSystem(ABC):
    """Common interface for electoral systems."""

    @staticmethod
    @abstractmethod
    def tally(election: Election) -> Candidate:
        """Tallies up the election results and returns the winning candidate."""

    @staticmethod
    def plot(data: dict[str, int]) -> plt.Axes:
        sorted_data = dict(sorted(data.items()))

        fig, ax = plt.subplots()
        fig.set_size_inches(10, 5)

        color_map = plt.get_cmap("tab20c")

        y = np.arange(len(sorted_data))
        ax.barh(
            y,
            sorted_data.values(),
            color=color_map.colors[::4],
            align="center",
        )

        ax.invert_yaxis()
        ax.set_yticks(y, sorted_data.keys())
        ax.set_xlabel("Votes")
        ax.set_xlim(left=0, right=constants.POPULATION_SIZE)

        return ax


class FirstPastThePost(ElectoralSystem):
    """In a first-past-the-post election, the candidate with the most first-choice votes is declared the winner."""

    @staticmethod
    def tally(election: Election) -> Candidate:
        counts = {candidate: 0 for candidate in election.candidates}

        for vote in election.results:
            choice, _ = max(
                zip(election.candidates.values(), vote),
                key=lambda x: x[1]
            )

            counts[choice.name] += 1

        FirstPastThePost.plot(counts)
        winner = max(counts, key=counts.get)
        return election.candidates[winner]

    @staticmethod
    def plot(counts: dict[str, int]):
        ax = ElectoralSystem.plot(counts)

        ax.set_title("First Past The Post (FPTP) Election")

        plt.subplots_adjust(left=0.14)
        plt.show()


class RankedChoiceVoting(ElectoralSystem):
    """In a ranked-choice election (also known as instant-runoff), candidates are eliminated until somebody obtains a
    majority, and their votes are redistributed according to higher-order choices."""

    @staticmethod
    def tally(election: Election) -> Candidate:
        remaining_candidates = set(election.candidates)

        round_num = 1
        max_rounds = len(remaining_candidates) - 1

        while remaining_candidates:
            # Calculates total votes for each remaining candidate
            counts = {candidate: 0 for candidate in remaining_candidates}

            for vote in election.results:
                choice, _ = max(
                    filter(
                        lambda x: x[0].name in remaining_candidates,
                        zip(election.candidates.values(), vote),
                    ),
                    key=lambda x: x[1]
                )

                counts[choice.name] += 1

            RankedChoiceVoting.plot(counts, round_num, max_rounds)

            # Check if any candidate has a majority. Stop the count if yes
            for candidate, votes in counts.items():
                if votes > constants.POPULATION_SIZE / 2:
                    return election.candidates[candidate]

            # Otherwise, eliminate the candidate with the fewest votes
            remaining_candidates.remove(min(counts, key=counts.get))
            round_num += 1

    @staticmethod
    def plot(counts: dict[str, int], round_num: int, max_rounds: int):
        ax = ElectoralSystem.plot(counts)

        ax.set_title(f"Ranked Choice (RCV) Election [{round_num} of {max_rounds} rounds]")
        majority = constants.POPULATION_SIZE / 2
        ax.plot([majority, majority], [-0.5, 3.5], "k--")

        plt.subplots_adjust(left=0.14)
        plt.show()


class ApprovalVoting(ElectoralSystem):
    """In an approval voting system, people are allowed to vote for any number of people they support. The candidate
    with the most total votes is declared the winner.

    In our simulation, support is defined as having an approval rating of at least 0. This does mean that a person
    might not vote for anybody if their approval ratings are all below the threshold.
    """

    @staticmethod
    def tally(election: Election) -> Candidate:
        counts = {candidate: 0 for candidate in election.candidates}

        for vote in election.results:
            # We get all candidates that the person "supports" (approval >= 0)
            choices = filter(
                lambda x: x[1] >= 0,
                zip(election.candidates.values(), vote),
            )

            for candidate, _ in choices:
                counts[candidate.name] += 1

        ApprovalVoting.plot(counts)
        winner = max(counts, key=counts.get)
        return election.candidates[winner]

    @staticmethod
    def plot(counts: dict[str, int]):
        ax = ElectoralSystem.plot(counts)

        ax.set_title("Approval Voting Election")

        plt.subplots_adjust(left=0.14)
        plt.show()
