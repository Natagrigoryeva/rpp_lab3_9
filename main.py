import http.client
import json

def operate(data: str, left: int):

    dict = json.loads(data)

    if dict['operation'] == 'mul':

        return left * dict['number']

    if dict['operation'] == 'sub':

        return left - dict['number']

    if dict['operation'] == 'div':

        return left / dict['number']

    if dict['operation'] == 'sum':

        return left + dict['number']

#Задание 1: Отправить HTTP запрос GET /number/{Вариант}.

connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request ("GET", "/number/9")
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = json.loads(decoded_body)['number']
print(left)

#Задание 2: Отправить HTTP запрос GET /number/ с параметром запроса option={Вариант}.

connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request('GET', '/number/?option=9')
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = operate(decoded_body, left)
print(left)

#Задание 3: Отправить HTTP запрос POST /number/ с телом option={Вариант}.
connect = http.client.HTTPConnection("167.172.172.227:8000")
headers = {'Content-type': 'application/x-www-form-urlencoded'}
connect.request('POST', '/number/', 'option=9', headers)
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = operate(decoded_body, left)
print(left)

#Задание 4: Отправить HTTP запрос PUT /number/ с телом JSON {"option": {Вариант}}.
connect = http.client.HTTPConnection("167.172.172.227:8000")
headers = {'Content-type': 'application/json'}
connect.request('PUT', '/number/', json.dumps({'option': 9}), headers)
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = operate(decoded_body, left)
print(left)

#Задание 5: Отправить HTTP запрос DELETE /number/ с телом JSON {"option": {Вариант}}.
connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request('DELETE', '/number/', json.dumps({'option': 9}))
response1 = connect.getresponse()
print(response1.status, response1.reason)
decoded_body = response1.read().decode()
left = operate(decoded_body, left)
print(left)
