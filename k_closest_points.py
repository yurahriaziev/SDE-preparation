import math

class Solution:
    def kClosest(self, points, k):
        def dist(point):
            return math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
        
        if len(points) == 1 or len(points) == 0:
            return points

        dists = {index:dist(point) for index, point in enumerate(points)}
        res = []
        min_dist = max(dists.values())
        # print(min_dist)
        a = 0
        while k > 0:
            # print('while iter', dists)
            for i in dists:
                # print('for iter', dists)
                if dists[i] < min_dist:
                    min_dist = dists[i]
                    # print(min_dist)
                    a = i
                    # print(a)
                    break
            k -= 1
            res.append(points[a])
            del dists[a]
            min_dist = max(dists.values())
            # print()        
        return res
            

sol = Solution()
print()
print(sol.kClosest([[1,3],[-2,2]], 1))
# print(sol.kClosest([[3,3],[5,-1],[-2,4]], 2))
print()

            
            