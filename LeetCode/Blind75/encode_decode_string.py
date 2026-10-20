class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s

        return encoded_str

    def decode(self, s: str) -> list[str]:
        result = []

        # count len of word and append to it like
        # hello -> 5#hello
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            end = start + length

            result.append(s[start:end])
            i = end

        return result


strs = ["Hello", "World"]
sol = Solution()
encoded = sol.encode(strs)
decoded = sol.decode(encoded)

print(encoded)
print(decoded)
