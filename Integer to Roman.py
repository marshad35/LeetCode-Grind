class Solution: 
    def intToRoman(self, num: int) -> str:

        numerals = [("I",1,), ("V",5),("X",10),("L",50),("C",100),("D",500),("M",1000)]
        places = []
        temp = num

        places.append(temp//1000*1000)
        temp -= (temp//1000*1000)
        places.append(temp//100*100)
        temp-=(temp//100*100)
        places.append(temp//10*10)
        temp-=(temp//10*10)
        places.append(temp//1*1)



        print(places)

        ret = ""

        
        for sub_num in places:

            if(sub_num == 4 or sub_num ==9 or sub_num ==40 or sub_num==90 or sub_num == 400 or sub_num ==900):
                
                for i in range(len(numerals)):
                    
                    for j in range(i+1,len(numerals)):
                        
                        if(numerals[j][1] - numerals[i][1] == sub_num):
                            ret += numerals[i][0]
                            ret+= numerals[j][0]
            else:
                dummy = 0
                j = len(numerals)-1
                i = 0
                while dummy < sub_num:
                    if(numerals[j][1] + dummy > sub_num):
                        j-=1
                    else:
                        dummy += numerals[j][1]
                        ret += numerals[j][0]
        return ret
