import unittest
from omsolver import *

class TestMealOrderSolver(unittest.TestCase):
    def setUp(self):
        self.mealNeed1 = MealNeed(50,5,7) 
        self.mealNeed2 = MealNeed(50,5,5,5,5)
        self.rest1 = Restaurant("Restaurant A",5,40,4)
        self.rest2 = Restaurant("Restaurant B",3,100,20,20)
        self.rest3 = Restaurant("Restaurant C",5,20,5,5,5,5)
        self.solver = MealOrderSolver()


    def test_not_enough_meal(self):
        self.solver.addNeed(self.mealNeed1)
        self.solver.addRestaurant(self.rest1)
        self.assertRaises(NotEnoughMealError,self.solver.run)

    def test_two_restaurant(self):
        self.solver.addNeed(self.mealNeed1)
        self.solver.addRestaurant(self.rest1)
        self.solver.addRestaurant(self.rest2)
        self.solver.run()
        self.assertDictEqual(self.solver.getSolution(), {"Restaurant A":{"vegetarian":4,"other":36}, 
            "Restaurant B":{"vegetarian":1,"gluten free":7,"other":2}})

    def test_three_restaurant(self):
        self.solver.addNeed(self.mealNeed1)
        self.solver.addNeed(self.mealNeed2)
        self.solver.addRestaurant(self.rest1)
        self.solver.addRestaurant(self.rest2)
        self.solver.addRestaurant(self.rest3)
        self.solver.run()
        self.assertDictEqual(self.solver.getSolution(), {"Restaurant A":{"vegetarian":4,"other":36},
            "Restaurant C":{"vegetarian":5,"gluten free":5, "nut free":5, "fish free":5},
            "Restaurant B":{"vegetarian":1,"gluten free":7,"other":32}})


if __name__=='__main__':
    unittest.main()






