day = 3


def get_monday():
    return "This is monday!"


def get_tuesday():
    return "This is tuesday!"


def get_wednesday():
    return "This is Wednesday!"


def get_thursday():
    return "This is thursday!"


def get_default():
    return "This is unknow day!"


get_days = {
    0: get_monday,
    1: get_thursday,
    2: get_wednesday,
    3: get_tuesday,
}
print(get_days.get(day, get_default)())

