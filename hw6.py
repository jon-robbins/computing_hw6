##Question 1

# commenting out the earlier version 

#class Patient:
#   test_name = ""
#    test_result = False
#
#    def __init__(self, name: str, symptoms: list):
#        self.name = name
#        self.symptoms = symptoms
#
#    def add_test(self, name: str, result: bool):
#        Patient.test_name = name
#        Patient.test_result = result
#
#    def has_covid(self):
#        if Patient.test_name == "covid":
#            if Patient.test_result:
#                return 0.99
#            else:
#                return 0.01
#        else:
#            prob = 0.05
#            for symptom in self.symptoms:
#                print(symptom)
#                if symptom in ['fever', 'cough', 'anosmia']:
#                    prob = prob + 0.1
#            return prob

# including a new  version

class Patient:

    def __init__(self, name: str, symptoms: list):
        self.name = name
        self.symptoms = symptoms


    def add_test(self, name: str, results: bool):
        self.test_name = name
        self.test_results = results

    def has_covid(self):
        if hasattr(self, 'test_name'):
            if self.test_name == 'covid':
                if self.test_results == True:
                    return 0.99
                else:
                    return 0.01

        else:
            prob = 0.05
            for s in list(set(self.symptoms)):
                if s in ['fever', 'cough', 'anosmia']:
                    prob += 0.1
            return round(prob, 2)


# p1 = Patient('Ken', ['fever', 'anosmia', 'headache', 'fever'])
# p2 = Patient('Lisa', ['sore throat', ])
# p1.add_test('covid', True)
# # p1.add_test('covid', False)
# print(p1.has_covid())
# print(p2.has_covid())

##Question 2
import random

class Card:
    suit = ""
    value = ""

    def __init__(self, suit, value):
        Card.suit = suit
        Card.value = value


class Deck:
    def __init__(self):
        self.englishDeck = []
        for suit in ["Hearts", "Diamonds", "Clubs", "Spades"]:
            for value in ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]:
                self.englishDeck.append(Card(suit, value))

    def shuffle(self):
        random.shuffle(self.englishDeck)

    def draw(self):
        index = random.randint(0, len(self.englishDeck) - 1)
        print(index)
        print("The suit is :" + self.englishDeck[index].suit + " and the value is :" + self.englishDeck[index].value)
        del self.englishDeck[index]


##Question 3
from abc import ABCMeta, abstractmethod
import math


class PlaneFigure(metaclass=ABCMeta):
    def __init__(self):
        pass

    @abstractmethod
    def compute_perimeter(self):
        pass

    @abstractmethod
    def compute_surface():
        pass


class Triangle(PlaneFigure):
    def __init__(self, base, c1, c2, h):
        self.base = base
        self.c1 = c1
        self.c2 = c2
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2

    def compute_surface(self):
        return self.base * self.h


class Rectangle(PlaneFigure):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def compute_perimeter(self):
        return 2 * (self.a + self.b)

    def compute_surface(self):
        return self.a * self.b


class Circle(PlaneFigure):
    def __init__(self, radius):
        self.radius = radius

    def compute_perimeter(self):
        return 2 * self.radius * math.pi

    def compute_surface(self):
        return math.pi * (self.radius ^ 2)