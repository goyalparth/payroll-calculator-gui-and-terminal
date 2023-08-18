import tkinter

class myGui():
    def __init__(self):

        self.main_window = tkinter.Tk()
        self.main_window.title('Payroll Calculator')
        self.name_frame = tkinter.Frame()
        self.hours_frame = tkinter.Frame()
        self.pay_frame = tkinter.Frame()
        self.tax_rate_frame = tkinter.Frame()
        self.medicare_levy_frame = tkinter.Frame()
        self.button_frame = tkinter.Frame()
        self.result_frame = tkinter.Frame()
        

        name_label = tkinter.Label(self.name_frame, text = "Enter employee's name: ")
        self.name_entry = tkinter.Entry(self.name_frame, bg = 'light blue', bd = 2 ,width = '10')
        name_label.pack(side = 'left', padx = 45)
        self.name_entry.pack(side = 'left')

        hours_label = tkinter.Label(self.hours_frame, text = "Enter number of hours worked in a week: ")
        self.hours_entry = tkinter.Entry(self.hours_frame, bg = 'light blue', bd = 2 ,width = '10')
        hours_label.pack(side = 'left')
        self.hours_entry.pack(side = 'left')

        pay_label = tkinter.Label(self.pay_frame, text = "Enter hourly pay rate: ")
        self.pay_entry = tkinter.Entry(self.pay_frame, bg = 'light blue', bd = 2 ,width = '10')
        pay_label.pack(side = 'left', padx = 52)
        self.pay_entry.pack(side = 'left')

        tax_rate_label = tkinter.Label(self.tax_rate_frame, text = "Enter ATO tax withholding rate: ")
        self.tax_rate_entry = tkinter.Entry(self.tax_rate_frame, bg = 'light blue', bd = 2 ,width = '10')
        tax_rate_label.pack(side = 'left', padx = 24)
        self.tax_rate_entry.pack(side = 'left')

        medicare_levy_label = tkinter.Label(self.medicare_levy_frame, text = "Enter Medicare Levy rate: ")
        self.medicare_levy_entry = tkinter.Entry(self.medicare_levy_frame, bg = 'light blue', bd = 2 ,width = '10')
        medicare_levy_label.pack(side = 'left', padx = 41)
        self.medicare_levy_entry.pack(side = 'left')
        
        calc_button = tkinter.Button(self.button_frame, text = 'Display Payroll', command = self.display)
        calc_button.pack(side = 'left')
        quit_button = tkinter.Button(self.button_frame, text='Quit', command=self.main_window.destroy)
        quit_button.pack(side='left')

        self.result_ta = tkinter.Text(self.result_frame, bg = 'light blue', height = 15, width = 40)
        self.result_ta.pack()
        
        self.name_frame.pack()
        self.hours_frame.pack()
        self.pay_frame.pack()
        self.tax_rate_frame.pack()
        self.medicare_levy_frame.pack()
        self.button_frame.pack()
        self.result_frame.pack()

        tkinter.mainloop()

    def display(self):
            
        name = (self.name_entry.get())
        hours = float(self.hours_entry.get())
        pay = float(self.pay_entry.get())
        tax_rate = float(self.tax_rate_entry.get())
        medicare_levy = float(self.medicare_levy_entry.get())

        gross_pay = (hours*pay)
        total_tax = (tax_rate)*gross_pay
        total_medicare = (medicare_levy)*gross_pay
        total_deduction = total_tax + total_medicare
        
        result1 = "Employee Name: " + str(name) + '\n'
        result2 = "Hours Worked: " + str(hours) + '\n'
        result3 = "Pay Rate: $"+  str(pay) + '\n'
        result4 = "Gross Pay: $" + str(gross_pay) + '\n'
        result5 = "Deductions: " + '\n'
        result6 = '\t' + "ATO tax (30.0%): $" + str(total_tax) + '\n'
        result7 = '\t' + "Medicare Levy (2.0%): $" + str(total_medicare) + '\n'
        result8 = '\t' + "Total Deduction: $" + str(total_deduction) + '\n'
        result9 = '\n' + "Net Pay: $" + str(gross_pay - total_deduction)

        self.result_ta.insert('1.0',result1)
        self.result_ta.insert('2.0',result2)
        self.result_ta.insert('3.0',result3)
        self.result_ta.insert('4.0',result4)
        self.result_ta.insert('5.0',result5)
        self.result_ta.insert('6.0',result6)
        self.result_ta.insert('7.0',result7)
        self.result_ta.insert('8.0',result8)
        self.result_ta.insert('9.0',result9)
        
my_gui = myGui()
