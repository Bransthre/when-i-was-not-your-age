import random as R

def get_num_pair():
    return (R.randint(1, 999) / (10 ** R.randint(0, 2)), R.randint(1, 999) / (10 ** R.randint(0, 2)))

def compare_response(response, correct_answer):
    return abs(response - correct_answer) <= 10 ** -6

def main():
    while True:
        curr_question = get_num_pair()
        correct_ans = curr_question[0] * curr_question[1]
        curr_ans = float(input(f"Input the value: {curr_question[0]} * {curr_question[1]} = "))
        print(f"The correct answer is {round(correct_ans, 6)}")
        if compare_response(curr_ans, correct_ans):
            print("You are correct!")
        else:
            print(f"You are wrong with an error of {round(correct_ans - curr_ans, 6)}")

main()