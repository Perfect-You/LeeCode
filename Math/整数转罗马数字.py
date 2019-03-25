class Solution:
    def intToRoman(self, num: int) -> str:
        li=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
        dic={1000:'M',500:'D',100:'C',50:'L',10:'X',5:'V',1:'I'}
        re=""
        for i in li:
            if i==900 and num//i==1:
                re+='CM'
                num-=900
            elif i==400 and num//i==1:
                re+='CD'
                num-=400
            elif i==90 and num//i==1:
                re+='XC'
                num-=90
            elif i==40 and num//i==1:
                re+='XL'
                num-=40
            elif i==9 and num//i==1:
                re+='IX'
                num-=9
            elif i==4 and num//i==1:
                re+='IV'
                num-=4
            elif num//i!=0:
                re+=(num//i)*dic[i]
                num-=(num//i)*i
        return re        
