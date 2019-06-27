'''从今天起，我要给我写过的代码写注释了，今天下午看了一个没有注释的代码，看不懂，
看的越来越生气，然后我更生气的发现，自己写的代码隔了一段时间也看不懂了，所以，
要给自己写的代码写注释啦'''

class Solution:
    def optimalDivision(self, nums: List[int]) -> str:
        if len(nums)==1:
            return str(nums[0])
        if len(nums)==2:
            return str(nums[0])+'/'+str(nums[1])  #字符串没有append函数，用+的方法来在末尾添加
        re=''
        re+=str(nums[0])
        re+='/('
        i=1
        for i in range(1,len(nums)):
            re+=str(nums[i])
            re+='/'
        re=re[:-1]      #因为执行完循环之后会在末尾多一个除号，所以把它去掉
        re+=')'
        return re
   
 '''这道题目还行吧，让找出得到的结果最大的算式，就是A/B的最大值，我们需要使A最大，B最小，
 因为只能往下除，肯定是越除越小，所以A最大的时候就是自己啦，B最小的时候就是从第二个数开始，
 一直往下除，所以括号就加在第二个数前面和末尾了'''
