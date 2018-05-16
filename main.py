from data_loading import open_filename, transaction_value, filter_rows_by_date, bestseller
from helper_functions import parse_date_from_string, create_date
import datetime


# Ścieżka pliku z danymi, który będziemy otwierać
filename = 'szwagropol_data/transactions.txt'

#Zapisujemy do zmiennej rows oraz column_names sformatowane dane z modułu open_filename
rows, column_names = open_filename(filename)

# Zapisujemy do zmiennych wartości z funckji transaction_value tj.
# total_revenue - ogólny przychód, all_transaction_value_list - lista wartości każdego zakupu
total_revenue, transactions_value_list = transaction_value(rows)


# W zmiennej second_april zapisujemy zwrócone przez funckję filter_date(), kolumny które odpowidają dacie filtracji
# Funkcja filter_date przyjmuje argumenty niezbędne do utowrzenia daty oraz argument rows w którym znajdują się
# wiersze po których będziemy wykonywać iterację celem odfiltrowania odpowiednich dni
second_april = filter_rows_by_date(2018, 4, 2, rows)
[print(row) for row in second_april]



# Obliczenie dochodu oraz wyświetlenie transakcji z danej daty przy użyciu funkcji transaction_value()
second_april_revenue, transactions_second_april = transaction_value(second_april)
print(second_april_revenue)
print(transactions_second_april)

# Utworzenie listy 5 najlepiej sprzedających się produktów z przekazanej do funkcji listy transakcji
bestseller_second_april = bestseller(second_april)
[print(row) for row in bestseller_second_april]



