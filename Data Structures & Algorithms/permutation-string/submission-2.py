class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        dic = {}
        for i in range(len(s1)):
            if s1[i] in dic:
                dic[s1[i]] += 1
            else:
                dic[s1[i]] = 1
        res = False
        currdic = {}
        # build first window
        for i in range(len(s1)):
            currdic[s2[i]] = currdic.get(s2[i], 0) + 1
        if dic == currdic:
            return True
        for i in range(1, len(s2) - len(s1) + 1):
            start = i
            end = i + len(s1) - 1
            if s2[end] in currdic:
                currdic[s2[end]] += 1
            elif s2[end] not in currdic:
                currdic[s2[end]] = 1
            currdic[s2[i-1]] -= 1
            if currdic[s2[i - 1]] == 0:
                currdic.pop(s2[i - 1])
            if dic == currdic:
                res = True
                break
        return res

            

        