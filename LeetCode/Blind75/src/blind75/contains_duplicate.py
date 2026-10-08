class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        uniques = set()

        for n in nums:
            if n in uniques:
                return True
            uniques.add(n)

        return False


nums = [1, 2, 3, 4]
sol = Solution()
print(sol.containsDuplicate(nums))
