import heapq as hq
class Restaurant:
    # Init the rating and number of meals of each kind
    def __init__(self, name="NoName",rt=5, tot=0, veg=0, gf=0, nf=0, ff=0):
        self.name = name
        self.rt = rt
        self.tot = tot
        self.veg = veg
        self.gf = gf
        self.nf = nf
        self.ff = ff
        self.other = tot-veg-gf-nf-ff
    def __lt__(self, other):
        return self.rt > other.rt

    def __repr__(self):
        return "{0:s} Rating: {1:d} TotalServe: {2:d}".format(self.name,self.rt,self.tot)
"""
    def getRating(self):
        return self._rating

    def getTotal(self):
        return self._tot

    def getTotal(self):
        return self._tot

    def getVegetarian(self):
        return self._veg

    def getGlutenFree(self):
        return self._gf

    def getNutFree(self):
        return self._nf

    def getFishFree(self):
        return self._ff

    def getOther(self):
        return self._other
"""


class MealNeed:
    def __init__(self, tot=0, veg=0, gf=0, nf=0, ff=0):
        self.tot = tot
        self.veg = veg
        self.gf = gf
        self.nf = nf
        self.ff = ff
        self.other = tot-veg-gf-nf-ff




class MealOrderSolver:
    def __init__(self):
        self.feed = []
        self.result = {}
        self.tot = 0
        self.veg = 0
        self.gf = 0
        self.nf = 0
        self.ff = 0
        self.other = 0

    def addNeed(self, need):
        self.tot += need.tot
        self.veg += need.veg
        self.gf += need.gf
        self.nf += need.nf
        self.ff += need.ff
        self.other += need.other

    def addRestaurant(self, rest):
        hq.heappush(self.feed, rest)

    def run(self):
        for i in range(len(self.feed)):
            rest = hq.heappop(self.feed)
            order = {}
            # if both need and available are not 0
            if (self.veg*rest.veg):
                if (self.veg > rest.veg):
                    order["vegetarian"] = rest.veg
                    self.veg -= rest.veg
                    self.tot -= rest.veg
                else:
                    order["vegetarian"] = self.veg
                    self.tot -= self.veg
                    self.veg = 0

            if (self.gf*rest.gf):
                if (self.gf > rest.gf):
                    order["gluten free"] = rest.gf
                    self.gf -= rest.gf
                    self.tot -= rest.gf
                else:
                    self.tot -= self.gf
                    order["gluten free"] = self.gf
                    self.gf = 0
           
            if (self.nf*rest.nf):
                if (self.nf > rest.nf):
                    order["nut free"] = rest.nf
                    self.nf -= rest.nf
                    self.tot -= rest.nf
                else:
                    self.tot -= self.nf
                    order["nut free"] = self.nf
                    self.nf = 0

            if (self.ff*rest.ff):
                if (self.ff > rest.ff):
                    order["fish free"] = rest.ff
                    self.ff -= rest.ff
                    self.tot -= rest.ff
                else:
                    self.tot -= self.ff
                    order["fish free"] = self.ff
                    self.ff = 0

            if (self.other*rest.other):
                if (self.other > rest.other):
                    order["other"] = rest.other
                    self.other -= rest.other
                    self.tot -= rest.other
                else:
                    self.tot -= self.other
                    order["other"] = self.other
                    self.other = 0
            self.result[rest.name] = order
            if (self.tot==0):
                break
        if (self.tot):
            raise NotEnoughMealError()

    def getSolution(self):
        return self.result

    def printSolution(self):
        for rest, order in self.result.items():
            print("{0:s} (".format(rest), end="")
            for key, value in order.items():
                print("{0:d} {1:s} ".format(value, key), end="")
            print(")")
        print("")

class NotEnoughMealError(Exception):
    def __init__(self):
        message = "Meals served are not enough!"
        super().__init__(message)

class OMSolver:
    def main():
        mealNeed1 = MealNeed(50,5,7)
        mealNeed2 = MealNeed(50,5,5,5,5)
        rest1 = Restaurant("Restaurant A",5,40,4)
        rest2 = Restaurant("Restaurant B",3,100,20,20)
        rest3 = Restaurant("Restaurant C",5,20,5,5,5,5)
        solver = MealOrderSolver()
        solver.addNeed(mealNeed1)
        solver.addNeed(mealNeed2)
        solver.addRestaurant(rest1)
        solver.addRestaurant(rest2)
        solver.addRestaurant(rest3)
        solver.run()
        solver.printSolution()








