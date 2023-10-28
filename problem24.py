def canYouGetSame(n: int, m: int, s: str, t: str) -> int:
    if n < m:
        return 0
    else:
        s = list(s)
        k = 0
        try:
            for i in s:
                if s[k] == s[k+1]:
                    k = k+1
                    continue
                else:
                    if s[k] == t[k]:
                        k = k+1
                        continue
                    s.pop(k)
                    s.pop(k)
                    s.insert(k,str(t[k]))
                    k+=1
                    print("".join(s))
    
        except IndexError:
            pass
        t = list(t)
        
        
(canYouGetSame(21,20,"11100010","110000"))