from collections import OrderedDict


def calculate_total_revenue(rows, CHOICES, sort_by=None):
    """Funckja odpowiedzialna za obliczenie wartości produktu razy jego ilość z przekazanych do funkcji danych.
       Funkcja przyjmuje argument rows w którym przekazujemy dane na których będzie wykonywać obliczenia,
       argumnet CHOICES, w którym znajdują się zdefiniowane indeksy wierszy, oraz argument opcjonalny sort_by,
       który wskazuje wg. jakiego indeksu wierszu mamy przefiltrować dane - np. 'product_name"""
    CHOICES = CHOICES
    report = OrderedDict()
    transaction_list = OrderedDict()

    if sort_by:
        # Jeżeli wystąpi argument opcjonalny sort_by, wykonujemy iteracje poprzez wszystkie elementy rows,
        # następnie funkcja sprawdza czy nazwa indeksu danej iteracji(wiersza) znajduje się już jako key w dict
        # jeżeli tak to dodaje do wskazanego key, value którym jest iloczyn indeksu quantity oraz unit_price
        for row in rows:
            if row[CHOICES[sort_by]] in report:  # Jeżeli indeks danej transakcji znajduje się w category to wykonuje:
                report['{}'.format(row[CHOICES[sort_by]])] += row[CHOICES['quantity']] * row[CHOICES['unit_price']]
            else:
                report['{}'.format(row[CHOICES[sort_by]])] = 0
                report['{}'.format(row[CHOICES[sort_by]])] += row[CHOICES['quantity']] * row[CHOICES['unit_price']]

    else:
        # Jeżeli nie ma argumentu opcjonalnego sort_by to funkcja wykonuje iteracje poprzez wszystkie elementy rows,
        # jeżeli obiekt type datetime przeparsowany do str danej iteracji(wiersza) znajduje się już w słowniku report
        # jako key to, funkcja dodaje do danego key, value którym jest iloczyn indeksu quantity oraz unit_price
        for row in rows:
            if str(row[CHOICES['transaction_time']]) in report:
                report['{}'.format(row[CHOICES['transaction_time']])] += row[CHOICES['quantity']] \
                                                                         * row[CHOICES['unit_price']]
            else:
                report['{}'.format(row[CHOICES['transaction_time']])] = 0
                report['{}'.format(row[CHOICES['transaction_time']])] += row[CHOICES['quantity']] \
                                                                         * row[CHOICES['unit_price']]


    # Poniższa iteracja zamienia value na liczbę posiadającą tylko dwa miejsca po przecinku
    for k, v in report.items():
        report[k] = round(v, 2)


    return report  # Zwraca wartości ze zmiennych zaokrąglone do 2 miejsc
