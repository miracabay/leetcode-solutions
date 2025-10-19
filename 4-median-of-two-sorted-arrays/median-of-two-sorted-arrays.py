class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        merged_nums = sorted(nums1+nums2)
        mid = len(merged_nums)//2
        if len(merged_nums) % 2 == 0:
            return (merged_nums[mid-1]+merged_nums[mid])/2.0
        else:
            return merged_nums[mid]