def quizGame():
    point = 0
    print("Qustion No : 01")
    print("Who is the creator of Python?")
    userAns1 = input("Answer: ")
    userAnsUpdate = userAns1.lower()
    if userAnsUpdate == "guido van rossum":
        print("Correct Answer")
        point = point + 1
        print("Your point: ", point)
    else:
        print("Incorrect Answer")
    print("Qustion No : 02")
    print("What is the most popular programming language?")
    userAns1 = input("Answer: ")
    userAnsUpdate = userAns1.lower()
    if userAnsUpdate == "python":
        print("Correct Answer")
        point = point + 1
        print("Your point: ", point)
    else:
        print("Incorrect Answre")
quizGame()