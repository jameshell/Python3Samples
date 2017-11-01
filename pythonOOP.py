#Python 3 - Object Oriented Programming.

class Employee:
    num_of_emps=0
    raise_amount = 1.94

    #Este viene siendo en constructor de la clase
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    #Esta es una forma de elevar la cantidad de empleados cada vez que se agregue uno
        Employee.num_of_emps+= 1

    def fullname(self):
        return '{} {}'.format(self.first,self.last)

    def apply_raise(self):
        self.pay = int(self.pay*self.raise_amount)

    #Si no quieres usar self, puedes usar class que se acerca más a los métodos de JAVA. La clase queda como el primer argumento.
    @classmethod
    def set_raise_amt(cls, amount):
        cls.set_raise_amt = amount

    #Este vendria siendo un constructor alternativo en caso de que se reciban empleados con String
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first,last,pay)

    #Estos métodos no operan ni en las instancias como self ni en las clases como cls
    @staticmethod
    def is_workday(day):
        if ((day.weekday()== 5) or (day.weekday() == 6)):
            return False
        return True

#Ejercicio de fechas
import datetime
my_date = datetime.date(2016, 7, 11)
print(Employee.is_workday(my_date))


#Una forma de realizar un setter
Employee.set_raise_amt(1.05)



emp_1 = Employee('Jaime','Alonso',98000)

#Ejercicio con string creando un nuevo empleado
emp_str_2 = 'Javier-Alonso-70000'
Employee.from_string(emp_str_2)

#Forma de cambiar el amount
Employee.raise_amount=2

print(emp_1.email)
print('Pay before the raise: '+str(emp_1.pay))
emp_1.apply_raise()
print('Pay after the raise: '+str(emp_1.pay))
print('Number of Employees: '+str(Employee.num_of_emps))

#print(emp_1.__dict__) Este método es del lenguaje como tal y te devuelve un arreglo en string de los componentes de la clase
#print('El primer empleado se llama '+emp_1.first+ ' y su paga es de '+str(emp_1.pay))