print("\nWitaj w programie mnozacym dwie liczby trzycyfrowe w sposob zbliczony do pisemnego\n")

a_0 = int(input('\n\nPodaj pierwsza cyfre liczby a - poczawszy od jednosci:\n '))
a_1 = int(input('Podaj druga cyfre liczby a - poczawszy od dziesiatek:\n '))
a_2 = int(input('Podaj trzecia cyfre liczby a - poczawszy od setek:\n '))

print(("\n\nTwoja liczba a to: \n") + str(a_2) + str(a_1) + str(a_0))
a_debug = a_0 + (10 * a_1) + (100 * a_2)

b_0 = int(input('\n\nPodaj pierwsza cyfre liczby b - poczawszy od jednosci:\n '))
b_1 = int(input('Podaj druga cyfre liczby b - poczawszy od dziesiatek:\n '))
b_2 = int(input('Podaj trzecia cyfre liczby b - poczawszy od setek:\n '))

print(("\n\nTwoja liczba b to: \n") + str(b_2) + str(b_1) + str(b_0))
b_debug = b_0 + (10 * b_1) + (100 * b_2)

c_start_program = int(input('Aby rozpoczac napisz 1, aby zakonczyc napisz 0, wprowadz cyfre i nacisnij enter: \n'))

# if a_debug or b_debug <= 9:
#     print("Podales zbyt mala liczbe!")

if c_start_program == 1:
    c_0 = b_0 * a_0 #   *1
    print ("\n\n          "+ str(c_0))
    c_1 = b_0 * a_1   *10
    print ("\n\n         "+ str(c_1))
    c_2 = b_0 * a_2    *100
    print ("\n\n        " + str(c_2))
    c_3 = b_1 * a_0    *10
    print ("\n\n       "+ str(c_3))
    c_4 = b_1 * a_1    *100
    print ("\n\n      "+ str(c_4))
    c_5 = b_1 * a_2    *1000
    print ("\n\n     " + str(c_5))
    c_6 = b_2 * a_0    *100
    print ("\n\n    "+ str(c_6))
    c_7 = b_2 * a_1    *1000
    print ("\n\n   "+ str(c_7))
    c_8 = b_2 * a_2    *10000
    print ("\n\n+ " + str(c_8))
    wynik = (c_0 + c_1 + + c_2 + c_3 + c_4 + c_5 + c_6 + c_7 + c_8)
    print ("===========\n " + str(wynik))
else:
    print ("\n\nDo zobaczenia!")

#   kazde przesuniecie w lewo to 10^n, gdzie n to wykladnik 10, gdy brak jest przesuniecia wspolczynnik przyjmuje wartosc 10^0 czyli 1; 
#   jednak nie udalo sie uniknac mnozenia, natomiast mnozenie przez 10 nie powinno mocno obciazac komputera - warto byloby sprawdzic, ktory ze sposobow (algorytmow) jest bardziej wydajny a*b czy moj - w szczegolnosci w odniesieniu do ogromnych liczb;