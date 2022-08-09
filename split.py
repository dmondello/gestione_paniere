def print_hi(name):
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('Daniele')


sentence1 ='"Il vettore che unisce l’origine del sistema di riferimento col punto in moto","Il versore della tangente alla traiettoria nella posizione del punto in moto","Il versore della perpendicolare alla traiettoria nella posizione del punto in moto","Il vettore che collega due posizioni diverse del punto in moto sulla traiettoria."'
sentence2='"È costante in direzione e verso, ma il modulo varia nel tempo","È variabile in modulo, direzione e verso","È costante in modulo, direzione e verso","È costante in modulo, ma direzione e verso variano nel tempo"'
sentence3='"3 metri","72 metri","2 metri",' \
          '"20 metri"'

answer_1_b = (sentence1.split('","')[0])
answer_1 = answer_1_b + '"'

answer_2_b = (sentence1.split('","')[1])
answer_2 = '"'+ answer_2_b + '"'

answer_3_b = (sentence1.split('","')[2])
answer_3 = '"'+ answer_3_b + '"'

sentence3=' \
          "3 metri","72 metri","2 metri",' '"20 metri"'
#add backspaces to sentence3
sentence3 = sentence3.replace('"', '"\b')
print(sentence3)



answer_4_b = (sentence1.split('","')[3])
answer_4 = '"'+ answer_4_b + '"'

#print(answer_1)
#print(answer_2)
#print(answer_3)
#print(answer_4)
