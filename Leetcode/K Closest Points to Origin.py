class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def dis(coords):
            x = coords[0]
            y = coords[1]
            return ((x*x) + (y*y)) ** 0.5


        hasher = {}
        finalArr = []
        ans = []
        for i in points:
            if dis(i) in hasher.keys():
                hasher[dis(i)].append(i)
            else:
                hasher[dis(i)] = [i]
        
        for j in hasher.keys():
            finalArr.append(j)

        finalArr.sort()
        i = 0
        counter = 0
        while counter < k:
            dist = finalArr[i]

            a = hasher[dist].pop()
            ans.append(a)
            counter += 1
            if hasher[dist] == []:
                i += 1
            
        return ans
