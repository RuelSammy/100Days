#Create a class for a simple car with methods like start and stop.
class Car:

    """ Creating the class constructor. """

    """ What is the purpose of the constructor? """

    """ The purpose of the constructor is to initialize the attributes of the class. """
    def __init__(self, make, model, year):

        
        self.make = make
        self.model = model
        self.year = year
        self.is_engine_started = False

        """ Creating a method called start_engine. """

    def start_engine(self):
        
        """ Creating a condition to check if the engine is already started. """

        """ If the engine is already started, print the message. """

        """ If the engine is not started, start the engine and print the message. """
        
        if self.is_engine_started:
            print("The engine is already running.")
        else:
            self.is_engine_started = True
            print(f"The {self.year} {self.make} {self.model}'s engine is now running.")
        
# Creating an instance of the Car class
my_car = Car(make="Audi", model="Q5", year=2023)

# Calling the start_engine method
my_car.start_engine()