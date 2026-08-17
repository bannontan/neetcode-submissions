class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        prefix = ''
        for i in range(len(first_word)):
            common_char = first_word[i]
            for j in range(1, len(strs)):
                if len(strs[j]) <= i or strs[j][i] != common_char:
                    return prefix
            prefix += common_char

        return prefix