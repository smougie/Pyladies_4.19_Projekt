def read_file():
    filename = 'szwagropol_data/transactions.txt'

    with open(filename, encoding='utf-8') as f_obj:
        rows = []
        for line in f_obj:
            current_row = line.strip().split(';')
            rows.append(current_row)

        for i in range(5):
            print(rows[i])
read_file()