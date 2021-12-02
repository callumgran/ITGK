import random

bokstaver = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def bil_reg_generator():
    string = ""
    for i in range(2):
        string = string + bokstaver[random.randint(0, 25)]
    for i in range(5):
        n = random.randint(0, 9)
        while i == 0 and n == 0:
            n = random.randint(0, 9)
        string = string + str(n)
    return string


print(bil_reg_generator())
