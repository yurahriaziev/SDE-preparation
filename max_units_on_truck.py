class Solution:
    def maximumUnits(self, boxTypes, truckSize): # boxTypes: List[List[int]]
        if truckSize == 0:
            return 0
        
        # [numOfBoxes, unitsPerBox]
        box_count = [box[0] for box in boxTypes]
        total_boxes = sum(box_count)
        print(box_count)
        box_weight = [box[1]*box[0] for box in boxTypes]
        print(box_weight)
        print('total boxes', total_boxes)

        
        # for box in boxTypes:
        #     while box[0] > 0:
        #         if box[0] < truckSize:



sol = Solution()
# print(sol.maximumUnits([[1,3], [2,2], [3,1]], 4))
print(sol.maximumUnits([[5,10], [2,5], [4,7], [3,9]], 10))