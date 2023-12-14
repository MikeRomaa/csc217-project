import itertools
import time

import numpy as np
from matplotlib import pyplot as plt

from election import constants, demographic
from election.candidate import CANDIDATES
from election.systems import ApprovalVoting, Election, FirstPastThePost, RankedChoiceVoting

# Age and gender probabilities are provided by the Census Bureau as a joint statistic.
# Therefore, we'll construct a joint probability mass function.
# Probabilities are listed below in the same order as they appear in `Demographics`.
#
# Sources:
# https://www.census.gov/data/tables/2022/demo/age-and-sex/2022-age-sex-composition.html
# https://www.pewresearch.org/social-trends/2018/05/22/demographic-and-economic-trends-in-urban-suburban-and-rural-communities/

male_age_probabilities = [0.024, 0.205, 0.158, 0.101]
female_age_probabilities = [0.023, 0.205, 0.164, 0.120]
gender_age_probabilities = male_age_probabilities + female_age_probabilities
location_probabilities = [0.31, 0.55, 0.14]

# Get every combination of genders, age ranges, and locations using the cartesian product of the subsets.
# This will help us make the selection using a joint probability mass function using `numpy.random.choice`.

choices = [
    gender | age | location
    for gender, age, location in itertools.product(demographic.GENDERS, demographic.AGE_RANGES, demographic.LOCATIONS)
]
probabilities = [a * b for a, b in itertools.product(gender_age_probabilities, location_probabilities)]

# Where the magic all happens

if __name__ == "__main__":
    start = time.perf_counter()
    population = np.random.choice(choices, constants.POPULATION_SIZE, p=probabilities)
    print(f"Generated {constants.POPULATION_SIZE} people in {time.perf_counter() - start}s")

    election = Election(CANDIDATES, population)

    for system in [FirstPastThePost, RankedChoiceVoting, ApprovalVoting]:
        winner = system.tally(election)
        print(system.__name__, winner.name)

        ratings = [winner.approval(person) for person in population]
        mean=round(statistics.mean(ratings),2)
        stdev= round(statistics.stdev(ratings),2)

        fig, ax = plt.subplots()
        ax.hist(ratings, bins=10, rwidth=0.9)
        ax.set_xlim(left=-2, right=2)
        plt.xlabel("Approval Rating")
        plt.text(1, 1000, rf'$\mu$ = {mean}' + '\n' + rf'$\sigma$ = {stdev}' )
        ax.set_title(f"Approval Rating Distribution for {winner.name}")

        plt.show()
