import matplotlib.pyplot as plt
import numpy as np


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

user_amounts = []
maxlengthamounts = 12
while len(user_amounts) < maxlengthamounts:
    monthspending = input("Please enter your monthly spending for " + months[len(user_amounts)] + ":")
    user_amounts.append(monthspending)

user_amounts = np.array(user_amounts)

plt.plot(months, user_amounts, linewidth = 2, marker = "o")
plt.title("Monthly Spending Graph")
plt.xlabel("Months")
plt.ylabel("Dollar Amount")
plt.legend(user_amounts)
plt.show()