store = {
    '小茂屋': {
        'adjs': ['長榮路上的', ''],
        'time': '10:00-20:00',
        'loc': '長榮路',
        'tel': '09xxxxxxxx',
        'comments': ['', '第一句', '第二句']
    }, 
    '再發號': {
        'adjs': ['百年老店', ''],
        'time': '10:00-20:00',
        'loc': '??路',
        'tel': '06xxxxxxxx',
        'comments': ['', '第三句', '第四句']
    }
}

heads = ['請問', '']

def timeQ_template (heads, adj, store):
    question = []
    for head in heads:
        for adj in adjs:
            question.append(head + adj + store + '的營業時間是什麼時候?')
            question.append(head + adj + store + '什麼時候營業?')
            question.append(head + '什麼時候是' + adj + store + '的營業時間?')
            question.append(head + '什麼時候' + adj + store + '有營業?')
            question.append(head + adj + store + '什麼時候有開?')
    return question

def timeA_template (adj, store, time):
    answer = []
    for adj in adjs:
        answer.append(adj + store + time + '都有營業。')
        answer.append(adj + store + time + '有開。')
        answer.append(adj + store + '的營業時間是' + time + '。')
        answer.append(time +adj + ',' + store + '都有開。')
    return answer

def gen_QA(Qlist, Alist, comments):
    QApair = []
    for Q in Qlist:
        for A in Alist:
            for comment in comments:
                QApair.append([Q, A+comment])
    return QApair

if __name__ == "__main__":
    for v in store.keys():
        print(v+':')
        adjs = [adj for adj in store[v]['adjs']]
        Qlist = timeQ_template(heads, adjs, v)
        Alist = timeA_template(adjs, v, store[v]['time'])
        print(len(gen_QA(Qlist, Alist, store[v]['comments'])))
