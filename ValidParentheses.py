class Solution:
    def isValid(self, s: str) -> bool:

        opens = ['(','{','[']

        closes = [')','}',']']

        start = []
        end = []


    
        for char in s:

            

            if(char in opens):
                start.append(char)
                
                

            elif(char in closes):
                end.append(char)
                if(len(start)>0 and opens[closes.index(char)] == start[-1]):
                    start.pop(-1)
                    end.pop(-1)
                else:
                    return False
        
                    


        if(len(start) != 0 or len(end)!=0):
            return False
        return True