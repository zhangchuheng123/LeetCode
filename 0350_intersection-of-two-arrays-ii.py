class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        set1 = {}
        for num in nums1:
            if num in set1:
                set1[num] += 1
            else:
                set1[num] = 1

        ans = []
        for num in nums2:
            if num in set1:
                set1[num] -= 1
                ans.append(num)
                if set1[num] == 0:
                    del set1[num]

        return ans