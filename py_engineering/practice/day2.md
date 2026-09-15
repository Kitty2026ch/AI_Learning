# Day1&Day 2
## Day1

###Reading Plan & Completed Status
link: Object-Oriented Programming (OOP) in Python 3
<https://realpython.com/python3-object-oriented-programming/>
-[x]What Is Object-Oriented Programming?
-[x]How to Define a Class
-[x]How to Instantiate an Object
-[x]How to Define Instance Attributes
-[x]How to Define Instance Methods

###Exercise
-[x]Create a plain Employee class (not a dataclass yet) with __init__ taking name, department, salary
-[x]Add a method give_raise(self, amount) that increases salary
-[x]Create 3 employee instances, print their names and salaries, give one a raise, print again

###Coding
```
class Employee:
    def __init__(self,name,department,salary):
        self.name=name
        self.department=department
        self.salary=salary

    def give_raise(self,amount):  # error, add self
        self.salary+=amount
        return self.salary

    def __repr__(self):
        return f"Employee({self.name},{self.salary})"  # f lost

kitty=Employee('Kitty','HR',22000)
once=Employee('Once','IT',50000)
emma=Employee('Emma','Retail',30000)
kitty.give_raise(8000)
once.give_raise(10000)
emma.give_raise(9000)

print(f"{kitty},{once},{emma}")
```

###Review
error:def give_raise(amount):
correct: def give_raise(self,amount):

##Day2

###Reading
Link:
Data Classes in Python (Guide)https://realpython.com/python-data-classes</>
-[x] "Data Classes in Python 3" 
+ read: "Basic Data Classes", "Default Values", "Type Hints" section intro only (don't go deep on typing yet, that's Day 3)

Python's property(): Add Managed Attributes to Your Classes
<https://realpython.com/python-property/>
-[x] "Python's property(): Add Managed Attributes to Your Classes" 
+ read only: "Getting Started With Python's property()", "Providing Read-Only Attributes" (that's the @property pattern you need). Skip everything about setters/deleters for now

###Excecise

-[x]Rewrite yesterday's Employee as a @dataclass with fields: name, department, salary, start_date
-[x]Add a @property called tenure_years that computes years since start_date
-[x]Add a custom __repr__ and __eq__ (dataclasses give you these for free — but write one manually too, so you understand what's happening underneath)
-[x]Create a Department class that holds a list of Employee objects

###Coding
```
from dataclasses import dataclass,field
from datetime import date
from dateutil.relativedelta import relativedelta

@dataclass   #__init__,__repr__,__eq__
class Employee:
    name:str
    dept:str
    salary:float
    start_date:date

    @property
    def tenure_years(self)->float:
        end_date=date.today()
        if self.start_date>=end_date:
            return 0.0
        rd=relativedelta(end_date,self.start_date)
        tenure_years=round(rd.years+rd.months/12+rd.days/365.25,2)
        return tenure_years
    
    def give_raise(self,amount:float) ->float:
        self.salary+=amount
        return self.salary
   
    def __repr__(self)->str:
        return (f'{self.__class__.__name__}'  #此处不能加逗号，加逗号会变成元组
                f'({self.name!r},{self.dept!r},{self.tenure_years},{self.salary})')

    def __eq__(self,other:object)->bool:
        if not isinstance(other,Employee):
            return NotImplemented
        return (self.name,self.dept,self.salary,self.start_date)==(other.name,other.dept,other.salary,other.start_date)

@dataclass
class Department:
    employees:List[Employee]=field(default_factory=list)

    def add_employees(self,emp:Employee) ->None:
        self.employees.append(emp)

    def total_salary(self)->float:
        return sum(emp.salary for emp in self.employees)
    
    def __str__(self) ->str:
        return f"{self.__class__.__name__}{self.employees!r}"

```

###Review
- @dataclass 自动生成 __init__/__repr__/__eq__，但手写一遍理解更深
- __repr__ 必须返回 str，多个 f-string 相邻拼接不能有逗号, f"{self.__class__.__.name__}" 和 f"({self.name}{self.dept})"之间不能有逗号，self.attribute 的类别是str的，用{self.name!r},显示结果出来"kitty"--带引号
- @property是无参函数，不能传参数。如 @property  def tenure_year(self)-> float: , 不能写 def tenure_year(self,end_date)