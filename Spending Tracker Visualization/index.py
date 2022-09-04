import matplotlib.pyplot as plt
import numpy as np


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
avg_amounts = [500, 250, 300, 400, 600, 800, 850, 700, 350, 950, 650, 740]

user_amounts = []
maxlengthamounts = 12
while len(user_amounts) < maxlengthamounts:
    monthspending = input("Please enter your monthly spending for " + months[len(user_amounts)] + ":")
    user_amounts.append(monthspending)

user_amounts = [int(item) for item in user_amounts]

plt.plot(months, user_amounts, linewidth = 2, marker = "o")
plt.title("Personal Monthly Spending Graph")
plt.xlabel("Months")
plt.ylabel("Dollar Amount")

personal_mean = np.mean(user_amounts)
personal_min = np.min(user_amounts)
personal_max = np.max(user_amounts)

print("Your Average Monthly Spending amount for the year is: $" + str(personal_mean))
print("Your Lowest Monthly Spending amount for the year is: $" + str(personal_min))
print("Your Highest Monthly Spending amount for the year is: $" + str(personal_max))

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

personal_values = create_x(2, 0.8, 1, 12)
avg_values = create_x(2, 0.8, 2, 12)

middle_x = [(a + b) / 2.0 for a, b in zip(personal_values, avg_values)]

plt.figure(figsize=(10, 8))
ax = plt.subplot()
plt.bar(personal_values, user_amounts)
plt.bar(avg_values, avg_amounts)
plt.title("Personal Spending Vs Average Canadian Spending")
plt.xlabel("Months")
plt.ylabel("Dollar Amount")
ax.set_xticks(middle_x)
ax.set_xticklabels(months)
plt.legend(["Your Monthly Spending", "Average Canadian Monthly Spending"])
plt.show()

