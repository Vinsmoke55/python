from data import question_data
from question_model import Question

question_bank=[]

for question in question_data:
	question_text=question["text"]
	question_answer=question["answer"]
	question_object=Question(question_text,question_answer)
	question_bank.append(question_object)

print(question_bank)