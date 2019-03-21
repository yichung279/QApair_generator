store = {
    '小茂屋': {
        'adj': ['長榮路上的', ''],
        'time': '10:00-20:00',
        'loc': '長榮路',
        'tel': '09xxxxxxxx',
        'comment': ['第一句', '第二句']
    }, 
    '再發號': {
        'adj': ['百年老店', ''],
        'time': '10:00-20:00',
        'loc': '??路',
        'tel': '06xxxxxxxx',
        'comment': ['第三句', '第四句']
    }
}

heads = ['你好，', '請問', '']

def timeQ_template (head, adj, store):
    return [
    head + adj + store + '的營業時間是什麼時候',
    head + adj + store + '什麼時候營業',
    head + '什麼時候是' + adj + store + '的營業時間',
    head + '什麼時候' + adj + store + '有營業',
    head + adj + store + '什麼時候有開',
    ]

def timeA_template (adj, store, time):
    return [
    adj + store + time + '都有營業',
    adj + store + time + '有開',
    adj + store + '的營業時間是' + time ,
    time +adj + ',' + store + '都有開'
    ]

def gen_QA(Qlist, Alist):
    QApair = []
    for Q in Qlist:
        for A in Alist:
            QApair.append([Q, A])
    return QApair

if __name__ == "__main__":
    for v in store.keys():
        print(v+':')
        Qlist=[]
        Alist=[]
        for head in heads:
            for adj in store[v]['adj']:
                Qlist.extend(timeQ_template(head, adj, v)),
                Alist.extend(timeA_template(adj, v, store[v]['time']))
        print(len(gen_QA(Qlist, Alist)))
