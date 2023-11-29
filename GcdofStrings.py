# class Solution(object):
#     def gcdOfStrings(self, str1, str2):
#         """
#         :type str1: str
#         :type str2: str
#         :rtype: str
#         """

#         """
#         str1 = "ABCABC", str2 = "ABC"
#         Output: "ABC"
#         ABCABCABC ABCABCABC

#         str1 = "ABABAB", str2 = "ABAB"
#         Output: "AB"
#         ABABABABABAB ABABABABAB

#         str1 = "LEET", str2 = "CODE"
#         Output: ""
#         LEETCODE CODELEET

#         """
#         l = []
#         m = []

#         if len(str1) < len(str2):

#             for i in range(len(str1)):
#                 if str1[i] not in l or str2[i] not in m:
#                     l.append(str1[i])
#                     m.append(str2[i])
#         else:
#             for i in range(len(str2)):
#                 if str1[i] not in l or str2[i] not in m:
#                     l.append(str1[i])
#                     m.append(str2[i])
#         if l == m:
#             gcd = ''.join(m)
#         return gcd


# sol = Solution()

# print(sol.gcdOfStrings("ABCABC", "ABC"))


class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        l = []
        m = []
        gcd = ""

        if str1 + str2 != str2 + str1:
            return ""

        if len(str1) < len(str2):

            for i in range(len(str1)):
                if str1[i] not in l or str2[i] not in m:
                    l.append(str1[i])
                    m.append(str2[i])

        else:
            for i in range(len(str2)):
                if str1[i] not in l or str2[i] not in m:
                    l.append(str1[i])
                    m.append(str2[i])
        if l == m:
            gcd = ''.join(m)
        return gcd


sol = Solution()

print(sol.gcdOfStrings("TAUXXTAUXXTAUXXTAUXXTAUXX",
      "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
