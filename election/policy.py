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
        Demographic.MALE: np.random.uniform(0, 0.5),
        Demographic.FEMALE: np.random.uniform(0, 0.5),
        Demographic.UNDER_21: np.random.uniform(0, 0.4),
        Demographic.UNDER_45: np.random.uniform(0.3, 0.7),
        Demographic.UNDER_65: np.random.uniform(0.5, 0.9),
        Demographic.OVER_65: np.random.uniform(0.6, 1),
        Demographic.URBAN: np.random.uniform(0.2, 0.8),
        Demographic.SUBURBAN: np.random.uniform(0.3, 0.7),
        Demographic.RURAL: np.random.uniform(0, 0.5),
    },
)

UNIV_HEALTHCARE = Policy(
    description=(
        "A large group of uninsured citizens have petitioned the government to provide a universal healthcare system, "
        "citing the poor health of many low and middle-class workers. "
    ),
    weights={
        Demographic.MALE: np.random.uniform(0.4, 0.8),
        Demographic.FEMALE: np.random.uniform(0.6, 1),
        Demographic.UNDER_21: np.random.uniform(0.6, 0.9),
        Demographic.UNDER_45: np.random.uniform(0.4, 0.9),
        Demographic.UNDER_65: np.random.uniform(0.4, 0.7),
        Demographic.OVER_65: np.random.uniform(0.4, 0.8),
        Demographic.URBAN: np.random.uniform(0.6, 1),
        Demographic.SUBURBAN: np.random.uniform(0.3, 0.9),
        Demographic.RURAL: np.random.uniform(0.3, 0.7),
    },
)

FINANCIAL_AID = Policy(
    description=(
        "Students from many universities are protesting about the rising financial cost of studying at university and "
        "are demanding that the government provide more financial aid to students."
    ),
    weights={
        Demographic.MALE: np.random.uniform(0.4, 0.8),
        Demographic.FEMALE: np.random.uniform(0.6, 0.8),
        Demographic.UNDER_21: np.random.uniform(0.7, 1),
        Demographic.UNDER_45: np.random.uniform(0.5, 0.7),
        Demographic.UNDER_65: np.random.uniform(0.3, 0.5),
        Demographic.OVER_65: np.random.uniform(0.0, 0.2),
        Demographic.URBAN: np.random.uniform(0.8, 1),
        Demographic.SUBURBAN: np.random.uniform(0.5, 0.8),
        Demographic.RURAL: np.random.uniform(0, 0.2),
    },
)

AIR_QUALITY = Policy(
    description=(
        "A sudden rise in temperatures has sparked a debate over what the government should do to counter "
        "global warming, if anything. The environmentalist movement is up-in-arms and has camped outside your "
        "residence for three days demanding an end to all toxic emissions."
    ),
    weights={
        Demographic.MALE: np.random.uniform(0.3, 0.8),
        Demographic.FEMALE: np.random.uniform(0.6, 0.8),
        Demographic.UNDER_21: np.random.uniform(0.6, 1),
        Demographic.UNDER_45: np.random.uniform(0.5, 0.9),
        Demographic.UNDER_65: np.random.uniform(0.5, 0.7),
        Demographic.OVER_65: np.random.uniform(0, 0.4),
        Demographic.URBAN: np.random.uniform(0.6, 1),
        Demographic.SUBURBAN: np.random.uniform(0.3, 0.8),
        Demographic.RURAL: np.random.uniform(0, 0.2),
    },
)
