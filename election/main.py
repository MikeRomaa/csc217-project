import itertools
import time

import numpy as np
from matplotlib import pyplot as plt

from election import demographic
from election.candidate import CANDIDATES
from election.systems import Election, PopularVote

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

# Some configuration options to rig/tune the election.

POPULATION_SIZE = 10_000

# Where the magic all happens

if __name__ == "__main__":
    # user = demographic.Demographic.MALE | demographic.Demographic.UNDER_21 | demographic.Demographic.URBAN
    # print([c.approval(user) for c in candidate.CANDIDATES])
    start = time.perf_counter()
    population = np.random.choice(choices, POPULATION_SIZE, p=probabilities)
    print(f"Generated {POPULATION_SIZE} people in {time.perf_counter() - start}s")

    num_candidates = len(CANDIDATES)
    election = Election(CANDIDATES, population)

    print(election.results)
    print(PopularVote.tally(election).name)

    y = np.arange(num_candidates)
    width = 0.5

    fig, ax = plt.subplots()
    fig.set_size_inches(10, 5)

    color_map = plt.get_cmap("tab20c")

    bottom = np.zeros(num_candidates)
    for i in range(num_candidates):
        values = [c[i] for c in election.results.values()]
        ax.barh(
            y + width,
            values,
            width,
            left=bottom,
            color=color_map.colors[i::4],
        )
        bottom += values

    ax.invert_yaxis()
    ax.set_yticks(y + width, (c.name for c in CANDIDATES))
    ax.set_xlabel('Votes')
    ax.set_title('Ranked Choice Votes per Candidate')

    plt.subplots_adjust(left=0.14)
    plt.show()
