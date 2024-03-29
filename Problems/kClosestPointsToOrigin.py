# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k, 
# return the k closest points to the origin (0, 0).

# The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

# You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).

from typing import List


# class Solution:
#     def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
#         largest = None
#         values = set()
#         sol = []
#         found = {}

#         for i in range(len(points)):
#             val = abs(points[i][0])**2 + abs(points[i][1])**2
#             if len(sol) < k:
#                 sol.append([points[i][0], points[i][1]])
#                 if val in found:
#                     found[val] += f'{len(sol)-1}'
#                 else:
#                     found[val] = f'{len(sol)-1}'
                
#                 values.add(val)    

#                 if not largest:
#                     largest = val
#                 else:
#                     largest = max(largest,val)
            
#             else:
#                 if val < largest:
#                     f_larg = found[largest]
#                     ind = f_larg[0]
#                     #Removes the first index of the string assigned to the variable
#                     if len(f_larg) > 1:
#                         found[largest] = f_larg[1::]
#                     else:
#                         found.pop(largest)
#                         values.remove(largest)
                    
#                     sol[int(ind)] = [points[i][0], points[i][1]]

#                     if val in found:
#                         found[val] += ind
#                     else:
#                         found[val] = ind
#                         values.add(val)
                        
#                     largest = max(values)
                
#         return sol


class Solution():
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        if k > len(points):
            return points

        values = []
        sol = []
        for pair in points:
            values.append(self.euclidean(pair))

        values = sorted(values)
        cutoff = values[k-1]

        l = 0
        for pair in points:
            if self.euclidean(pair) <= cutoff:
                sol.append(pair)
                l += 1

            if l > k: break

        return sol

    def euclidean(self, pair: List) -> int:
        return pair[0] * pair[0] + pair[1] * pair[1]


if __name__ == '__main__':
    solution = Solution()
    blah = [[2,2],[2,2],[2,2],[2,2],[2,2],[2,2],[1,1]]
    points = [[1,3],[-2,2]]
    dog = [[3,3],[5,-1],[-2,4]]
    k = 1
    print(solution.kClosest(blah,k))