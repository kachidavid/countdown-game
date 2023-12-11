import random
def play_human_turn(n):
    # 1. prompt user for their move
    # 2. output number of coins after user's move
    user = int(input("User: "))
    while user <1 or user >3:
            print(f"User can't subtract a number greater than 3 or less than 1")
            user = int(input("User: "))
    print(f"user took {user} number of coins")
    n-=user
    if n == 0:
        print("User won the game!")
        print("Computer lost!")
    return n
    
    #p
# 3. If the human wins, indicate that and return 0
# You must implement this function
    pass
def play_computer_turn(n):
    comp = random.randint(1, 3)
    # 1. Make computer move
    if n % 4==0:
        n-=comp
        print(f"Computer has {n} coins left")
    else:
        comp = n % 4
        n-=comp
        print(f"Computer subtracted {comp} coins")
        
    if n == 0:
        print("Computer won the game")
        print("User lost!")
    return n
    # 2. If computer wins, indicate that and return 0
    # 3. return number of coins remaining
    # You must implement this function 
    pass
