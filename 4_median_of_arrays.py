class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        l1 = len(nums1)
        l2 = len(nums2)

        # avoid [] data
        if l1 == 0:
            nums1 = nums2
        if l2 == 0:
            nums2 = nums1

        # make sure len(nums2) > len(nums1)
        if l1 > l2:
            nums1, nums2 = nums2, nums1
            l1, l2 = l2, l1

        l = l1 + l2
        is_odd = l % 2
        half_l = (l + 1) // 2

        MIN = min(nums1[0], nums2[0])
        MAX = max(nums1[-1], nums2[-1])

        class Cut:
            """
            cut range [0, l]
            position=0:    | 0 1 2 ... i-1   i ...     l-1
            position=i:      0 1 2 ... i-1 | i ...     l-1
            position=l:      0 1 2 ... i-1   i ...     l-1 |
            """

            def __init__(self, nums, comp, min_pos, max_pos):
                self.l = len(nums)
                self.position = (self.l+comp) // 2
                self.nums = nums
                self.min_pos = min_pos
                self.max_pos = max_pos

            def get_right_min(self):
                if self.position == self.l:
                    return MAX
                else:
                    return self.nums[self.position]

            def get_left_max(self):
                if self.position == 0:
                    return MIN
                else:
                    return self.nums[self.position-1]

            def set_position(self, position):
                self.position = position

            def get_position(self):
                return self.position

            def cut_down(self):
                self.max_pos = self.position
                self.position = (self.max_pos + self.min_pos) // 2
                return self.position

            def cut_up(self):
                self.min_pos = self.position+1
                self.position = (self.min_pos + self.max_pos) // 2
                return self.position

            def get_len(self):
                return self.l

        # init cut makes num of left part no less than num of right part
        # if the number is odd, comp=0 divides n|n+1; comp=1 divides n+1|n
        # if the number is even, comp=0 or 1 both leads to equal dividing
        # This is quite ugly for clearity
        if (l1 % 2 == 1) and (l2 % 2 == 1):
            # odd odd
            cut1 = Cut(nums1, comp=0, min_pos=0, max_pos=l1)
            cut2 = Cut(nums2, comp=1, min_pos=half_l-l1, max_pos=half_l)
        elif (l1 % 2 == 0) and (l2 % 2 == 1):
            # even odd
            cut1 = Cut(nums1, comp=0, min_pos=0, max_pos=l1)
            cut2 = Cut(nums2, comp=1, min_pos=half_l-l1, max_pos=half_l)
        elif (l1 % 2 == 1) and (l2 % 2 == 0):
            # odd even
            cut1 = Cut(nums1, comp=1, min_pos=0, max_pos=l1)
            cut2 = Cut(nums2, comp=0, min_pos=half_l-l1, max_pos=half_l)
        elif (l1 % 2 == 0) and (l2 % 2 == 0):
            # even even
            cut1 = Cut(nums1, comp=0, min_pos=0, max_pos=l1)
            cut2 = Cut(nums2, comp=0, min_pos=half_l-l1, max_pos=half_l)

        while True:
            c1_max, c2_max = cut1.get_left_max(), cut2.get_left_max()
            c1_min, c2_min = cut1.get_right_min(), cut2.get_right_min()

            left_max = max(c1_max, c2_max)
            right_min = min(c1_min, c2_min)
            if left_max <= right_min:
                if is_odd:
                    result = left_max
                else:
                    result = float(left_max + right_min) / 2
                break

            if c1_max < c2_max:
                position2 = cut2.cut_down()
            else:
                position2 = cut2.cut_up()

            position1 = half_l - position2
            cut1.set_position(position1)

        return result

if __name__ == '__main__':
    solution = Solution()
    ans = solution.findMedianSortedArrays([2, 3], [1])
    print(ans)
    ans = solution.findMedianSortedArrays([], [1])
    print(ans)
    ans = solution.findMedianSortedArrays([4], [1, 2, 3])
    print(ans)
