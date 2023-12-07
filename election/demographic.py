import enum


class Demographic(enum.Flag):
    MALE = enum.auto()
    FEMALE = enum.auto()

    UNDER_21 = enum.auto()  # 18 to 20 years old
    UNDER_45 = enum.auto()  # 21 to 44 years old
    UNDER_65 = enum.auto()  # 45 to 64 years old
    OVER_65 = enum.auto()  # 65 years and over

    URBAN = enum.auto()
    SUBURBAN = enum.auto()
    RURAL = enum.auto()


GENDERS = [
    Demographic.MALE,
    Demographic.FEMALE,
]

AGE_RANGES = [
    Demographic.UNDER_21,
    Demographic.UNDER_45,
    Demographic.UNDER_65,
    Demographic.OVER_65,
]

LOCATIONS = [
    Demographic.URBAN,
    Demographic.SUBURBAN,
    Demographic.RURAL,
]
