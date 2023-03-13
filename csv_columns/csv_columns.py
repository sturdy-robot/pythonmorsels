from itertools import zip_longest
import csv


def csv_columns(file, headers=None, missing=None):
    reader = csv.reader(file)
    dictionary = {}
    columns = list(zip_longest(*reader, fillvalue=missing))
    if headers is None:
        headers = [col[0] for col in columns]

    for column, header in zip_longest(columns, headers):
        col = [item for item in column if item != header]
        dictionary[header] = col

    return dictionary
