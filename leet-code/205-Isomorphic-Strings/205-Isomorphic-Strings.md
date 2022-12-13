## 205. Isomorphic Strings
Easy

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Example 3:

Input: s = "paper", t = "title"
Output: true

Constraints:

1 <= s.length <= 5 * 104
t.length == s.length
s and t consist of any valid ascii character.

### Solution Notes:
Interesting one-liner exists using `set()` and `zip()` built-in functions:
```py
    return len(set(zip(s, t))) == len(set(s)) == len(set(t))
```
or
```py
    return len(s)==len(t) and len(set(zip(s,t)))==len(set(s)) and len(set(s))==len(set(t))
```
`zip()` creates the mapping relationship for each element in s and t. `set()` removes duplicates. The lengths should be the same if isomorphic rules followed.
```py
    >>> s = 'abab'
    >>> t = 'baba'
    >>> list(zip(s,t))
    [('a', 'b'), ('b', 'a'), ('a', 'b'), ('b', 'a')]
    >>> list(set(zip(s,t)))
    [('b', 'a'), ('a', 'b')]
    >>> t = 'babb'
    >>> list(zip(s,t))
    [('a', 'b'), ('b', 'a'), ('a', 'b'), ('b', 'b')]
    >>> list(set(zip(s,t)))
    [('b', 'a'), ('a', 'b'), ('b', 'b')]
```


Another one-liner using `map()`:
```py
    return map(s.find, s) == map(t.find, t)
```
A bit cryptic, but makes sense if I think about the `list` outputs of the `map`s matching:
```py
    >>> s = 'abab'
    >>> t = 'baba'
    >>> list(map(s.find, s))
    [0, 1, 0, 1]
    >>> list(map(t.find, t))
    [0, 1, 0, 1]
```


Expanded form using two dictionaries. Straightforward, readable:
```py
    s2t, t2s = {}, {}
    for i in range(len(s)):
        if s[i] in s2t and s2t[s[i]] != t[i]:
            return False
        if t[i] in t2s and t2s[t[i]] != s[i]:
            return False
        s2t[s[i]] = t[i]
        t2s[t[i]] = s[i]
    return True
```

