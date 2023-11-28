import enum


class Demographics(enum.Flag):
    MALE = enum.auto()
    FEMALE = enum.auto()

    UNDER_21 = enum.auto()  # 18 to 20 years old
    UNDER_45 = enum.auto()  # 21 to 44 years old
    UNDER_65 = enum.auto()  # 45 to 64 years old
    OVER_65 = enum.auto()  # 65 years and over

    URBAN = enum.auto()
    SUBURBAN = enum.auto()
    RURAL = enum.auto()

    @staticmethod
    def genders():
        return [
            Demographics.MALE,
            Demographics.FEMALE,
        ]

    @staticmethod
    def age_ranges():
        return [
            Demographics.UNDER_21,
            Demographics.UNDER_45,
            Demographics.UNDER_65,
            Demographics.OVER_65,
        ]

    @staticmethod
    def locations():
        return [
            Demographics.URBAN,
            Demographics.SUBURBAN,
            Demographics.RURAL,
        ]
