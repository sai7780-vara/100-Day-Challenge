class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        # Check if both strings can be formed by a common divisor string
        if str1 + str2 != str2 + str1:
            return ""

        # Find GCD of lengths
        gcd_length = gcd(len(str1), len(str2))
        return str1[:gcd_length]
