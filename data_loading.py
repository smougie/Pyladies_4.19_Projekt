from helper_functions import parse_date_from_string


def open_filename(filename):
    """Funkcja odpowiedzialna za wczytanie pliku"""
    filename = 'szwagropol_data/transactions.txt'

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

# Funckja odpowiedzialna za liczenie sumy transakcji
def transaction_value(rows):
    QUANTITY_INDEX = -2  # Indeks odpowiadający ilości produktów
    VALUE_INDEX = -1  # Indeks odpowiadający wartości
    transaction_value = 0  # Wartość całkowita transakcji
    all_transaction_value_list = []  # Lista w której będziemy przechowywać sumę ilości produktu * jego wartość
    # Pętla która dodaje do transaction_value oraz transaction list, przemnożoną ilość produtków razy jego wartość
    for lane in rows:
        transaction_value += lane[QUANTITY_INDEX] * lane[VALUE_INDEX]
        all_transaction_value_list.append(lane[QUANTITY_INDEX] * lane[VALUE_INDEX])
    return transaction_value, all_transaction_value_list