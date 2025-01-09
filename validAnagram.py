class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map1 = dict()

        for i in s:
            map1[i] =map1.get(i, 0) + 1
        
        for j in t:
            map1[j] =map1.get(j, 0) - 1

        for key, value in map1.items():
            if map1[key] != 0:
                return False
        return True