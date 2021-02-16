## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):

    '''class Animal() - To handle the race and color of animal'''
    def __init__(self, race, color):
        ## class Animal has-a attribute named race
        self.race = race
        ## class Animal has-a attribute named color
        self.color = color

## Dog is-a Animal
class Dog(Animal):

    '''class Dog() - To handle the name, race and color of dog'''
    def __init__(self, name, race, color):
        ## Inheritance from class Aminal()
        super(Dog, self).__init__(race, color)
        ## class Dog has-a attribute named name 
        self.name = name

    ## class Dog has-a method named print_dog_data()
    def print_dog_data(self):
        print("Dog name: " + self.name)
        print("Race: " + self.race)
        print("Color: " + self.color)

## Cat is-a Animal
class Cat(Animal):

    '''class Cat() - To handle the name, race and color of cat'''
    def __init__(self, name, race, color):
        ## Inheritance from class Animal()
        super(Cat, self).__init__(race, color)
        ## class Cat has-a attribute named name 
        self.name = name

    ## class Cat has-a method named print_cat_data()
    def print_cat_data(self):
        print("Cat name: ", self.name)
        print("Race: ", self.race)
        print("Color: ", self.color)

## Person is-a object
class Person(object):

    '''class Person() - To handle the name and pet of Person'''
    def __init__(self, name):
        ## class Person has-a attribute named name
        self.name = name
        ## Person has-a pet of some king
        self.pet = None

## Employee is-a Person
class Employee(Person):

    '''class Employee() - To handle the name, salary and id of Employee'''
    def __init__(self, name, salary, id):
        ## Inheritance from class Person()
        super(Employee, self).__init__(name)
        ## Employee has-a attribute named salary
        self.salary = salary
        ## Employee has-a attribute named id
        self.id = id

    ## class Employee has-a method named print_employee_data()
    def print_employee_data(self):
        print("Employee name: ", self.name)
        print("Salary: ", self.salary)
        print("ID: ", self.id)

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    
    '''class Salmon() - To handle the name of Salmon fish'''
    def __init__(self, name):
        self.name = name

## Halibut is-a Fish
class Halibut(Fish):
    
    '''class Halibut() - To handle the name of Halibut fish'''
    def __init__(self, name):
        self.name = name

## rover is-a Dog
rover = Dog("Rover", "Pug", "Brown")
## from rover get print_dog_data method
rover.print_dog_data()
print()
## satan is-a Cat
satan = Cat("Satan", "Ragdoll", "Black")
## from satan get print_cat_data method
satan.print_cat_data()

## mary is-a Person
mary = Person("Mary")
print()
print("Person name: ", mary.name)

## mary has-a pet of sata
mary.pet = satan
print(mary.pet)

print()
## frank is-a Employee
frank = Employee("Frank", 120000, 9087334)
## from frank get print_employee_data method
frank.print_employee_data()

print()
## fran has-a pet of rover
frank.pet = rover
print(frank.pet)

## flipper is-a Fish
flipper = Fish()
print(flipper)