from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
	question_text=question["text"]
	question_answer=question["answer"]
	question_object=Question(question_text,question_answer)
	question_bank.append(question_object)

quiz=QuizBrain(question_bank)
quiz.next_question()