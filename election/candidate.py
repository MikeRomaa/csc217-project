from dataclasses import dataclass

from election import policy
from election.demographic import Demographic
from election.policy import Policy


@dataclass
class Candidate:
    name: str
    party: str
    stances: list[tuple[Policy, bool]]

    def approval(self, demographics: Demographic) -> float:
        """Returns approval rating for the candidate by the given person.

        Args:
            Demographics representing a person in the population.

        Returns:
            Floating number between -2 and 2, with 0 being the baseline approval
            representing indifference to the candidate.
        """
        return sum(
            # We first adjust the approval probability for the policy by a factor of 0.5.
            # This means that if somebody is less than 50% likely to vote YES for a policy,
            # they will tend to dislike candidates that strongly support the policy.
            (pol.approval(demographics) - 0.5)
            # We then multiply this new adjusted probability by a scalar, either 1 or -1,
            # that will yield a positive number if the voter and candidate agree, and
            # a negative number if they disagree.
            * (1 if stance else -1)
            for pol, stance in self.stances
        )


CANDIDATES = [
    Candidate(
        name="Justin Case",
        party="Birthday Party",
        stances=[
            (policy.TECHNOLOGY_USE, True),
            (policy.UNIV_HEALTHCARE, True),
            (policy.FINANCIAL_AID, True),
            (policy.AIR_QUALITY, True),
        ],
    ),
    Candidate(
        name="Jason Response",
        party="Abolish Political Parties Party",
        stances=[
            (policy.TECHNOLOGY_USE, True),
            (policy.UNIV_HEALTHCARE, True),
            (policy.FINANCIAL_AID, False),
            (policy.AIR_QUALITY, False),
        ],
    ),
    Candidate(
        name="Ruüd van Driver",
        party="The Best Party",
        stances=[
            (policy.TECHNOLOGY_USE, False),
            (policy.UNIV_HEALTHCARE, True),
            (policy.FINANCIAL_AID, True),
            (policy.AIR_QUALITY, True),
        ],
    ),
    Candidate(
        name="Janelle Lawless",
        party="Independent",
        stances=[
            (policy.TECHNOLOGY_USE, False),
            (policy.UNIV_HEALTHCARE, False),
            (policy.FINANCIAL_AID, False),
            (policy.AIR_QUALITY, False),
        ],
    ),
]
