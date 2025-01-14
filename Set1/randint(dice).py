import random 
    

def main():
    while True:
        print("Rolling the dice . . . ")
        print("Their Values are")
        
        value_one = (random.randint(1, 6))
        value_two = (random.randint(1, 6))
        print(value_one)
        print(value_two)
         
        continue_rolling = input("Roll them agin? (y = yes)")
        value= continue_rolling.upper()
        
        if value == 'Y':
            continue
        else:
            break
        

main()
            
        
        