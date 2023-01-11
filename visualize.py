import csv
import re
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
from collections import Counter
file_name = ""
names = []
with open(file_name, 'r') as file:
    file_obj = csv.reader(file)
    for i in file_obj:
        name = i[0].split(' ')
        if name[0] not in names:
            names.append(name[0].lower())

names.sort()
counts = Counter(names)
name_nums = []
for k, v in counts.items():
    name_nums.append(v)
