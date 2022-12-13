
def isSubsequence(s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if s == "": return True
        if t == "": return False
        i, j = 0, 0
        while True:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
            if i == len(s): return True
            if j == len(t): return False
            
        ### alternate using recursion
        # if s == "": return True
        # if t == "": return False
        # return isSubsequence(s[1:], t[1:]) if s[0] == t[0] else isSubsequence(s, t[1:])
        
        ### alternate using for loop
        # for c in s:
        #     i = t.find(c)
        #     if i == -1: return False
        #     t = t[i + 1:]
        # return True
        