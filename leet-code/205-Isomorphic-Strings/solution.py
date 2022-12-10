
def isIsomorphic(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    if len(set(s)) == len(set(t)):
        s_replace_dict = {s[i]: t[i] for i in range(len(s))}
        new_s = [s_replace_dict[c] for c in s]
        if ''.join(new_s) == t:
            return True
    
    return False
        