class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp

        totalLen = (len(nums1) + len(nums2))
        L1 = 0
        R1 = len(nums1) - 1

        while True:
            M1 = (L1 + R1) // 2
            P2 = (totalLen // 2) - M1 - 2

            left1 = nums1[M1] if -1 < M1 < len(nums1) else float('-inf')
            right1 = nums1[M1+1] if -1 < M1 + 1 < len(nums1) else float('inf')
            left2 = nums2[P2] if -1 < P2 < len(nums2) else float('-inf')
            right2 = nums2[P2+1] if -1 < P2 + 1 < len(nums2) else float('inf')

            if left1 <= right2 and left2 > right1:
                L1 = M1 + 1
            elif left1 > right2 and left2 <= right1:
                R1 = M1 - 1
            else:
                if totalLen % 2:
                    return min(right1, right2)
                else:
                    return (max(left1, left2) + min(right1, right2)) / 2