class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def permutation(a,b):
            dic1, dic2 = {}, {}
            for char1 in a:
                if char1 in dic1:
                    dic1[char1] += 1
                else:
                    dic1[char1] = 1
            for char2 in b:
                if char2 in dic2:
                    dic2[char2] += 1
                else:
                    dic2[char2] = 1
            return dic1 == dic2
        left = 0
        for left in range(len(s2) - len(s1) + 1):
            if permutation(s2[left : left + len(s1)], s1):
                return True
        return False


        