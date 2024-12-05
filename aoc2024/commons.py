def load_data(day_number: str):
    with open('../data/input-{:0>2}.txt'.format(day_number), 'r') as file:
        return file.read()
