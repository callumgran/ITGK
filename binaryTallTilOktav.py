binaryNumbers = {'0', '1'}


def binary_number_checker(t):
    if binaryNumbers == t or t == {'0'} or t == {'1'}:
        return True
    else:
        return False


def binary_number_converter():
    binary = str(input("Skriv inn et binært tall: "))
    t = set(binary)
    if binary_number_checker(t):
        while len(binary) % 8 != 0:
            binary = "0" + binary
        return binary
    else:
        return "Det du skrev var ikke et binært tall"


print(binary_number_converter())
