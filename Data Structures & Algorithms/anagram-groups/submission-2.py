from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)
        
        for s in strs:
            alphabet = [0] * 26
            for char in s:
                alphabet[ord(char)-ord("a")] += 1
            count[tuple(alphabet)].append(s)        

        return list(count.values())




