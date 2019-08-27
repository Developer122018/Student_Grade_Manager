# what is (random question answer?) try making a game but start of as random questions
import random

num_of_runs_1 = []
player_score = 0
minus_while_loop_variable = 0
list_of_operations = ['addition', 'subtraction', 'multiplication', 'division']
print('How many times would you like to play?')
num_of_runs = int(input())

# make sure that the user is playing max of 99 times
if num_of_runs < 100:
    pass
else:
    print('How many times would you like to play? Please choose a number less than 100')
    num_of_runs = int(input())

# num_of_runs = num_of_runs_1
# for x in num_of_runs_1:
# What level of difficulty
game_played_count = 0
while game_played_count < num_of_runs:
    game_played_count = game_played_count + 1

    random_number_1 = random.randrange(1, 100)
    random_number_2 = random.randrange(1, 100)
    random_choice_of_list_of_operations = random.choice(list_of_operations)

    # Process addition
    if random_choice_of_list_of_operations == 'addition':
        print(random_number_1, '+', random_number_2, '=')
        answer = random_number_1 + random_number_2

        # if answer is wrong then give user 3 chances to correct his answer
        # and then give him correct answer
        # mark question correct if user chooses correct answer and increment player_score by 1
        add_while_loop_variable = 0
        while add_while_loop_variable < 3:
            user_answer = int(input())
            if answer == user_answer:
                print('You got it right')
                player_score += 1
                break
            else:
                print('Try again')
                print(random_number_1, '+', random_number_2, '=')
                add_while_loop_variable += 1
        if add_while_loop_variable == 3:
            print('Work on your maths!, correct answer =', answer)


    if random_choice_of_list_of_operations == 'subtraction':
        print(random_number_1 ,'-', random_number_2,'=')
        answer = random_number_1 - random_number_2
        user_answer = int(input())

    while minus_while_loop_variable < 3:
        if answer == user_answer:
            print('You got it right')
            player_score += 1
            break
        else:
            print('Try again')
            print(random_number_1 , '-', random_number_2,'=')
            user_answer = int(input())
            minus_while_loop_variable += 1
    if minus_while_loop_variable == 3:
        print('Work on your maths!, correct answer =', answer)

    if random_choice_of_list_of_operations == 'multiplication':
        print(random_number_1 ,'*', random_number_2,'=')
        answer = random_number_1 * random_number_2
        user_answer = int(input())

    times_while_loop_variable = 0
    while times_while_loop_variable < 3:
        if answer == user_answer:
            print('You got it right')
            player_score += 1
            break
        else:
            print('Try again')
            print(random_number_1 , '*', random_number_2,'=')
            user_answer = int(input())
            minus_while_loop_variable += 1
    if times_while_loop_variable == 3:
        print('Work on your maths!, correct answer =', answer)

    if random_choice_of_list_of_operations == 'division':
        print(random_number_1 ,'/', random_number_2,'=')
        answer = random_number_1 / random_number_2
        user_answer = int(input())

    divide_while_loop_variable = 0
    while divide_while_loop_variable < 3:
        if answer == user_answer:
            print('You got it right')
            player_score += 1
            break
        else:
            print('Try again')
            print(random_number_1 , '/', random_number_2,'=')
            user_answer = int(input())
            minus_while_loop_variable += 1
    if divide_while_loop_variable == 3:
        print('Work on your maths!, correct answer =', answer)

print( 'You have scored',player_score,'out of',num_of_runs,'.Well done!')
#if minus_while_loop_variable == 3:
 #   print('Work on your maths!')