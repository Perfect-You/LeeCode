'''最容易想到的当然是两个循环嵌套的方式，不过会超出时间限制，这个方法只需要遍历一遍'''
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h=0
        r=len(height)-1
        re=0
        while h<r:
            l=r-h
            if height[h]<height[r]:
                w=height[h]
                h+=1
            else:
                w=height[r]
                r-=1
            area=l*w
            if area>re:
                re=area
        return re
