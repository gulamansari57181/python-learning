# Creating my own Datatype to perform +,-,* and / operations on fraction data
class Fraction:
    # Initializing parametarized constructor
    def __init__(self,num,deno):
        self.num=num
        self.deno = deno
        
    # To display our fraction datatype in required format using __str__ magic  method
    def __str__(self):
        return "Fraction is : {}/{}".format(self.num,self.deno)
    
    
    # To implement add method for two fraction numbers
    def __add__(self,other):
        result_num = self.num * other.deno + self.deno * other.num
        result_deno= self.deno * other.deno
        
        return "Result of add is : {}/{}".format(result_num,result_deno)
    
    
    # To implement sub method for two fraction numbers
    def __sub__(self,other):
        result_num = self.num * other.deno - self.deno * other.num
        result_deno= self.deno * other.deno
        
        return "Result of sub is : {}/{}".format(result_num,result_deno)
    
     # To implement multiplication method for two fraction numbers
    def __mul__(self,other):
        result_num = self.num * other.num 
        result_deno= self.deno * other.deno
        
        return "Result of multiplication is : {}/{}".format(result_num,result_deno)
    
      # To implement sub method for two fraction numbers
    def __truediv__(self,other):
        result_num = self.num * other.deno
        result_deno= self.deno * other.num
        
        return "Result of division is : {}/{}".format(result_num,result_deno)
    
frcation1 = Fraction(1,3)  
fraction2 = Fraction(2,3)

print(frcation1)   
print(fraction2)   

print(frcation1 + fraction2)
print(frcation1 - fraction2)
print(frcation1 * fraction2)
print(frcation1 / fraction2)

        