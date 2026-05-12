class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        small, big = nums1, nums2
        total = len(small) + len(big)
        half = total // 2

        if len(big) < len(small):
            small, big = big, small

        l, r = 0, len(small) - 1

        while True:
            smallMid = (l + r) // 2
            bigMid = half - smallMid - 2

            smallLeft = small[smallMid] if smallMid >= 0 else float('-inf')
            smallRight = small[smallMid + 1] if (smallMid + 1) < len(small) else float('inf')
            bigLeft = big[bigMid] if bigMid >= 0 else float('-inf')
            bigRight = big[bigMid + 1] if (bigMid + 1) < len(big) else float('inf')

            if smallLeft <= bigRight and smallRight >= bigLeft:
                if total % 2 > 0:
                    return min(smallRight, bigRight)
                return (max(smallLeft, bigLeft) + min(smallRight, bigRight)) / 2
            elif smallLeft > bigRight:
                r = smallMid - 1
            else:
                l = smallMid + 1