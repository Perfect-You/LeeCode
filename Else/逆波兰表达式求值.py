class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l=[]
        for i in range(len(tokens)):
            if tokens[i]!="+" and tokens[i]!="-" and tokens[i]!="*" and tokens[i]!="/" :
                l.append(int(tokens[i]))
            if tokens[i]=="+":
                a=l.pop()
                b=l.pop()
                c=b+a
                l.append(c)
            if tokens[i]=="-":
                a=l.pop()
                b=l.pop()
                c=b-a
                l.append(c)
            if tokens[i]=="*":
                a=l.pop()
                b=l.pop()
                c=b*a
                l.append(c)
            if tokens[i]=="/":
                a=l.pop()
                b=l.pop()
                c=int(b/a)
                l.append(c)
        return l[0]
