import math

GREEN = "\033[92m"
RESET = "\033[0m"
PINK = "\033[95m"

class Solution:
    def kClosest(self, points, k):
        print(points)
        def dist(point):
            return round(math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2)), 2)
        
        if len(points) == 1 or len(points) == 0:
            return points

        dists = {index: dist(point) for index, point in enumerate(points)}
        dists = sorted(dists.items(), key=lambda item: item[1])
        res = [points[i[0]] for i in dists]
        
        return res[:k]
            

sol = Solution()
print()
print(f'{PINK}case1 {sol.kClosest([[1,3],[-2,2]], 1)}{RESET}')
print(f'{PINK}case2 {sol.kClosest([[3,3],[5,-1],[-2,4]], 2)}{RESET}')
print(f'{PINK}case3 {sol.kClosest([[0,1],[1,0]], 2)}{RESET}')
print()

            
            