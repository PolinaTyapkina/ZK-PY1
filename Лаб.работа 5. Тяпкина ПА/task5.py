from random import sample
import string

population = string.ascii_lowercase + string.ascii_uppercase + string.digits
n = 8


def get_random_password() -> str:
    list_ = sample(population, n, counts=None)
    password = "".join(list_)
    return password


print(get_random_password())
#
