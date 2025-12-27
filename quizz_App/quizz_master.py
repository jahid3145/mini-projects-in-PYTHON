# Features of QuizzMaster
'''
1. Welcome screen with app name and instructions
2. Predefined set of multiple-choice questions
3. User answers with A,B,C or D
4. Correct and worng answers checking
5. Score calculation
6. Display totoal score and percentage
7. Performance feedback (Excellent / Good / practice more)
8. Option to play again(replay feature)
'''

def quiz():
    questions= [
       {
           "question": "Which language is known as the 'mother of all programming languages'?",
           "options": ["A. C", "B. Python", "C. Java", "D. Assembly"],
           "answer": "A"  
        },
       {
           "question": "Which keyword is used to define a function in Python?",
           "options": ["A. function", "B. def", "C. fun", "D. define"],
           "answer": "B"
        },
       {
          "question": "Which data type is used to store multiple values in a single variable?",
          "options": ["A. int", "B. float", "C. list", "D. string"],
          "answer": "C"
        },
       {
           "question": "What is the correct file extension for Python files?",
           "options": ["A. .py", "B. .python", "C. .pt", "D. .p"],
           "answer": "A"
        } ,
       {
           "question": "Which symbol is used for comments in Python?",
           "options": ["A. //", "B. /* */", "C. #", "D. <!-- -->"],
           "answer": "C"
        },
       {
           "question": "Which built-in function returns the length of a list?",
           "options": ["A. count()", "B. size()", "C. length()", "D. len()"],
           "answer": "D"
        }

     ]
    
    score =0
    print("Welcome to the quizeMaster\n")
    print('Answer the questions by just typing A,B,C or D\n')
    
    for i ,q in enumerate(questions,start=1):
        print(f'{i}: {q['question']}')
        
        for option in q['options']:
            print(option)
        
        answer = input("Enter your Answer:").strip().upper()
        
        if answer == q['answer']:
            print('correct\n')
            score = score +1
        else:
            print(f" wrong! correct Answer is :{q['answer']}\n")
    total = len(questions)
    print(f'Quiz over! You Scored:{score}/{total}')
    
    percentage = (score/total) * 100
    
    print(f"your Percentage is :{percentage:.2f}%")
    
    if percentage == 100:
        print("Excellent")
    elif percentage >=60:
        print("Good Job")
    else:
        print('Keep Practicing!')
    
    retry = input('\n Do you want to play again?(yes/no)').lower()
    
    if retry == 'yes':
        quiz()
quiz()
        
