from dataclasses import dataclass
from functools import reduce

import numpy as np

from election.demographic import Demographic


@dataclass
class Policy:
    description: str
    weights: dict[Demographic, float]

    def approval(self, demographics: Demographic) -> float:
        """Returns probability of the given person voting YES for the policy.

        Args:
            Demographics representing a person in the population.

        Returns:
            Probability between 0 and 1 obtained from multiplying the weights of each
            component of the demographics.
        """
        return reduce(lambda x, y: x * self.weights[y], demographics, 1)


TECHNOLOGY_USE = Policy(
    description=(
        "Teenagers haven't been seen outdoors since the nation connected to the Internet. "
        "Congress is proposing a strict five hour limit on recreational internet use."
    ),
    weights={
        # TODO: Replace with actual probabilities
        Demographic.MALE: np.random.uniform(),
        Demographic.FEMALE: np.random.uniform(),
        Demographic.UNDER_21: np.random.uniform(),
        Demographic.UNDER_45: np.random.uniform(),
        Demographic.UNDER_65: np.random.uniform(),
        Demographic.OVER_65: np.random.uniform(),
        Demographic.URBAN: np.random.uniform(),
        Demographic.SUBURBAN: np.random.uniform(),
        Demographic.RURAL: np.random.uniform(),
    },
)

UNIV_HEALTHCARE = Policy(
    description=(
        "A large group of uninsured citizens have petitioned the government to provide a universal healthcare system, "
        "citing the poor health of many low and middle-class workers. "
    ),
    weights={
        # TODO: Replace with actual probabilities
        Demographic.MALE: np.random.uniform(),
        Demographic.FEMALE: np.random.uniform(),
        Demographic.UNDER_21: np.random.uniform(),
        Demographic.UNDER_45: np.random.uniform(),
        Demographic.UNDER_65: np.random.uniform(),
        Demographic.OVER_65: np.random.uniform(),
        Demographic.URBAN: np.random.uniform(),
        Demographic.SUBURBAN: np.random.uniform(),
        Demographic.RURAL: np.random.uniform(),
    },
)

FINANCIAL_AID = Policy(
    description=(
        "Students from many universities are protesting about the rising financial cost of studying at university and "
        "are demanding that the government provide more financial aid to students."
    ),
    weights={
        # TODO: Replace with actual probabilities
        Demographic.MALE: np.random.uniform(),
        Demographic.FEMALE: np.random.uniform(),
        Demographic.UNDER_21: np.random.uniform(),
        Demographic.UNDER_45: np.random.uniform(),
        Demographic.UNDER_65: np.random.uniform(),
        Demographic.OVER_65: np.random.uniform(),
        Demographic.URBAN: np.random.uniform(),
        Demographic.SUBURBAN: np.random.uniform(),
        Demographic.RURAL: np.random.uniform(),
    },
)

AIR_QUALITY = Policy(
    description=(
        "A sudden rise in temperatures has sparked a debate over what the government should do to counter "
        "global warming, if anything. The environmentalist movement is up-in-arms and has camped outside your "
        "residence for three days demanding an end to all toxic emissions."
    ),
    weights={
        # TODO: Replace with actual probabilities
        Demographic.MALE: np.random.uniform(),
        Demographic.FEMALE: np.random.uniform(),
        Demographic.UNDER_21: np.random.uniform(),
        Demographic.UNDER_45: np.random.uniform(),
        Demographic.UNDER_65: np.random.uniform(),
        Demographic.OVER_65: np.random.uniform(),
        Demographic.URBAN: np.random.uniform(),
        Demographic.SUBURBAN: np.random.uniform(),
        Demographic.RURAL: np.random.uniform(),
    },
)
