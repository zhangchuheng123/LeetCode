class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        set1 = set()
        for num in nums1:
            count = 0
            while (num, count) in set1:
                count += 1
            set1.add((num, count))


        return list(set(nums1).intersect(set(nums2)))