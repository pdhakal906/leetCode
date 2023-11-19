class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """

        """
        abcd, pqrs = apbqcrds
        abcd, pq = apbqcd
        ab, pqrs = apbqrs 
        """

        new_word = ""

        if len(word1) == len(word2):
            for i in range(len(word1)):
                new_word += word1[i] + word2[i]
        if len(word1) > len(word2):
            for i in range(len(word1)):
                try:
                    new_word += word1[i] + word2[i]
                except IndexError:
                    new_word += word1[i:]
                    break
        if len(word2) > len(word1):
            for i in range(len(word2)):
                try:
                    new_word += word1[i] + word2[i]
                except IndexError:
                    new_word += word2[i:]
                    break

        return new_word


sol = Solution()
print(sol.mergeAlternately("ab", "pqrs"))
