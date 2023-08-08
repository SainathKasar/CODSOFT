import random

#global variable we need
choices = ['rock', 'paper', 'scissors']
def get_user_choice():
    print("Choose:\n1.rock\n2.paper\n3.scissors")
    user_choice = int(input())
    while user_choice not in range(0,3):
        print("Invalid choice. Choose: rock, paper, or scissors")
        user_choice = int(input())
    return user_choice

def get_computer_choice():
    
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif user_choice == 1:
        return "You win!" if computer_choice == 'scissors' else "Computer wins!"
    elif user_choice == 2:
        return "You win!" if computer_choice == 'rock' else "Computer wins!"
    elif user_choice == 3:
        return "You win!" if computer_choice == 'paper' else "Computer wins!"

def play_game():
    user_score = 0
    computer_score = 0
     #chances you wanted to play
    while True:
        chances=3
        while chances>0:
            user_choice = get_user_choice()
            computer_choice = get_computer_choice()
            print(f"You chose: {choices[user_choice-1]}")
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if 'You win' in result:
                user_score += 1
            elif 'Computer wins' in result:
                computer_score += 1

            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")

            chances-=1
        play_again = input("Do you want to play again? (yes/no) ").lower()
        if play_again == 'no':
            break
        else:
            chances=3
    
if __name__=="__main__":
    play_game()
        
