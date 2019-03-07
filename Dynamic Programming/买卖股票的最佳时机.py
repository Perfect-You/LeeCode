class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices)==0:
            return 0
        begin=prices[0]
        result=0
        for i in prices:
            if i-begin>result:
                result=i-begin
            if i<begin:
                begin=i
        return result
