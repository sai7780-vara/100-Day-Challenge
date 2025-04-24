class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = []
        i = 0
        j = 0
        len1 = len(word1)
        len2 = len(word2)

        # Merge characters alternately from both strings
        while i < len1 and j < len2:
            merged.append(word1[i])
            merged.append(word2[j])
            i += 1
            j += 1

        # Append remaining characters from the longer word
        if i < len1:
            merged.append(word1[i:])
        if j < len2:
            merged.append(word2[j:])

        return ''.join(merged)
