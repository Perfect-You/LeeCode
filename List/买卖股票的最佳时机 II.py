class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices is None or len(prices)==0:
            return 0
        result=0
        Begin=prices[0]
        for p in prices:
            if p>Begin:
               result+=p-Begin
               Begin=p
            else:
               Begin=min(Begin,p)
        return result
