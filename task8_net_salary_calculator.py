

HOUSE_ALLOWANCE = 6500
MEDICAL_ALLOWANCE = 5500

# a. Capture employee details
payroll_number = input("Enter payroll number: ")
name = input("Enter employee name: ")
gender = input("Enter gender: ")
department = input("Enter department: ")
basic_salary = float(input("Enter basic salary: "))

# b. Calculate gross pay
gross_pay = basic_salary + HOUSE_ALLOWANCE + MEDICAL_ALLOWANCE

# c. Calculate PAYE based on gross pay bracket
if gross_pay <= 15000:
    paye_rate = 0.00
elif gross_pay <= 30000:
    paye_rate = 0.04
elif gross_pay <= 50000:
    paye_rate = 0.05
else:
    paye_rate = 0.06

paye = gross_pay * paye_rate

# d. Calculate NHIF and NSSF
nhif = gross_pay * 0.02
nssf = basic_salary * 0.03

# e. Total deductions and net pay
total_deductions = paye + nhif + nssf
net_pay = gross_pay - total_deductions

# f. Display formatted output
print("\n" + "=" * 40)
print("        EMPLOYEE SALARY REPORT")
print("=" * 40)
print(f"Payroll Number : {payroll_number}")
print(f"Name           : {name}")
print(f"Gender         : {gender}")
print(f"Department     : {department}")
print("-" * 40)
print(f"Basic Salary       : Ksh {basic_salary:,.2f}")
print(f"House Allowance    : Ksh {HOUSE_ALLOWANCE:,.2f}")
print(f"Medical Allowance  : Ksh {MEDICAL_ALLOWANCE:,.2f}")
print(f"Gross Pay          : Ksh {gross_pay:,.2f}")
print("-" * 40)
print(f"PAYE ({paye_rate * 100:.0f}%)          : Ksh {paye:,.2f}")
print(f"NHIF (2% of gross) : Ksh {nhif:,.2f}")
print(f"NSSF (3% of basic) : Ksh {nssf:,.2f}")
print(f"Total Deductions   : Ksh {total_deductions:,.2f}")
print("-" * 40)
print(f"NET PAY            : Ksh {net_pay:,.2f}")
print("=" * 40)