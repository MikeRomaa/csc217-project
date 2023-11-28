import itertools

import numpy as np
import numpy.typing as np_type

from election.demographics import Demographics

# Age and gender probabilities are provided by the Census Bureau as a joint statistic.
# Therefore, we'll construct a joint probability mass function.
# Probabilities are listed below in the same order as they appear in `Demographics`.
#
# Source:
# https://www.census.gov/data/tables/2022/demo/age-and-sex/2022-age-sex-composition.html

male_age_probabilities = [0.024, 0.205, 0.158, 0.101]
female_age_probabilities = [0.023, 0.205, 0.164, 0.120]
gender_age_probabilities = male_age_probabilities + female_age_probabilities

# Get every combination of genders and age ranges using the cartesian product of the two subsets.
# This will help us make the selection using a joint probability mass function using `numpy.random.choice`.

gender_age_choices = [
    gender | age for gender, age in
    itertools.product(Demographics.genders(), Demographics.age_ranges())
]

# Source:
# https://www.pewresearch.org/social-trends/2018/05/22/demographic-and-economic-trends-in-urban-suburban-and-rural-communities/

location_probabilities = [0.31, 0.55, 0.14]


def generate_population(n: int) -> np_type.NDArray[Demographics]:
    gender_ages = np.random.choice(gender_age_choices, n, p=gender_age_probabilities)
    locations = np.random.choice(Demographics.locations(), n, p=location_probabilities)

    return gender_ages | locations


if __name__ == "__main__":
    print(generate_population(1_000_000))
