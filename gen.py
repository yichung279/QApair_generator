import json
import random
with open('data.json', 'r') as file1:
    store = json.loads(file1.read())


heads = ['請問', '']

def timeQ_template (heads, adj, store):
    question = []
    for head in heads:
        for adj in adjs:
            question.append(f'{head}{adj}{store}的營業時間是什麼時候?')
            question.append(f'{head}{adj}{store}什麼時候營業?')
            question.append(f'{head}什麼時候是{adj}{store}的營業時間?')
            question.append(f'{head}什麼時候{adj}{store}有營業?')
            question.append(f'{head}{adj}{store}什麼時候有開?')
    return question

def timeA_template (adj, store, time):
    answer = []
    for adj in adjs:
        answer.append(f'{adj}{store}{time}都有營業。')
        answer.append(f'{adj}{store}{time}有開。')
        answer.append(f'{adj}{store}的營業時間是{time}。')
        answer.append(f'{time}{adj}，{store}都有開。')
    return answer

def locationQ_template(heads, adj, store):
    question = []
    for head in heads:
        for adj in adjs:
            question.append(f'{head}{adj}{store}在哪裡？')
            question.append(f'{head}我該怎麼去{adj}{store}？')
            question.append(f'{head}{adj}{store}怎麼走?')
    return question

def locationA_template (adj, store, location):
    answer = []
    for adj in adjs:
        answer.append(f'{adj}{store}的營業地點在{location}。')
        answer.append(f'{adj}{store}在{location}。')
        answer.append(f'{adj}{store}開在{location}。')
        answer.append(f'在{location}就能找到{adj}{store}。')
    return answer


def gen_QA(Qlist, Alist, comments):
    QApair = []
    for Q in Qlist:
        for A in Alist:
            for comment in comments:
                if random.randint(1, 100) % 2:
                    QApair.append([Q, A + comment])
                else:
                    QApair.append([Q, comment + '，' + A])
    return QApair

if __name__ == "__main__":
    for v in store.keys():
        print(v+':')
        adjs = [adj for adj in store[v]['adjs']]
        #Qlist = timeQ_template(heads, adjs, v)
        #Alist = timeA_template(adjs, v, store[v]['time'])
        Qlist = locationQ_template(heads, adjs, v)
        Alist = locationA_template(adjs, v, store[v]['loc'])
        print(len(gen_QA(Qlist, Alist, store[v]['comments'])))
        #print(gen_QA(Qlist, Alist, store[v]['comments']))
