from itertools import chain, combinations
class Solution(object):
    def subsetsWithDup(self, nums):
        if len(nums) < 1:
            return [[]]
        else:   
            a = chain.from_iterable(combinations(nums, r) for r in range(len(nums)+1))
            sol = []
            for y in a:
                y = list(y)
                y.sort()
                sol.append(y)
            res = []
            for i in sol:
                if i not in res:
                    res.append(i)
        return res
            
        

if __name__ == '__main__':
    print(Solution().subsetsWithDup([4,4,4,1,4]))