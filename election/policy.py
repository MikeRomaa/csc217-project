from dataclasses import dataclass

from election.demographic import Demographic


@dataclass
class Policy:
    description: str
    weights: dict[Demographic, float]


TECHNOLOGY_USE = Policy(
    description=(
        "Teenagers haven't been seen outdoors since the nation connected to the Internet. "
        "Congress is proposing a strict five hour limit on recreational internet use."
    ),
    weights={
        Demographic.MALE: 0,
        Demographic.FEMALE: 0,
        Demographic.UNDER_21: 0,
        Demographic.UNDER_45: 0,
        Demographic.UNDER_65: 0,
        Demographic.OVER_65: 0,
        Demographic.URBAN: 0,
        Demographic.SUBURBAN: 0,
        Demographic.RURAL: 0,
    },
)

UNIV_HEALTHCARE = Policy(
    description=(
        "A large group of uninsured citizens have petitioned the government to provide a universal healthcare system, "
        "citing the poor health of many low and middle-class workers. "
    ),
    weights={
        Demographic.MALE: 0,
        Demographic.FEMALE: 0,
        Demographic.UNDER_21: 0,
        Demographic.UNDER_45: 0,
        Demographic.UNDER_65: 0,
        Demographic.OVER_65: 0,
        Demographic.URBAN: 0,
        Demographic.SUBURBAN: 0,
        Demographic.RURAL: 0,
    },
)

FINANCIAL_AID = Policy(
    description=(
        "Students from many universities are protesting about the rising financial cost of studying at university and "
        "are demanding that the government provide more financial aid to students."
    ),
    weights={
        Demographic.MALE: 0,
        Demographic.FEMALE: 0,
        Demographic.UNDER_21: 0,
        Demographic.UNDER_45: 0,
        Demographic.UNDER_65: 0,
        Demographic.OVER_65: 0,
        Demographic.URBAN: 0,
        Demographic.SUBURBAN: 0,
        Demographic.RURAL: 0,
    },
)

AIR_QUALITY = Policy(
    description=(
        "A sudden rise in temperatures has sparked a debate over what the government should do to counter "
        "global warming, if anything. The environmentalist movement is up-in-arms and has camped outside your "
        "residence for three days demanding an end to all toxic emissions."
    ),
    weights={
        Demographic.MALE: 0,
        Demographic.FEMALE: 0,
        Demographic.UNDER_21: 0,
        Demographic.UNDER_45: 0,
        Demographic.UNDER_65: 0,
        Demographic.OVER_65: 0,
        Demographic.URBAN: 0,
        Demographic.SUBURBAN: 0,
        Demographic.RURAL: 0,
    },
)
