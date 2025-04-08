import random
def generate_question():
    num1=random.randint(1,10)
    num2=random.randint(1,10)
    operation=random.choice("+","-","*")
    if operation == "+":
        correct_answer=num1+num2
    elif operation == "-":
        correct_answer=num1-num2
    else:
        correct_answer=num1*num2
    return f"What is {num1} {operation} {num2}?",correct_answer
def math_quiz():
    print("🧿🧿🧿Welcome to the iconic world,So Lets attend a quiz on Mathametics🔮🔮")
    score=0
    total_questions=5
    for i in range(total_questions):
        question,correct_answer=generate_question()
        print(f"\n Question {i+1}: {question}")
        try:
            user_answer=int(input("Your answer: "))
            if user_answer==correct_answer:
            print("Correct✔✔✔✔✔✔")
            score+=1
        else:
            print(f"Oops,The answer is Wrong!❌❌❌❌")
        except ValueError:
                print("Please Enter a Number")
    print(f"\n You Got {score} out of {total_questions} correct!")
if __name__ == "__main__":
    math_quiz()