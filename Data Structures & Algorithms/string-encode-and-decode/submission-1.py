class Solution:

    def encode(self, strs: List[str]) -> str:           
        encoded_str = ""
        for s in strs:
            encoded_str += str(len(s)) + "#" + s
        return encoded_str

        #5#Hello5#World
            
    def decode(self, s: str) -> List[str]:
        res, i = [], 0
        while i < len(s):
            j = i
            while s[j] != "#": # loop until "#"            
                j += 1
            length = int(s[i:j])             
            res.append(s[j + 1: length + j + 1])
            i = j+ 1+ length
        return res




                





