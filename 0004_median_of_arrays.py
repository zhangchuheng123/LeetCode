# 既然提示了 O(log(m+n)) 的算法，肯定是要二分查找，只要遍历一遍就跪了
# 找一个 partition (ind1, ind2) 使得刚左边一半的数字比右边一半的数字都小于等于

class Solution:
    def findMedianSortedArrays(self, nums1, nums2):

        INF = 1e6 + 1

        # There should be k numbers partitioned to the left
        n1, n2 = len(nums1), len(nums2) 
        k = (n1 + n2 + 1) // 2
        is_even = ((n1 + n2) % 2 == 0)

        # make sure nums1 is longer
        if n2 > n1:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        # special case
        if n2 == 0:
            if is_even:
                return float((nums1[k-1] + nums1[k]) / 2)
            else:
                return float(nums1[k-1])

        # find a partition point such that 
        # 1) ind1 + ind2 = k
        # 2) nums2[ind2-1] <= nums1[ind1] and nums1[ind1-1] <= nums2[ind2]
        ind1 = k                                        
        ind2 = 0                                        
        delta = k                                      

        while True:
            l1 = nums1[ind1-1] if ind1-1 >= 0 else -INF 
            r1 = nums1[ind1] if ind1 < n1 else INF      
            l2 = nums2[ind2-1] if ind2-1 >= 0 else -INF
            r2 = nums2[ind2] if ind2 < n2 else INF             
            if l2 <= r1 and l1 <= r2:
                if is_even:
                    return float((max(l1, l2) + min(r1, r2) ) / 2)
                else:
                    return float(max(l1, l2))
            elif l1 > r2:
                delta = (delta + 1) // 2
                ind1 = max(0, ind1 - delta)
                ind2 = min(k - ind1, n2)
                ind1 = k - ind2
            elif l2 > r1:
                delta = (delta + 1) // 2
                ind1 = min(ind1 + delta, n1)
                ind2 = k - ind1

if __name__ == '__main__':
    solution = Solution()
    print(solution.findMedianSortedArrays([1], [2, 3, 4, 5]))