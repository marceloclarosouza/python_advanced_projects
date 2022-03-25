
from flat import Bill, Flatmate
from reports import PdfReport


amount = float(input("Enter the bill amount: \n"))
period = input("Enter the period (eg. December 2022): \n")
name1 = input("What is your name? \n")
days_in_house1 = int(input(f"How many days did {name1} stay in the house during this period? \n"))
name2 = input("What is the other name? \n")
days_in_house2 = int(input(f"How many days did {name2} stay in the house during this period? \n"))


the_bill = Bill(amount, period)
flatmate1 = Flatmate(name1, days_in_house1)
flatmate2 = Flatmate(name2, days_in_house2)

print(f"{flatmate1.name} pays: ", flatmate1.pays(the_bill, flatmate2))
print(f"{flatmate2.name} pays: ", flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(filename=f"{the_bill.period}.pdf")
pdf_report.generate(flatmate1, flatmate2, the_bill)
