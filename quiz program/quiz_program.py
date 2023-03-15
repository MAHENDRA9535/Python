quiz = {
    'question 1': {
        'question': 'what is the capital city of INDIA',
        'answer': 'DELHI'
    }, 'question 2': {
        'question': 'what is the capital city of GERMANY',
        'answer': 'BERLIN'
    }, 'question 3': {
        'question': 'what is the capital city of SWIZERLAND',
        'answer': 'SWIZ'
    }, 'question 4': {
        'question': 'what is the capital city of Karnataka',
        'answer': 'Bengaluru'
    }, 'question 5': {
        'question': 'what is the capital city of maharastra',
        'answer': 'pune'
    }

}
score = 0

for key, value in quiz.items():
    print(value['question'])
    answer = input('answer?')

    if (answer.lower() == value['answer'].lower()):
        print("correct")
        score += 1
        print("score", score)
        print("")
        print("")

    else:
        print("wrong")
        print("the answer is", value['answer'])
        print("score", score)
        print("")
        print("")

print("your score is", score, "out of 5 questions")
