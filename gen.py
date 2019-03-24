import json
import random
import xlsxwriter

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

def phoneQ_template(heads, adj, store):
    question = []
    for head in heads:
        for adj in adjs:
            question.append(f'{head}{adj}{store}的電話是幾號？')
            question.append(f'{head}我該怎麼聯絡{adj}{store}？')
            question.append(f'{head}{adj}{store}電話多少?')
    return question

def phoneA_template (adj, store, phone):
    answer = []
    for adj in adjs:
        answer.append(f'{adj}{store}的電話是{phone}。')
        answer.append(f'打{phone}就能聯絡到{adj}{store}。')
        answer.append(f'{phone}是{adj}{store}的電話。')
    return answer

def select(pair, num):
    random.shuffle(pair)
    return pair[:num]

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
    QApair = []
    for v in store.keys():
        adjs = [adj for adj in store[v]['adjs']]
        Qlist = timeQ_template(heads, adjs, v)
        Alist = timeA_template(adjs, v, store[v]['time'])
        QApair += select(gen_QA(Qlist, Alist, store[v]['comments']), 34)

        Qlist = locationQ_template(heads, adjs, v)
        Alist = locationA_template(adjs, v, store[v]['loc'])
        QApair += select(gen_QA(Qlist, Alist, store[v]['comments']), 33)

        Qlist = phoneQ_template(heads, adjs, v)
        Alist = phoneA_template(adjs, v, store[v]['phone'])
        QApair += select(gen_QA(Qlist, Alist, store[v]['comments']), 33)
    random.shuffle(QApair)
    with xlsxwriter.Workbook('QA.xlsx') as workbook:
        worksheet = workbook.add_worksheet()
        for i, v in enumerate(QApair):
            worksheet.write(i, 0, v[0])
            worksheet.write(i, 1, v[1])
    

