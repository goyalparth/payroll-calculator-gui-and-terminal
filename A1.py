name = input("Enter employee's name: ")
hours = float(input("Enter number of hours worked in a week: "))
pay = float(input("Enter hourly pay rate: "))
tax_rate = float(input("Enter ATO tax withholding rate: "))
medicare_levy = float(input("Enter Medicare Levy rate: "))

gross_pay = (hours*pay)
total_tax = (tax_rate)*gross_pay
total_medicare = (medicare_levy)*gross_pay
total_deduction = total_tax + total_medicare

print()
print("Employee Name:",name)
print("Hours Worked:", str(hours))
print("Pay Rate: $"+ str(pay))
print("Gross Pay: $" + str(gross_pay))
print("Deductions: ")
print('\t' + "ATO tax (30.0%): $" + str(total_tax))
print('\t' + "Medicare Levy (2.0%): $" + str(total_medicare))
print('\t' + "Total Deduction: $" + str(total_deduction))

print()
print("Net Pay: $" + str(gross_pay - total_deduction))
