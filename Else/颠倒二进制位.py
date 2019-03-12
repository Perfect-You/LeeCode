class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        x=str(bin(n))[2:]
        while len(x)<32:
            x="0"+x
        y=x[::-1]
        return int(y,2)
