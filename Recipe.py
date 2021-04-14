from random import randint


class Recipe:
    def __init__(self, *inp):
        """
        Constructor will detect if there is any inputs passed during construction, and will
        choose one of the two statements to execute. If nothing is passed during creation,
        the class will create a blank item with empty lists and "No name given" as the title.
        Whether if arguments are passed or not, the constructor will assign a random recipe
        ID as to allow for easier search functionality.
        """
        if len(inp) == 3:
            self.name = inp[0]
            self.ingredients = inp[1]
            self.steps = inp[2]
        else:
            self.name = "No set name"
            self.ingredients = []
            self.steps = []
        self.uniqueID = 10000 + randint(0, 9999)

    def resetName(self, name):
        self.name = name
        # Works as intended, will change the name to passed value

    def getName(self):
        return self.name
        # Works as intended, returns name within class

    def getRecipeID(self):
        return self.uniqueID
        # Works as intended, returns randomly assigned RecipeID

    def getIngredients(self):
        return self.ingredients
        # Works as intended, returns list of ingredients

    def getSteps(self):
        return self.steps
        # Works as intended, returns list containing string of steps

    def addIngredients(self, original):
        self.ingredients.extend(original)
        # Works as intended, adds items in passed list to Ingredients list

    def addSteps(self, original):
        self.steps.extend(original)
        # Works as intended, adds items in passed list to Ingredients list
