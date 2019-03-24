'''功劳在于re函数库哈哈哈'''
import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        pattern=re.compile(p)
        m=pattern.match(s)
        if m:
            if m.group()==s:
                return True
            else:
                return False
        else:
            return False
