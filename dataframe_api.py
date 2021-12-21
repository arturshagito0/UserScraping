import gspread
import numpy as np
import pandas as pd
import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import threading






TAGS = 'CEO'

def create_new_spreadsheet(name):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.create(name)
    sh.share('art_shagi@mail.ru', perm_type='user', role='writer')


chromedriver = "chromedriver.exe"


def save_to_google_drive(df, name):
    print("Saving to google...")
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open(name)
    worksheet = sh.add_worksheet(title = f"A new One", rows="10000", cols="20")
    worksheet.update([df.columns.values.tolist()] + df.values.tolist())


def update_spreadsheet(size, df, name, wsname):
    gc = gspread.service_account(filename='creds.json')
    sh = gc.open(name)

    try:
        worksheet = sh.worksheet(wsname)
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())
    except:
        worksheet = sh.add_worksheet(title=f"{name}-{size}", rows="10000", cols="20")
        worksheet.update([df.columns.values.tolist()] + df.values.tolist())




def populate_dataframe(user_list):
    print("Populating dataframe...")
    leads = np.array([])
    for i in user_list:
        leads = np.append(leads, dict(zip(['firstname', 'lastname', 'occupation', 'id'], [i.firstname, i.lastName, i.occupation, i.id])))
    df = pd.DataFrame.from_dict(list(leads), orient = 'columns')
    df['user_url'] = df['id'].apply(lambda x: f"https://www.linkedin.com/in/{x}")

    return df
    


# linked_url = "https://www.linkedin.com/groups/35222/"
#
#
# driver.get(linked_url)
# driver.fullscreen_window()
#
#
# def sign_in(user, passw):
#     time.sleep(3)
#     cookies_button = driver.find_element_by_xpath(
#         '//*[@id="artdeco-global-alert-container"]/div/section/div/div[2]/button[2]')
#     cookies_button.click()
#     time.sleep(3)
#     sign_in_link = driver.find_element_by_xpath('/html/body/div[1]/main/p/a')
#     sign_in_link.click()
#     time.sleep(3)
#     user_field = driver.find_elements_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[1]/input')[0]
#     user_field.send_keys(user)
#     passw_field = driver.find_elements_by_xpath('/html/body/div/main/div[2]/div[1]/form/div[2]/input')[0]
#     passw_field.send_keys(passw)
#     time.sleep(3)
#     sign_in_btn = driver.find_elements_by_xpath('//*[@id="organic-div"]/form/div[3]/button')[0]
#     sign_in_btn.click()
#     try:
#         inside = driver.find_elements_by_xpath('//*[@id="ember48"]/div[1]/h1')
#     except Exception:
#         input("There was a problem logging in, check the browser window pls...")
#         time.sleep(5)
#
# sign_in(login, pwd)
#
# time.sleep(3)
# driver.find_element_by_xpath("/html/body/div[6]/aside/section/header/div[3]/button[2]").click()
# time.sleep(1)
# driver.find_element_by_xpath("//*[@id='ember75']").click()
#
# time.sleep(2)
#
# window_after = driver.window_handles[0]
# driver.switch_to.window(window_after)
#
# time.sleep(4)
#
#
# # search_box = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/main/div/div/div/div[1]/div/div/div/input")
# # search_box.send_keys(TAGS)
# ul_list = driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/div[2]/div/div/main/div/div/div/ul")
#
#
# def scroll_down_page():
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
# while True:
#     scroll_down_page()

# for i in range(10000):
#     if i % 1000:
#
#         list_count = driver.find_element(By.XPATH,
#                                          "/html/body/div[6]/div[3]/div/div[2]/div/div/main/div/div/div/ul").get_attribute("data-count")
#         print(list_count)
#     driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#


#Working ul list parser 
# list = driver.find_element(By.ID, "ember330-a11y")
# 
# items = list.find_elements_by_tag_name("li");
# 
# for li in items:
#     link = li.find_element_by_tag_name("a")
#     print(link.get_attribute("href"))
# 




