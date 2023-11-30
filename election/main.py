import itertools
import time

import numpy as np

from election.demographics import Demographics

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
    for gender, age, location in itertools.product(
        Demographics.genders(), Demographics.age_ranges(), Demographics.locations()
    )
]
probabilities = [a * b for a, b in itertools.product(gender_age_probabilities, location_probabilities)]

# Some configuration options to rig/tune the election.

POPULATION_SIZE = 320_000_000

# Where the magic all happens

if __name__ == "__main__":
    start = time.perf_counter()
    population = np.random.choice(choices, POPULATION_SIZE, p=probabilities)
    print(f"Generated {len(population)} people in {time.perf_counter() - start}s")
