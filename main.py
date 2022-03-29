import game_data
import art
from random import randint

# TODO:

data = game_data.data
game_logo = art.logo
vs_logo = art.vs

user_score = 0

used_indices_list = []


def article_solver(index):
    """Sets a correct article before nouns.
    Returns 'a' or 'an' automatically."""

    if data[index]["description"][0] in ["A", "E", "I", "O", "U"]:
        return "an "
    else:
        return "a "


def generate_rand_ind():
    """Generate and return a random integer.
    The new integer will be filled in the used indices list.
    No duplicates will be made."""

    rand_int = randint(0, len(data) - 1)

    if rand_int in used_indices_list:
        while rand_int in used_indices_list:
            rand_int = randint(0, len(data) - 1)

    used_indices_list.append(rand_int)

    return rand_int


def show_questions():
    """Shows the questions"""

    # Uncomment to see results for debugging purpose
    # print(data[random_index_1]["follower_count"])
    # print(data[random_index_2]["follower_count"])

    question_1 = "Compare A: " + data[random_index_1]["name"] + ", " + article_solver(random_index_1) + \
                 data[random_index_1]["description"] + " from " + data[random_index_1]["country"]
    print(question_1)
    print(vs_logo)
    question_2 = "Compare B: " + data[random_index_2]["name"] + ", " + article_solver(random_index_2) + \
                 data[random_index_2]["description"] + " from " + data[random_index_2]["country"]
    print(question_2)


print(game_logo)
run = True

random_index_1 = generate_rand_ind()

while run:
    # Main game loop

    if len(used_indices_list) < len(data):
        random_index_2 = generate_rand_ind()

        show_questions()

        user_input = input("Who has more followers? Type a or b: ")
        a = data[random_index_1]["follower_count"] > data[random_index_2]["follower_count"]

        if (user_input == "a" and a) or (user_input == "b" and not a):
            print(" ")
            random_index_1 = random_index_2
            user_score += 1
        else:
            print(" ")
            print(f"Not true. Your score is {user_score}.")
            try_again_prompt = input("Try again? Type y or n: ")

            if try_again_prompt == "y":
                user_score = 0
                used_indices_list.clear()
                continue
            else:
                break
    else:
        win_prompt = input(f"You won! Your score is {user_score}. Play again: Type y or n: ")

        if win_prompt == "y":
            continue
        else:
            break
