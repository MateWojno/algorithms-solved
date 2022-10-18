while True:
    try:
        a = int(input("\n\nPodaj pierwsza liczbe 3-cyfrowa:\n"))
        b = int(input("\n\nPodaj druga liczbe 3-cyfrowa:\n"))
    except ValueError: 
        print("\nPodales nieprawidlowe dane\nZacznij od poczatku...")
        continue
    while a < 100 or a > 1000 or b < 100 or b > 1000:
        print ("\nPodales nieprawidlowe dane\nZacznij od poczatku...")
        a = int(input("\n\nPodaj pierwsza liczbe 3-cyfrowa:\n"))
        b = int(input("\n\nPodaj druga liczbe 3-cyfrowa:\n"))
    else:
        print("\n\nTwoja liczba a to:\n" + str(a) + "\n\nTwoja liczba b to:\n" + str(b))
        break

a_number = str(a) 
b_number = str(b)
print('\n\n' + a_number[0] + '  to index 0 str a' + '\n' + a_number[1] + '  to index 1 str a' + '\n' + a_number[2] + '  to index 2 str a')
print('\n\n' + b_number[0] + '  to index 0 str b' + '\n' + b_number[1] + '  to index 1 str b' + '\n' + b_number[2] + '  to index 2 str b')

a2 = int(a_number[0])
a1 = int(a_number[1])
a0 = int(a_number[2])

b2 = int(b_number[0])
b1 = int(b_number[1])
b0 = int(b_number[2])
