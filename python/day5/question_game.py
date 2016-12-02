"""
Create a game that asks the user for 5 modulus questions using a dictionary to
store the questions and answers.

Keep track of the score of how many questions were answered right and how many were
anwered wrong

At the end of the game, print the number of right and wrong and overall percentage.
-----
We're going to create a variable called  modulus_questions.
We're creating a dictionary with 5 right or wrong modulus_questions.
The key will be the question
The value will be the correct answer

We'll create a variable that counts how many correct answers
Create a variable that counts how many wrong answers.

Write a function to determine if the input is True or False.
if user answer is == the question asked then this will return True.

We'll write a function that asks the user a question and asks for input (an answer).
We'll write a function that will check to see if the user's answer is correct or not.


Each question is worth 20 points. (20% each )
1 missed is still passing at 80%



"""
correct_answer_count = 0
wrong_answer_count = 0

modulus_questions = {"What is 2 % 2?": 0, "What is 5 % 2?": 1,
"What is 3 % 2?": 1, "What is 4 % 2?": 0, "What is 6 % 2": 0}

question1 = int(input("Please enter a number answer. What is 2 % 2?"))
if question1 == modulus_questions["What is 2 % 2?"]:
    correct_answer_count += 1
    print("YES!")
    print("You've got", correct_answer_count, "correct!")
else:
    wrong_answer_count += 1
    print("DOH!")
    print(wrong_answer_count)

question2 = int(input("Please enter a number. What is 5 % 2? "))
if question2 == modulus_questions["What is 5 % 2?"]:
    correct_answer_count += 1
    print("YES!")
    print("You've got", correct_answer_count, "correct!")
else:
    wrong_answer_count += 1
    print("DOH!")
    print(wrong_answer_count)

question3 = int(input("Please enter a number. What is 3 % 2? "))
if question3 == modulus_questions["What is 3 % 2?"]:
    correct_answer_count += 1
    print("YES!")
    print("You've got", correct_answer_count, "correct!")
else:
    wrong_answer_count += 1
    print("DOH!")
    print(wrong_answer_count)

question4 = int(input("Please enter a number. What is 4 % 2? "))
if question4 == modulus_questions["What is 4 % 2?"]:
    correct_answer_count += 1
    print("YES!")
    print("You've got", correct_answer_count, "correct!")
else:
    wrong_answer_count += 1
    print("DOH!")
    print(wrong_answer_count)

question5 = int(input("Please enter a number. What is 6 % 2? "))
if question5 == modulus_questions["What is 6 % 2"]:
    correct_answer_count += 1
    print("YES!")
    print("You've got", correct_answer_count, "correct!")
else:
    wrong_answer_count += 1
    print("DOH!")
    print(wrong_answer_count)

percentage_grade = (correct_answer_count/5)*100
print("You answered",correct_answer_count, "correctly!")
print("You answered",wrong_answer_count,"incorrectly!")
print("You got", percentage_grade,"!")
