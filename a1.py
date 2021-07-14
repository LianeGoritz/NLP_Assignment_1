import nltk
import re

nltk.download('punkt')

from nltk import word_tokenize
from nltk.stem import PorterStemmer

stemmer = PorterStemmer()

f1 = open('script.in')
script = f1.read()
script_tokens = word_tokenize(script)
script_tokens_stemmed = list()

f2 = open('question.in')
question = f2.read()
question_tokens = word_tokenize(question)
question_blanks = list()

f3 = open('answer.in')
answer = f3.read()
answer_tokens = word_tokenize(answer)

script_answer_tokens = list()
index = 0
points = 0

for i in script_tokens:
    script_tokens_stemmed.append(stemmer.stem(i))

for word in question_tokens:
    match = re.match('[_]+', word)

    if match:
        question_blanks.append(index)

    index = index + 1

for i in range(0,len(script_tokens_stemmed)):
    for blank_index in question_blanks:
        if i == blank_index:
            script_answer_tokens.append(script_tokens_stemmed[i])

print('------Results------')


if len(script_answer_tokens) == len(answer_tokens):
    for i in range(0, len(answer_tokens)):
        full_match = re.fullmatch(script_answer_tokens[i], answer_tokens[i])

        if full_match:
            print('Student Answer: ', script_answer_tokens[i], '   Correct Answer: ', answer_tokens[i], '   Points Rewarded: 1')
            points = points + 1
        else:
            print('Student Answer: ', script_answer_tokens[i], '   Correct Answer: ', answer_tokens[i], '   Points Rewarded: 0')
print('-------------------')
print('Total number of points rewarded: ', points)
