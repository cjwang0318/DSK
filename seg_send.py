# conda install requests
import requests
import time
import json

def seg(lst,server_IP):
    query = {"sentences": lst, "dictionary": "None"}
    sendMessage_json = json.dumps(query)

    # sent json to server
    res = requests.post('http://' + server_IP + '/getResult', json=sendMessage_json)

    if res.ok:
        outputs = res.json()
        # for line in outputs:
        #     print(line)
    else:
        print("segmentation abnormal return, please have check")
    return outputs

if __name__ == '__main__':
    lst = ["全效清爽保濕凝凍150ml", "妮維雅q10plus美體緊膚乳液400ml"]
    query = {"sentences": lst, "dictionary": "None"}
    sendMessage_json = json.dumps(query)
    # print(sendMessage_json)

    start = time.time()
    # sent json to server
    res = requests.post('http://192.168.50.29:5000/getResult', json=sendMessage_json)

    if res.ok:
        outputs = res.json()
        for line in outputs:
            print(line)
    else:
        print("Abnormal return, please have check")
    end = time.time()
    print('time: ', end - start)
