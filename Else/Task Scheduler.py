class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        newtasks=tasks
        maxnum=0
        maxtask=""
        x=0
        newtasks=list(set(newtasks))
        for i in newtasks:
            if tasks.count(i)>maxnum:
                maxnum=tasks.count(i)
                maxtask=i
        for i in newtasks:
            if tasks.count(i)==maxnum and i!=maxtask:
                x+=1
        re=maxnum+n*(maxnum-1)+x
        return max(len(tasks),re)
