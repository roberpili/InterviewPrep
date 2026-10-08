# T: O(n), S: O(n)
class Solution:
    def two_sum(self, nums: list[int], target: int) -> list[int]:
        seen = {}

        for i in range(len(nums)):
            needs = target - nums[i]
            if needs in seen:
                return [i, seen[needs]]

            seen[nums[i]] = i

        return []


nums = [2, 7, 11, 15]
target = 9
sol = Solution()
print(sol.two_sum(nums, target))
