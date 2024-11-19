# Leetcode 1603

class Solution:
    def __init__(self, big, medium, small):
        self.bigSpace = big
        self.mediumSpace = medium
        self.smallSpace = small
        self.slots = [self.bigSpace, self.mediumSpace, self.smallSpace]

    def addCar(self, carType):
        if self.slots[carType-1] == 0:
            return False

        self.slots[carType-1] -= 1
        return True
    
parkingSys = Solution(1,1,5)
print(parkingSys.addCar(1))
print(parkingSys.addCar(2))
print(parkingSys.addCar(1))
print(parkingSys.addCar(3))