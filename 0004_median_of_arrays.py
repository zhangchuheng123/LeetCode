class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """


        return result

if __name__ == '__main__':
    solution = Solution()
    ans = solution.findMedianSortedArrays([2, 3], [1])
    print(ans)
    ans = solution.findMedianSortedArrays([], [1])
    print(ans)
    ans = solution.findMedianSortedArrays([4], [1, 2, 3])
    print(ans)
