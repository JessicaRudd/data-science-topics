# ## Classes
# class User:
    
#     def __init__(self, user_id, username) -> None:
#         # initialize starting values for attributes
#         self.user_id = user_id
#         self.username = username
#         # setting an attribute with a default value
#         self.followers = 0
#         self.following = 0
#     # Add methods aka functions
#     # user follows another user - their following count increases by 1, and the other users follower count increases by 1
#     def follow(self, user):
#         user.followers += 1
#         self.following += 1


# user_1 = User("001", "jessica")
# user_2 = User("002", "adam")

# print(user_1.username)

# user_1.follow(user_2)
# print(user_1.followers)
# print(user_1.following)

# print(user_2.followers)
# print(user_2.following)

# Trivia game - could use open trivia database https://opentdb.com/

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")

