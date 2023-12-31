# -*- coding: utf-8 -*-
"""Question2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1QLpHtBCpOGrJ7BasUUaD9Vn_p3FTwORR
"""

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) <= 1:
            return s

        start, max_len = 0, 1  # Initialize the start and maximum length of the palindrome
        dp = [[False] * len(s) for _ in range(len(s))]  # Create a 2D DP table

        # All substrings of length 1 are palindromes
        for i in range(len(s)):
            dp[i][i] = True

        # Check for palindromes of length 2
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start = i
                max_len = 2

        # Check for palindromes of length 3 or more
        for length in range(3, len(s) + 1):
            for i in range(len(s) - length + 1):
                j = i + length - 1  # Ending index of the current substring

                # Check if the current substring is a palindrome
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True

                    # Update the start and max_len if a longer palindrome is found
                    if length > max_len:
                        start = i
                        max_len = length

        return s[start:start + max_len]