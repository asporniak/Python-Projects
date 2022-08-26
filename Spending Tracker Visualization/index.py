import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

user_amounts = []
maxlengthamounts = 10
while len(user_amounts) < maxlengthamounts:
    monthspending = input("Please enter your monthly amount of spending. Ensure you hit enter after each month for the values to be recorded. Enter amount: ")
    user_amounts.append(monthspending)

plt.plot(months, user_amounts, color = "blue", marker = "o")
plt.title("Monthly Spending Graph")
plt.xlabel("Months")
plt.ylabel("Dollar Amount")
plt.legend(user_amounts)
plt.show()