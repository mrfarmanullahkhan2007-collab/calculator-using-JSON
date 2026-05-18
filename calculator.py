import json

class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        pass
    def addition(self):
        return self.a + self.b
    def subtraction(self):
        return self.a - self.b
    def multiplication(self):
        return self.a * self.b
    def division(self):
        return self.a / self.b
    def obj_to_dict(self):
        return {
            "addtion" : self.a + self.b,
            "subtraction" : self.a - self.b,
            "multiplication" : self.a * self.b,
            "division" : self.a / self.b
        }
    def write(self):
        with open ("cal.txt", "w") as file:
            json.dump(self.obj_to_dict(), file, indent=4)
a = int (input("a : "))
b = int (input ("b : "))
cal = Calculator(a, b)
cal.addition()
cal.subtraction()
cal.multiplication()
cal.division()
cal.obj_to_dict()
cal.write()
