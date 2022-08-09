def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

if __name__ == '__main__':
    print_hi('Daniele')

# import paniere
with open('paniere_old.txt', 'r') as f:
    paniere = f.read()
    sentence = paniere.split('QUESTION')[1].split(' Section: (none) Explanation')[0]

# define correct answer
correct_answer = sentence.split('Correct Answer: ')[1][0]
answer_to_delete = 'Correct Answer: ' + correct_answer
sentence = sentence.replace(answer_to_delete, '')

# define question and answers
question = (sentence.split('\n')[1])
sentence = sentence.replace(question, '')

# delete every whitspaces in sentence before first character
sentence = sentence.lstrip()
print(sentence)

answer_1_b = (sentence.split('","')[0])
answer_1 = answer_1_b

answer_2_b = (sentence.split('","')[1])
answer_2 = '"' + answer_2_b

answer_3_b = (sentence.split('","')[2])
answer_3 = '"' + answer_3_b

answer_4_b = (sentence.split('","')[3])
answer_4_c = '"' + answer_4_b
answer_4 = answer_4_c[:-1]

print(answer_1)
print(answer_2)
print(answer_3)
print(answer_4)

if correct_answer == 'A':
    with open('paniere_new.txt', 'a') as d:
        d.write("question = \"" + question + "\"\n")
        d.write("answers = [" + answer_1 + '"]\n')
        d.write("alternatives = [" + answer_2 + '",' + answer_3 + '",' + answer_4 + '"]\n\n')

if correct_answer == 'B':
    with open('paniere_new.txt', 'a') as d:
        d.write("question = \"" + question + "\"\n")
        d.write("answers = [" + answer_2 + '"]\n')
        d.write("alternatives = [" + answer_1 + '",' + answer_3 + '",' + answer_4 + ']\n\n')

if correct_answer == 'C':
    with open('paniere_new.txt', 'a') as d:
        d.write("question = \"" + question + "\"\n")
        d.write("answers = [" + answer_3 + '"]\n')
        d.write("alternatives = [" + answer_1 + '",' + answer_2 + '",' + answer_4 + ']\n\n')

if correct_answer == 'D':
    with open('paniere_new.txt', 'a') as d:
        d.write("question = \"" + question + "\"\n")
        d.write("answers = [" + answer_4 + ']\n')
        d.write("alternatives = [" + answer_1 + '",' + answer_2 + '",' + answer_3 + '"]\n\n')

'''
print(sentence + '\n')
print(correct_answer + '\n')
print(question + '\n')
print(answer_1 + '\n')
print(answer_2 + '\n')
print(answer_3 + '\n')
print(answer_4 + '\n')
'''

with open('paniere_old.txt', 'r') as f:
    paniere = f.read()
    sentence = paniere.split('QUESTION')[1].split(' Section: (none) Explanation')[0]
    paniere_a = paniere.replace(sentence, '')
    paniere_b = paniere_a.replace("QUESTION Section: (none) Explanation", '')
    paniere_c = paniere_b .replace("Explanation/Reference:", '')


with open('paniere_old.txt', 'w') as f:
    new_paniere = paniere_c
    f.write(new_paniere)
