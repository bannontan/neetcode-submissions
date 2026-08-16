class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash = defaultdict(int)
        t_hash = defaultdict(int)

        for char in s:
            s_hash[char] += 1
        
        for char in t:
            t_hash[char] += 1

        return s_hash == t_hash
