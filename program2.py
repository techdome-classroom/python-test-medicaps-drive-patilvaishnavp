class Solution(object):
    def romanToInt(self, s):
        ef romanToInt(self, s: str) -> int:
        roman_to_int_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        prev_value = 0
        for char in s[::-1]:  # Reverse iterate over the string
            value = roman_to_int_map[char]
            if value < prev_value:
                result -= value
            else:
                result += value
            prev_value = value
        return result

# Example usage:
solution = Solution()
print(solution.romanToInt("III"))     # Output: 3
print(solution.romanToInt("LVIII"))   # Output: 58
print(solution.romanToInt("MCMXCIV")) # Output: 1994
        pass
