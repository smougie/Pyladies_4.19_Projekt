from data_loading import open_filename, bestseller, write_result
from date_filters import filter_rows_by_date, filter_rows_by_day, filter_rows_by_days
from filter_by import calculate_total_revenue
from helper_functions import create_date
import matplotlib.pyplot as plt

# Ścieżka pliku z danymi, który będziemy otwierać
filename = 'szwagropol_data/transactions.txt'

# Dict w którym każda liczba posiada określony indeks transakcji
CHOICES = {
    'transaction_time' : 0,
    'customer' : 1,
    'product_name' : 2,
    'category_name' : 3,
    'quantity' : 4,
    'unit_price' : 5,
}

#Zapisujemy do zmiennej rows oraz column_names sformatowane dane z modułu open_filename
rows, column_names = open_filename(filename)
# print([print(row) for row in bestseller(rows)])

# Zapisujemy do zmiennych wartości z funckji transaction_value tj.
# total_revenue - ogólny przychód, all_transaction_value_list - lista wartości każdego zakupu
report = calculate_total_revenue(rows, CHOICES, 'category_name')
for k, v in report.items():
    print(k, v)
print(report)

# W zmiennej second_april zapisujemy zwrócone przez funckję filter_date(), kolumny które odpowidają dacie filtracji
# Funkcja filter_date przyjmuje argumenty niezbędne do utowrzenia daty oraz argument rows w którym znajdują się
# wiersze po których będziemy wykonywać iterację celem odfiltrowania odpowiednich dni
second_april = create_date(2018, 4, 2)
second_april = filter_rows_by_day(rows, second_april)
# [print(row) for row in second_april]

# Obliczenie dochodu oraz wyświetlenie transakcji z danej daty przy użyciu funkcji transaction_value()
report_second_april = calculate_total_revenue(second_april, CHOICES)
print(report_second_april)
# print(transactions_second_april)

# Utworzenie listy 5 najlepiej sprzedających się produktów z przekazanej do funkcji listy transakcji
# bestseller_second_april = bestseller(report)
# [print(row) for row in bestseller_second_april]

# Filtrowanie od dnia do dnia
start_date = create_date(2018, 4, 2)
finish_date = create_date(2018, 4, 6)
# start_finish_date_rows = filter_rows_by_date(start_date, finish_date, rows)
# [print(row) for row in star_finish_date_rows]

# Utarg z pierwszego tygodnia kwietnia
# first_week_april, transactions_first_week_april = calculate_total_revenue(start_finish_date_rows)
# print([print(row) for row in transactions_first_week_april])
# print('Utarg z pierwszego tygodnia kwietnia wynosi {}zł'.format(first_week_april))

# Zapisanie utargu z pierwszego tygodnia kwietnia
# write_result(transactions_first_week_april)

# Wizualizacja danych
# plt.plot(transactions_first_week_april)
# plt.ylabel('Kwota transakcji w zł')
# plt.bar(list(range(0, len(transactions_first_week_april))), transactions_first_week_april)
# plt.xticks(list(range(0, len(transactions_first_week_april))), range(0, len(transactions_first_week_april)))
# plt.show()


third_april = create_date(2018, 4, 3)
fourth_april = create_date(2018, 4, 4)
fifth_april = create_date(2018, 4, 5)
three_days_april = filter_rows_by_days(rows, third_april, fourth_april, fifth_april)
# print([print(item) for item in three_days_april['2018-04-03']])

