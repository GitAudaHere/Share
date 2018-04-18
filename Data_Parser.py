#! /usr/bin/python3

import csv
import matplotlib.pyplot as plt

with open('/home/cheney/Desktop/GDPData(1).csv', 'r') as csv_file:
    values = []
    csv_reader = csv.reader(csv_file)
    years = list(map(int, list(next(csv_reader))[5:43]))
    print(years)
    for line in csv_reader:
        values.append(line[5:43])

    for col in range(len(values)):
        for row in range(len(values[col])):
            value = values[col][row]
            if value == "n/a":
                values[col][row] = ''
            else:
                values[col][row] = float(value)

    rates = []
    for col in range(len(values)):
        single_row = []
        for row in range(1, len(values[col])):
            last_value = values[col][row - 1]
            value = values[col][row]
            if last_value != '':
                single_row.append(round(value - last_value, 4))
            else:
                single_row.append('')
        rates.append(single_row)
    print("rates:")
    print(rates)

    # In the values list, split it into two lists for the two different datasets.
    # one for GDP and the other for per capita
