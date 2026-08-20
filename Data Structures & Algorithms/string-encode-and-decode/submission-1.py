class Solution:
    
    def __init__(self):
        self.code = '#!#!?'

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for s in strs:
            encoded_string += f'{self.code}{s}'
        # encoded_string = f'{self.code}'.join(strs)
        encoded_string += self.code
        return encoded_string

    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        return s.split(self.code)[1:-1]
        # res = []
        # curr = ''
        # for char in s:
        #     if curr 