import json
with open('final_answers.json') as file:
    data = json.load(file)
    
    
q = []
a = []
qa = {}
for k in data:
    for j in data[k]:
        qa[data[k][j]['question']] = data[k][j]['answer']
        #q.append(data[k][j]['question'])
        #a.append(data[k][j]['answer'])

qna = {}
for q, a in qa.items():
    print('---Question---')
    print(q)
    print('===Answer===')
    print(a)
    print()
    print()
    inp = input('respond with y / n:      ')
    
    count = 0
    
    while inp not in ['y', 'n']:
        print('incorrect input')
        print('current input is ' + inp)
        print('respond with y /n')
        inp = input()
    
    if inp in ['y', 'n']:
        qna[count] = {}
        qna[count]['q'] = q
        qna[count]['a'] = a
        qna[count]['desir'] = inp
        count += 1
    print()
    print()
    print()
    print()

with open('final_final.txt') as fp:
    fp.write(qna)