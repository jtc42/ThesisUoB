import numpy as np
import csv
import codecs
from datetime import datetime

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

filename = "../wordcount.txt"

dates = []
words = []

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    for row in csv_reader:
        print(row)
        try:
            words.append(int(row[1]))
            dates.append(datetime.strptime(row[0], '%a, %d %b %Y %H:%M:%S %z'))
        except ValueError:
            print("Skipping broken wordcount results")
        

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())

plt.plot(dates, words)
plt.gcf().autofmt_xdate()

plt.ylabel("Words")
plt.title("Thesis word count from git history")

plt.show()

print("END")