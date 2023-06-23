class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        sum = 0

        symbols = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        for i in range(len(s)):
          if s[i] == "I":
            try:
                if s[i+1] == "V" or s[i+1] == "X":
                  sum -= symbols["I"]
                else:  
                    sum += symbols["I"]
            except IndexError:
                if s[i] == "V" or s[i] == "X":
                  sum -= symbols["I"] 
                else:
                  sum += symbols["I"]

          elif s[i] == "V":
              sum += symbols["V"]

          elif s[i] == "X":
            try:
                if s[i+1] == "L" or s[i+1] == "C":
                  sum -= symbols["X"]
                else:  
                    sum += symbols["X"]
            except IndexError:
                if s[i] == "L" or s[i] == "C":
                  sum -= symbols["X"] 
                else:
                  sum += symbols["X"]

          elif s[i] == "L":
              sum += symbols["L"]
              
          elif s[i] == "C":
            try:
                if s[i+1] == "D" or s[i+1] == "M":
                  sum -= symbols["C"]
                else:  
                    sum += symbols["C"]
            except IndexError:
                if s[i] == "D" or s[i] == "M":
                  sum -= symbols["C"] 
                else:
                  sum += symbols["C"]

          elif s[i] == "D":
              sum += symbols["D"]

          elif s[i] == "M":
              sum += symbols["M"]
        
        return sum
       


sol = Solution()
print(sol.romanToInt("VIII"))


# Another way:

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_to_integer = {
#             'I': 1,
#             'V': 5,
#             'X': 10,
#             'L': 50,
#             'C': 100,
#             'D': 500,
#             'M': 1000,
#         }
#         s = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace("XC", "LXXXX").replace("CD", "CCCC").replace("CM", "DCCCC")
#         return sum(map(lambda x: roman_to_integer[x], s))