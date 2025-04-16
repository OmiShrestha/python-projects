import math

def guess_number():
    print("Pick a number between a lower and upper bound.")
    
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))
    
    # for min guessed for computer
    ## I think this is what the question is asking ##
    max_guesses = math.ceil(math.log2(upper_bound - lower_bound + 1))
    print(f"I will guess your number in at most {max_guesses} attempts.")
    
    # initialize range
    low = lower_bound
    high = upper_bound
    attempts = 0 # counter for attempts
    
    while low <= high:
        if attempts >= max_guesses:
            print("You entered misleading hints.")
            break
        
        # computer makes a guess (mid-point for guess)
        guess = (low + high) // 2
        attempts += 1
        print(f"My guess is: {guess}")
        
        # Get feedback from the user
        feedback = input("Enter '=', '>', or '<': ").strip().lower()
        
        if feedback == '=':
            print(f"I guessed your number in {attempts} attempts!")
            break
        elif feedback == '>':
            if guess == high:  # check for inconsistency 
                print("Your hints are inconsistent.")
                break
            low = guess + 1
        elif feedback == '<':
            if guess == low:  # check for inconsistency
                print("Your hints are inconsistent.")
                break
            high = guess - 1
        else:
            print("Invalid input. Please enter '=', '>', or '<'.")
            attempts -= 1  # to not count invalid attempts

        # to ensure user is not cheating
        if low > high:
            print("Your hints are inconsistent.")
            break

def main():
    guess_number()

main()