class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for idx in range(len(digits)-1, -1, -1):
            digits[idx] = (digits[idx] + 1) % 10
            if digits[idx] == 0:
                if idx == 0:
                    digits.insert(0, 1)
            else:
                break
        return digits