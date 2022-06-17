from breezypythongui import EasyFrame
from tkinter.font import Font
#other imports
class Practice(EasyFrame):
#AppilcationName will change from project to project

#defintion of the __init__() method which is our class constructor

	def __init__(self):

		EasyFrame.__init__(self, title = "practice", background = "lightblue")
		self.setResizable(True)

		titleFont = Font(family = "Goergia", size = 24, weight = "bold")

		textLabel = self.addLabel(font = titleFont, text = "Salary Calculator", background = "lightblue", row = 0, column = 0, columnspan = 2, sticky = "NSEW")
		howage = self.addLabel(text = "Hourly Wage :", background = "lightblue", row = 1, column = 0)
		noworked = self.addLabel(text = "No. of Hours Worked :", background = "lightblue", row = 2, column = 0)
		self.but = self.addButton(text = "Compute", row = 3, column = 0, columnspan = 2, command = self.compute)
		emp = self.addLabel(text = "The employee's salary is :", background = "lightblue", row = 4, column = 0)
		self.wageField = self.addFloatField(value = 0.0, row = 1, column = 1)
		self.noField = self.addFloatField(value = 0.0, row = 2, column = 1)
		self.resultField = self.addFloatField(value = 0.0, row = 4, column = 1, precision = 2)
		self.but["background"] = "yellow"

	def compute(self):
		wage = self.wageField.getNumber()
		hours = self.noField.getNumber()
		salary = wage * hours 
		self.resultField.setNumber(salary)
def main():
	# instance an object from the class into mainloop
	Practice().mainloop()
#global call to trigger he main() method
main()		  