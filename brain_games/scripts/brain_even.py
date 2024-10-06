from random import randint

def main():
    print('May I have your name?')
    name = input()

    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    def game_step():
        number_in_question = randint(1, 999)
        print(f'Question: {number_in_question} Your answer?')
        answer = input()
    
        if number_in_question % 2 == 0 and answer == 'yes':
            print('Correct')
            return True
        elif number_in_question % 2 == 0 and answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
            return False
        elif number_in_question % 2 != 0 and answer == 'no':
            print('Correct')
            return True
        elif number_in_question % 2 != 0 and answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\n Let's try again, {name}!")
            return False
        else:
            print(f'That is not a valid answer, sorry, {name}')
            return False

    for steps in range(3):
        if not game_step():
            break
    else:
        print(f'Congratulations, {name}!')

if __name__ == "__main__":
    main()