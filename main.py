from data_loading import open_filename, filter_rows_by_day, bestseller, filter_rows_by_date, \
    calculate_total_revenue, write_result
from helper_functions import create_date
import matplotlib.pyplot as plt

# Ścieżka pliku z danymi, który będziemy otwierać
filename = 'szwagropol_data/transactions.txt'

#Zapisujemy do zmiennej rows oraz column_names sformatowane dane z modułu open_filename
rows, column_names = open_filename(filename)

# Zapisujemy do zmiennych wartości z funckji transaction_value tj.
# total_revenue - ogólny przychód, all_transaction_value_list - lista wartości każdego zakupu
total_revenue, transactions_value_list = calculate_total_revenue(rows)

# W zmiennej second_april zapisujemy zwrócone przez funckję filter_date(), kolumny które odpowidają dacie filtracji
# Funkcja filter_date przyjmuje argumenty niezbędne do utowrzenia daty oraz argument rows w którym znajdują się
# wiersze po których będziemy wykonywać iterację celem odfiltrowania odpowiednich dni
second_april = filter_rows_by_day(2018, 4, 2, rows)
# [print(row) for row in second_april]

# Obliczenie dochodu oraz wyświetlenie transakcji z danej daty przy użyciu funkcji transaction_value()
second_april_revenue, transactions_second_april = calculate_total_revenue(second_april)
# print(second_april_revenue)
# print(transactions_second_april)

# Utworzenie listy 5 najlepiej sprzedających się produktów z przekazanej do funkcji listy transakcji
bestseller_second_april = bestseller(second_april)
[print(row) for row in bestseller_second_april]

# Filtrowanie od dnia do dnia
start_date = create_date(2018, 4, 2)
finish_date = create_date(2018, 4, 6)
star_finish_date_rows = filter_rows_by_date(start_date, finish_date, rows)
# [print(row) for row in star_finish_date_rows]

# Utarg z pierwszego tygodnia kwietnia
first_week_april, transactions_first_week_april = calculate_total_revenue(star_finish_date_rows)
# print([print(row) for row in transactions_first_week_april])
print('Utarg z pierwszego tygodnia kwietnia wynosi {}zł'.format(first_week_april))

# Zapisanie utargu z pierwszego tygodnia kwietnia
write_result(transactions_first_week_april)

# Wizualizacja danych
# plt.plot(transactions_first_week_april)
plt.ylabel('Kwota transakcji w zł')
plt.bar(list(range(0, len(transactions_first_week_april))), transactions_first_week_april)
plt.xticks(list(range(0, len(transactions_first_week_april))), range(0, len(transactions_first_week_april)))
plt.show()