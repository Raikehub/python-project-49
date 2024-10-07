import random
import prompt

def main():
    print('May I have your name?')
    name = prompt.string()
    print(f"Hello, {name}!")
    print('What is the result of the expression?:')

    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
    }

    def game_step():
        number_in_question = random.randint(1, 100)
        number_in_question_2 = random.randint(1,100)
        op_symbol = random.choice(list(operations.keys()))
        op = operations[op_symbol]
        correct_answer = op(number_in_question, number_in_question_2)

        print(f'Question: {number_in_question} {op_symbol} {number_in_question_2}')
        answer = prompt.string()

        if answer.isdigit() and int(answer) == correct_answer:
            print('Correct')
            return True
        else:
            print(f"{answer} is wrong answer ;(. Correct answer was {correct_answer}. \nLet's try again, {name}!")
            return False

    for steps in range(3):
        if not game_step():
            break
    else:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()