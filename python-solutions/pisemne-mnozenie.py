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

a_2 = int(a_number[0])
a_1 = int(a_number[1])
a_0 = int(a_number[2])

b_2 = int(b_number[0])
b_1 = int(b_number[1])
b_0 = int(b_number[2])

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

#   kazde przesuniecie w lewo to 10^n, gdzie n to wykladnik 10, gdy brak jest przesuniecia wspolczynnik przyjmuje wartosc 10^0 czyli 1; 
#   jednak nie udalo sie uniknac mnozenia, natomiast mnozenie przez 10 nie powinno mocno obciazac komputera - warto byloby sprawdzic, ktory ze sposobow (algorytmow) jest bardziej wydajny a*b czy moj - w szczegolnosci w odniesieniu do ogromnych liczb;