from collections import OrderedDict

from helper_functions import create_date


def filter_rows_by_day(rows, date):
    """Funkcja, która jako parametry przyjmuje zbiór wszystkich transakcji oraz datę której użyjemy do filtrowania"""

    filtered_rows = []  # pusta lista do której będziemy dodawać kolumny odpowiadające filtrowanej dacie
    for row in rows:
        if row[0] == date:
            filtered_rows.append(row)
    return filtered_rows

def filter_rows_by_days(rows, *days):
    '''Funkcja która przyjmuje zbiór wszystkich transakcji oraz nieokreśloną liczbę dni których użyjemy do
    filtrowania'''
    report = OrderedDict()
    for day in days[:]:
        report['{}'.format(day)] = []

    for row in rows:
        if row[0] in days:
            report['{}'.format(row[0])].append(row)
    return report


def filter_rows_by_date(rows, start_date, finish_date=None):
    """Funkcja ta filtruje dane z zmiennej rows przy użyciu argumentów start_date oraz fisnish_date(jeżeli podano)
    Jeżeli nie podano finish_date, funkcja zwraca ordered dict z jednym key którym jest start_date oraz value ,którymi
    są rows odpowiadające start_date, jeżeli podano finish date, funkcja tworzy dict którego keys są unikalne daty
    pobrane z indeksu każdej row - row[0]. Values odpowiadają wartości których data równa jest dict key.
    """
    report = OrderedDict()  # Tworzy pusty ordered dict

    if finish_date:  # jeżeli podano argument opcjonalny finish_date
        for row in rows:  # iteracja poprzez każdą linię rows
            if row[0] >= start_date and row[0] <= finish_date:  # jeżeli indeks odpowiedzialny za datę mieści się w
                                                                # podanym przedziale to wykonuje blok kodu
                if str(row[0]) in report:  # jeżeli data danej linii znajduje się już w słowniku
                    report['{}'.format(row[0])].append(row)  # funkcja dodaje do tej daty obecny wiersz jako value
                else:
                    # jeżeli nie ma takiej daty to tworzy key, którego value to obecny wiersz
                    report['{}'.format(row[0])] = []
                    report['{}'.format(row[0])].append(row)

    else:
        # jeżeli nie podano argumentu opcjonalnego finish_date, funkcja tworzy tworzy jeden key którym jest start_date
        # a następnie dodaje do tego key, value którymi są kolejne iterowane wiersze których data odpowaida podanej
        # w argumencie funckji start_date
        report['{}'.format(start_date)] = []
        for row in rows:
            if row[0] == start_date:
                report['{}'.format(start_date)].append(row)

    return report