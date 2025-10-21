class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        closet_total=nums[0]+nums[1]+nums[2]

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left = i+1
            right = len(nums)-1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < target:
                    left += 1
                elif total > target:
                    right -= 1
                else:
                    return total

                if abs(total - target) < abs(closet_total - target):
                    closet_total = total
        
        return closet_total