# Эксплуатация веб-уязвимостей в owasp juice-shop и их автоматизация с помощью python

1. DOM-XSS-keylogger - скрипт работает с javascript'ом на сайте, вводит payload и переходит на страницу авторизации. Каждый ввод пользователя с клавиатуры пересылается на удалённый сервер node.js

   Видео демонстрации работы скрипта:

https://github.com/user-attachments/assets/9f86631a-509e-4601-9f88-fd3fbcff320e

2. SQL-injection - скрипт работает с запросами http, вставляет payload, сохраняет базу данных и записывает данные из неё в формате email:hash

   Видео демонстрации работы скрипта:

https://github.com/user-attachments/assets/f00c026a-52df-46b5-942f-ac894ab250df

