annual_salary = float(input("Enter your annual salary: "))
portion_saved = float(input("Enter the percent that you save from your annual salary, as a decimal: ")) * annual_salary
total_cost = float(input("Enter the cost of your dream home: "))

monthly_salary = (annual_salary - portion_saved) / 12
portion_down_payment = total_cost * 0.25
current_savings = 0
r = 0.04
investment = current_savings * (r / 12)
n = 0
saved = True

while saved:
    current_savings += monthly_salary + investment
    n += 1
    if current_savings >= total_cost :
        saved = False

print("Number of months = ", n)