import http.client
import json


# Задание 1. Ответ: {"number":56}, Первое число: 56
connect = http.client.HTTPConnection("167.172.172.227:8000")
connect.request("GET", "/number/9")
response1 = connect.getresponse()
decoded_body = response1.read().decode()
print(decoded_body)
json_decoded_body = json.loads(decoded_body)
first = json_decoded_body["number"]
print('Первое число:', first)

# Задание 2. Ответ:{"operation":"mul","number":17}, Второе число: 17, Умножение: 952
connect.request("GET", "/number/?option=9")
response2 = connect.getresponse()
decoded_body_1 = response2.read().decode()
print(decoded_body_1)
json_decoded_body_1 = json.loads(decoded_body_1)
second = json_decoded_body_1["number"]
print('Второе число:', second)
print('Умножение:', int(first * second))

# Задание 3. Ответ: {"operation":"sub","number":82}, Третье число:  82, Вычитание: 65
headers = {'Content-type': 'application/x-www-form-urlencoded'}
connect.request("POST", "/number/", "option=9", headers)
response3 = connect.getresponse()
decoded_body_2 = response3.read().decode()
print(decoded_body_2)
json_decoded_body_2 = json.loads(decoded_body_2)
third = json_decoded_body_2["number"]
print('Третье число: ', third)
print('Вычитание:', int(third - second))

# Задание 4. Ответ: {"operation":"div","number":29}, Четвертое число:  29, Деление:  2
headers = {'Content-type': 'application/json'}
body = {'option': 9}
connect.request("PUT", "/number/", json.dumps(body), headers)
response4 = connect.getresponse()
decoded_body_3 = response4.read().decode()
print(decoded_body_3)
json_decoded_body_3 = json.loads(decoded_body_3)
fourth = json_decoded_body_3["number"]
print('Четвертое число: ', fourth)
print('Деление: ', int(third / fourth))

# Задание 5. Ответ: {"operation":"sum","number":7}, Пятое число:  7, Сумма:  36
headers = {'Content-type': 'application/json'}
body = {'option': 9}
connect.request("DELETE", "/number/", json.dumps(body), headers)
response5 = connect.getresponse()
decoded_body_4 = response5.read().decode()
print(decoded_body_4)
json_decoded_body_4 = json.loads(decoded_body_4)
fifth = json_decoded_body_4["number"]
print('Пятое число: ', fifth)
print('Сумма: ', int(fourth + fifth))
