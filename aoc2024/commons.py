def load_data(day_number: str, prefix: str = ''):
    with open('../data/{prefix}input_{day_number:0>2}.txt'.format(day_number=day_number, prefix=prefix), 'r') as file:
        return file.read()
