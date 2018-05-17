from helper_functions import parse_date_from_string, create_date
from operator import itemgetter


def open_filename(filename):
    """Funkcja odpowiedzialna za wczytanie pliku"""

    with open(filename, encoding='utf-8') as f_obj:
        # Tworzymy pustą listę dla przetworzonych danych
        rows = []
        # Zmienna w której będziemy przechowywać nazwy kolumn
        columns_names = f_obj.readline().strip().split(';')  # Wczytujemy pierwszą linę, usuwając białe znaki oraz ';'

        # Iterujemy przez każdą linię w otwartym wcześniej pliku
        for line in f_obj:
            current_row = line.strip().split(';')  # Usuwamy białe znaki oraz ';'
            current_row[0] = parse_date_from_string(current_row[0])  # Na indeksie 0 wykonujemy parsowanie daty
            try:  # Umieszamy w try except warunek, jeżeli ostatni indeks wywoła Value Error podczas parsowania to
                  # pomijamy daną linię, w innym wypadku wykonujemy parsowanie stringa na float
                current_row[-1] = float(current_row[-1])  # Zmieniamy string na float
            except ValueError:
                continue
            current_row[-2] = int(current_row[-2])  # Zamieniamy przeostatni indeks który jest str na int
            rows.append(current_row)  # Dodajemy edytowaną linię do nowo utworzonej listy rows

        return rows, columns_names  # funkcja zwraca nazwę kolumn oraz ich wartość w dwóch różnych zmiennych


def write_result(result):
    filename = 'szwagropol_data/results.txt'
    with open(filename, 'w') as f_obj:
        for row in result:
            f_obj.write(str(row) + '\n')


def bestseller(rows):
    print(rows)
    sorted_rows = sorted(rows, key=itemgetter(-2))
    bestseller_list = sorted_rows

    return bestseller_list[:-6:-1]  # ostatnie 5 indeksów, odwrócone