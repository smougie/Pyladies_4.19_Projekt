from collections import OrderedDict


def calculate_total_revenue(rows, CHOICES, sort_by=None):
    """Funckja odpowiedzialna za obliczenie wartości produktu razy jego ilość z przekazanych do funkcji danych.
       Funkcja przyjmuje argument rows w którym przekazujemy dane na których będzie wykonywać obliczenia,
       argumnet CHOICES, w którym znajdują się zdefiniowane indeksy wierszy, oraz argument opcjonalny sort_by,
       który wskazuje wg. jakiego indeksu wierszu mamy przefiltrować dane - np. 'product_name"""
    CHOICES = CHOICES
    key_index = CHOICES['transaction_time']
    report = OrderedDict()

    if sort_by:
        # Jeżeli wystąpi argument opcjonalny sort_by, funkcja zmienia wartość key_index na odpowiadającą sort_by
        key_index = CHOICES[sort_by]

    for row in rows:
        # Jeżeli nie ma argumentu opcjonalnego sort_by to funkcja wykonuje iteracje poprzez wszystkie elementy rows,
        # jeżeli obiekt type datetime przeparsowany do str danej iteracji(wiersza) znajduje się już w słowniku report
        # jako key to, funkcja dodaje do danego key, value którym jest iloczyn indeksu quantity oraz unit_price

        multiply_value = row[CHOICES['quantity']] * row[CHOICES['unit_price']]
        if row[key_index] in report:  # Jeżeli indeks danej transakcji znajduje się w category to wykonuje:
            report['{}'.format(row[key_index])] += multiply_value
        else:
            report['{}'.format(row[key_index])] = multiply_value

    # else:




    # Poniższa iteracja zamienia value na liczbę posiadającą tylko dwa miejsca po przecinku
    for k, v in report.items():
        report[k] = round(v, 2)


    return report  # Zwraca wartości ze zmiennych zaokrąglone do 2 miejsc
