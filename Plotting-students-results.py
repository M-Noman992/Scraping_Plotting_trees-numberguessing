import numpy as np
import matplotlib.pyplot as plt

academic_years = [2015, 2016, 2017, 2018, 2019]

it_passed = [12, 28, 2, 8, 22]
ece_passed = [26, 6, 16, 5, 10]
cse_passed = [27, 3, 24, 25, 17]

bar_width = 0.2

r1 = np.arange(len(academic_years))
r2 = [x + bar_width for x in r1]
r3 = [x + bar_width for x in r2]

plt.xlabel('Branches')
plt.ylabel('Students Passed')

plt.bar(r1, it_passed, color='red', label="IT", width=bar_width)
plt.bar(r2, ece_passed, color='green', label="ECE", width=bar_width)
plt.bar(r3, cse_passed, color='blue', label="CSE", width=bar_width)

plt.xticks([r + bar_width for r in range(len(academic_years))], academic_years)
plt.legend()

plt.title("Students Passed in Different Branches Over the Years")
plt.tight_layout()
plt.show()