import heapq


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        h = []
        heapq.heapify(h)

        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        # heap needs to priorize the number and not freq
        # for key, v in count.items():
        #             heapq.heappush(h, [key, -v])
        for key, v in count.items():
            heapq.heappush(h, [-v, key])

        result = []
        for i in range(k):
            result.append(heapq.heappop(h)[1])

        return result


nums = [1, 1, 1, 2, 2, 3]
k = 2
sol = Solution()

print(sol.topKFrequent(nums, k))
