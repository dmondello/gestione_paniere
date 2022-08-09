def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Daniele')


# open "domande.txt",delete all rows until "Explanation/Reference"
with open('paniere_old.txt', 'r') as f:
    paniere = f.read()
    sentence = paniere.split('QUESTION')[1].split(' Section: (none) Explanation')[0]
    complete_sentence_a = paniere.replace(sentence, '')
    complete_sentence_b = complete_sentence_a.replace("QUESTION Section: (none) Explanation", '')
    complete_sentence = complete_sentence_b.replace("Explanation/Reference:", '')
    print(complete_sentence)

with open('paniere_old.txt', 'w') as f:
    new_paniere = complete_sentence
    f.write(new_paniere)



