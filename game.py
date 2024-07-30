import random
#Asking for users choice and making it redundant.
def the_user_choice():
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock/paper/scissors): ")
    return user_choice
#Making the computer choose.
def the_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

#Determination of the winner considering all of the outcomes
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == 'rock' and computer_choice == 'scissors') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissors' and computer_choice == 'paper')
    ):
        return "You win!"
    else:
        return "Computer wins!"
#Creating an interface for the user.
def play_game():
    print("Welcome to Rock-Paper-Scissors Game!")
    
    user_choice = the_user_choice()
    computer_choice = the_computer_choice()

    print(f"You chose {user_choice}")
    print(f"Computer chose {computer_choice}")

    result = determine_winner(user_choice, computer_choice)
    print(result)
#Ensuring execution Of the code
if __name__ == "__main__":
    play_game()
