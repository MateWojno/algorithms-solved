#   [PL] `Algorytmy rozwiazane w C++/C#/Pythonie/JavaScript;`


##      `#1 algorytm pisemnego mnozenia `
*   dwoch liczb calkowitych dodatnich, przynajmniej dwocyfrowych

###     `*specyfikacja problemu;*`

-   zalozenia [dane_wejsciowe] - a, b - liczby calkowite, a > 9, b > 9 | wynik [dane_wyjsciowe] a * b;
-   opis dzialania algorytmu:
                           1/   zapisz liczbe a;    [start]
                           2/   zapisz liczbe b ponizej liczby a tak, zeby jej cyfry jednosci, dziesiatek, setek itd. znajdowaly sie odpowiednio nad cyframi jednosci, dzisiatek, setek liczby a.
                           3/   dla kazdej z cyfr liczby b, poczawszy od cyfry jednosci, traktowanych jako liczby jednocyfrowe, wykonaj kroki 4 i 5;
                           4/   wykonaj mnozenie (oblicz iloczyn) biezacej liczby jednocyfrowej i liczby a;
                           5/   jesli iloczyn jest pierwszym czastkowym iloczynem to zapisz go ponizej  liczby b (jednosci pod jednosciami, dzisiatki pod dziesiatkami itd.). Kolejne iloczyny zapisuj z odpowiednim przesunieciem w lewo, tj. cyfre jednosci iloczynu zapisz pod cyfra dzisiatek poprzedniego iloczynu, cyfre dziesiatek iloczynu zapisz pod cyfra etek poprzedniego iloczynu itd;
                           6/   zsumuj czastkowe iloczyny [stop]

####    `rozwiazanie:`
-   aby 'przesuwac' liczby w lewo o n [jednostek] nalezy je pomnozyc przez 10^n (w systemie dziesietnym, ktorego uzywamy);


