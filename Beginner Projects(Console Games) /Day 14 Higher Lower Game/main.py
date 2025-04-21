import random 
import game_data
import art

def call_new_person():
    return random.choice(game_data.data)

a_option = call_new_person()
b_option = call_new_person()
if a_option == b_option :
    a_option = call_new_person()
player_score = 0


def compare_followers(followers_1, followers_2):
    if followers_1["follower_count"] > followers_2["follower_count"] :
        return followers_1["name"]
    else:
        return followers_2
    
right_answer = compare_followers(a_option,b_option)

print(art.logo)
correct_answer = True
while correct_answer :
    print(f"Compare A :{a_option["name"]}, {a_option["description"]} from {a_option["country"]} ")
    print(art.vs)
    print(f"Againts B : {b_option["name"]}, {b_option["description"]} from {b_option["country"]}")
    player_choice = input("Who has more followers? Type 'A' or 'B' : ").lower()
    if player_choice == "a" and right_answer == a_option:
        player_score += 1
        print(f"Correct!Your Score : {player_score}")
        a_option = right_answer
        b_option = call_new_person()
    elif player_choice == "b" and right_answer == b_option:
        player_score += 1
        print(f"Correct!Your Score : {player_score}")
        a_option = right_answer
        b_option = call_new_person()
    else:
        print(f"False! You Lose!Your Final Score is : {player_score}")
        correct_answer = False
    