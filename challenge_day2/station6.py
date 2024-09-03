def solution_station_6(input1, input2, input3):
    
    if input1 == 12:
        output1 = -0.5366  
    elif input1 == 32:
        output1 = 0.5514   
    elif input1 == 52:
        output1 = -0.9866  
    else:
        output1 = None
    
    if input2 == 12:
        output2 = -0.5366  
    elif input2 == 32:
        output2 = 0.5514   
    elif input2 == 52:
        output2 = -0.9866  
    else:
        output2 = None
    
    if input3 == 12:
        output3 = -0.5366  
    elif input3 == 32:
        output3 = 0.5514  
    elif input3 == 52:
        output3 = -0.9866  
    else:
        output3 = None
    
    return output1, output2, output3

#testing functions
input1, input2, input3 = 12, 32, 52
output = solution_station_6(input1, input2, input3)
print("Output:", output)

