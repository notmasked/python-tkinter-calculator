import pygubu
import tkinter as tk
import pathlib

PROJECT_PATH = pathlib.Path(__file__).parent
UI_PATH = PROJECT_PATH / "ui.ui"

class Calculator:
    def __init__(self):
        self.builder = builder = pygubu.Builder()
        builder.add_resource_path(PROJECT_PATH)
        builder.add_resource_path(PROJECT_PATH / "assets")
        builder.add_from_file(UI_PATH)
        self.mainwindow = builder.get_object("window")
        builder.connect_callbacks(self)
        self.display = builder.get_object("message1")
        self.error_display = builder.get_object("error_msg")
        self.operation = ""
        self.waiting_for_result = False
        self.just_evaluated = False

    def run(self):
        self.mainwindow.mainloop()

    def append_digit(self, digit):
        if self.check_char_limit():
            return
        if self.just_evaluated:
            self.operation = ""
            self.just_evaluated = False
        self.operation += digit
        self.display.config(text=self.operation)

    def button1(self):
        self.append_digit("1")

    def button2(self):
        self.append_digit("2")

    def button3(self):
        self.append_digit("3")

    def button4(self):
        self.append_digit("4")

    def button5(self):
        self.append_digit("5")

    def button6(self):
        self.append_digit("6")

    def button7(self):
        self.append_digit("7")

    def button8(self):
        self.append_digit("8")

    def button9(self):
        self.append_digit("9")

    def button0(self):
        self.append_digit("0")

    def pnt(self):
        if self.check_char_limit() or self.check_point():
            pass
        else:
            if self.just_evaluated:
                self.operation = ""
                self.just_evaluated = False
            self.operation += "."
            self.display.config(text=self.operation)

    def check_point(self):
        string = self.operation
        string = string.replace(" ","")
        operator = None
        operator_list = ["+", "-", "*", "÷"]
        for x in string:
            if x in operator_list:
                operator = x
        string = string.split(operator)
        try:
            if "." in string[0] or "." in string[1]:
                return True
            elif string[1] == "":
                return True
            else:
                return False
        except IndexError:
            if "." in string[0]:
                return True
            elif string[0] == "":
                return True
            else:
                return False

    def delt(self):
        self.check_char_limit()
        if len(self.operation) >= 3 and self.operation[-1] == " ":
            self.operation = self.operation[:-3]
            self.display.config(text=self.operation)
        elif self.operation == "":
            pass
        else:
            temp = self.operation
            self.operation = temp[:-1]
            self.display.config(text=self.operation)

    def clr(self):
        self.check_char_limit()
        self.operation = ""
        self.just_evaluated = False
        self.display.config(text=self.operation)

    def add(self):
        if self.check_char_limit():
            pass
        else:
            self.check_operator()
            if self.operation == "" or self.waiting_for_result:
                pass
            else:
                self.waiting_for_result = True
                self.just_evaluated = False
                self.operation += " + "
                self.display.config(text=self.operation)

    def sub(self):
        if self.check_char_limit():
            pass
        else:
            self.check_operator()
            if self.operation == "" or self.waiting_for_result:
                pass
            else:
                self.waiting_for_result = True
                self.just_evaluated = False
                self.operation += " - "
                self.display.config(text=self.operation)

    def multiply(self):
        if self.check_char_limit():
            pass
        else:
            self.check_operator()
            if self.operation == "" or self.waiting_for_result:
                pass
            else:
                self.waiting_for_result = True
                self.just_evaluated = False
                self.operation += " * "
                self.display.config(text=self.operation)

    def div(self):
        if self.check_char_limit():
            pass
        else:
            self.check_operator()
            if self.operation == "" or self.waiting_for_result:
                pass
            else:
                self.waiting_for_result = True
                self.just_evaluated = False
                self.operation += " ÷ "
                self.display.config(text=self.operation)

    def check_operator(self):
        operators = ["+", "-", "*", "÷"]
        for x in self.operation:
            if x in operators:
                self.waiting_for_result = True
                return
            else:
                self.waiting_for_result = False

    def equals(self):
        string = self.operation.replace(" ","")
        operator = None
        operator_list = ["+", "-", "*", "÷"]
        for x in string:
            if x in operator_list:
                operator = x
        if operator is None:
            return

        string = string.split(operator)
        if len(string) != 2 or "" in string:
            self.error_display.config(text="Incomplete expression")
            return

        try:
            string = list(map(int, string))
        except ValueError:
            try:
                string = list(map(float, string))
            except ValueError:
                self.error_display.config(text="Invalid input")
                return

        match operator:
            case "+":
                self.operation = str(string[0] + string[1])
            case "-":
                self.operation = str(string[0] - string[1])
            case "*":
                self.operation = str(string[0] * string[1])
            case "÷":
                try:
                    self.operation = f"{float(string[0]) / float(string[1]):.2f}"
                except ZeroDivisionError:
                    self.error_display.config(text="Zero Division isn't possible")
                    return

        self.waiting_for_result = False
        self.just_evaluated = True
        self.display.config(text=self.operation)

    def check_char_limit(self):
        if len(self.operation) == 32:
            self.error_display.config(text="Maximum Characters")
            return True
        else:
            self.error_display.config(text="")

if __name__ == "__main__":
    app = Calculator()
    app.run()