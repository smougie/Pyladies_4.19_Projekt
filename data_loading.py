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


def calculate_total_revenue(rows, *category):
    """Funckja odpowiedzialna za liczenie sumy transakcji"""

    QUANTITY_INDEX = -2  # Indeks odpowiadający ilości produktów
    VALUE_INDEX = -1  # Indeks odpowiadający wartości
    CATEGORY_INDEX = -3  # Indeks odpowiadający categorii produktu
    transaction_value = 0  # Wartość całkowita transakcji
    transaction_value_list = []  # Lista w której będziemy przechowywać sumę ilości produktu * jego wartość

    # Pętla która dodaje do transaction_value oraz transaction list, przemnożoną ilość produtków razy jego wartość
    # Zaokrąglamy także transaction_value oraz wartości dodawane do transaction_value_list
    for lane in rows:
        if category:  # Jeżeli wystąpi argument pozycyjny category to:
            if lane[CATEGORY_INDEX] in category:  # Jeżeli indeks danej transakcji znajduje się w category to wykonuje:
                transaction_value += lane[QUANTITY_INDEX] * lane[VALUE_INDEX]
                transaction_value_list.append(round(lane[QUANTITY_INDEX] * lane[VALUE_INDEX], 2))
        else:  # Jeżeli nie podamy argumentu pozycyjnego to wykonuje:
            transaction_value += lane[QUANTITY_INDEX] * lane[VALUE_INDEX]
            transaction_value_list.append(round(lane[QUANTITY_INDEX] * lane[VALUE_INDEX], 2))
    return round(transaction_value, 2), transaction_value_list  # Zwraca wartości ze zmiennych zaokrąglone do 2 miejsc


def filter_rows_by_day(year, month, day, rows):
    """Funkcja która przyjmuje 4 parametry, pierwsze 3 służą do utworzenia daty, następny argument to kolumny na których
    wykonamy filtrowanie, zwraca odfitrowane kolumny"""

    date = create_date(year, month, day)  # tworzymy datę przy użyciu funkcji create_date()
    filtered_rows = []  # pusta lista do której będziemy dodawać kolumny odpowiadające filtrowanej dacie
    for row in rows:
        if row[0] == date:
            filtered_rows.append(row)
    return filtered_rows


def filter_rows_by_date(start_date, finish_date, rows):
    filtered_rows = []
    for row in rows:
        if row[0] >= start_date and row[0] <= finish_date:
            filtered_rows.append(row)
    return filtered_rows

def write_result(result):
    filename = 'szwagropol_data/results.txt'
    with open(filename, 'w') as f_obj:
        for row in result:
            f_obj.write(str(row) + '\n')


def bestseller(rows):
    sorted_rows = sorted(rows, key=itemgetter(-2))
    bestseller_list = sorted_rows

    return bestseller_list[:-6:-1]  # ostatnie 5 indeksów, odwrócone