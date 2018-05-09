from data_loading import open_filename, transaction_value
from helper_functions import parse_date_from_string, create_date
import datetime


# Ścieżka pliku z danymi, który będziemy otwierać
filename = 'szwagropol_data/transactions.txt'

#Zapisujemy do zmiennej rows oraz column_names sformatowane dane z modułu open_filename
rows, column_names = open_filename(filename)

# Zapisujemy do zmiennych wartości z funckji transaction_value tj.
# total_revenue - ogólny przychód, all_transaction_value_list - lista wartości każdego zakupu
total_revenue, all_transaction_value_list = transaction_value(rows)


# Tu jestem!!! wyszukiwanie danych po dacie.
second_april = create_date(2018, 4, 2)

rows_filtered = []
for row in rows:
    if second_april == row[0]:
        rows_filtered.append(row)

second_april_revenue, all_transaction_second_april = transaction_value(rows_filtered)
print(second_april)

print(rows_filtered)