'''一开始判断是否是质数就是从2到根号x看是否能整除，然后一直超出时间限制，只好求助网络，
下面是尼拉多塞筛法：西元前250年，希腊数学家厄拉多塞(Eeatosthese)想到了一个非常美妙的质
数筛法，减少了逐一检查每个数的的步骤，可以比较简单的从一大堆数字之中，筛选出质数来，这方
法被称作厄拉多塞筛法(Sieve of Eeatosthese)。 具体操作：先将 2~n 的各个数放入表中，然后
在2的上面画一个圆圈，然后划去2的其他倍数；第一个既未画圈又没有被划去的数是3，将它画圈，再
划去3的其他倍数；现在既未画圈又没有被划去的第一个数是5，将它画圈，并划去5的其他倍数……依次
类推，一直到所有小于或等于n的各数都画了圈或划去为止。这时，表中画了圈的以及未划去的那些数
正好就是小于 n 的素数。'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<3:
            return 0
        prime=[1]*n
        prime[0]=prime[1]=0
        for i in range(2,int(n**0.5+1)):
            if prime[i]==1:
                prime[i*i:n:i]=[0]*len(prime[i*i:n:i])
        return sum(prime)
