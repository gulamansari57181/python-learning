# User will provide area of wall that can be paint by one can , and lenhth and breadth of the wall
# We have to calculate number of cans required to paint entire wall
import math
can_capacity=int(input("Enter capacity of can to paint the wall in square meter :"))
length  = int(input("Provide length of the wall :"))
breadth =int(input("Provide breadth of the wall :"))

def paintAreaCanCount(can_capacity,length,breadth):
    
    area = length*breadth
    return math.ceil(area/can_capacity)

      
no_can = paintAreaCanCount(can_capacity,length,breadth) 
print(f"Number of can that will be required is : {no_can}")
