from sortedcontainers import SortedList
from bisect import bisect_left
from typing import *
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        ans = []
        left_data = SortedList()
        for i in range(len(nums)-1, -1, -1):
            if not ans:
                ans.append(0)
                left_data.add(nums[i])
            else:
                idx = bisect_left(left_data, nums[i])
                ans.append(idx)
                left_data.add(nums[i])
        return(ans[::-1])