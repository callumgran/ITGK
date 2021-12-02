def tekst_til_ascii():
    ascii_verdier = []
    tall = 0
    tekst = input("Skriv inn det som skal konverteres: ")
    for i in tekst:
        ascii_verdier.append(ord(i))
    for i in ascii_verdier[len(ascii_verdier) - 5:]:
        tall += i
    return chr(tall)


print(tekst_til_ascii())
