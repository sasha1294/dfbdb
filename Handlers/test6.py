from database.test1 import *
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

async def result():
    try:
        browser = webdriver.Chrome(executable_path=r'D:\KargASS\Utorrent_Edition\Chrome\chromedriver.exe')
        browser.get('https://www.croxyproxy.com/')
        assert 'Free' in browser.title

        res1 = cur.execute("""SELECT name FROM Games;""")
        res = res1.fetchall()

        elem = browser.find_element(By.ID, 'url')  # Find the search box
        elem.send_keys('torrent-games.net' + Keys.RETURN)
        time.sleep(8)
        print(browser.title)
        elem = browser.find_element(By.ID, 'ajax_search')  # Find the search box
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, 'poster-item').click()
        time.sleep(2)

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Game_name = soup.find('h1', class_="flex-grow-1").text
        Game_poster = soup.find('div', class_="page__poster img-fit-cover").find('img').get("src")
        Game_attribute = soup.find('ul', class_="page__list").text
        Game_link = soup.find('a', class_="iksweb").get("__cporiginalvalueofhref")
        print(f"{'https://torrent-games.net' + Game_poster}\n{Game_name}{Game_attribute}{Game_link}")

        return Game_name,\
               Game_poster,\
               Game_attribute,\
               Game_link
    except:
        print("ERROR")
        return 'попробуйте снова'

async def result2():
    try:
        browser = webdriver.Chrome(executable_path=r'D:\KargASS\Utorrent_Edition\Chrome\chromedriver.exe')
        browser.get('https://www.croxyproxy.com/')
        assert 'Free' in browser.title

        res1 = cur.execute("""SELECT name FROM Games;""")
        res = res1.fetchall()
        elem = browser.find_element(By.ID, 'url')  # Find the search box
        elem.send_keys('thepiratebay.org' + Keys.RETURN)
        time.sleep(8)
        elem = browser.find_element(By.XPATH, '/html/body/main/section/form/div[2]/span[3]/label/input').click()
        elem = browser.find_element(By.XPATH, '/html/body/main/section/form/div[1]/input')
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ol/li[2]/span[2]/a').click()

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Media_name = soup.find('section', class_='col-center').find('label').text
        Media_link = soup.find('div', class_='links').find('a').get('href')
        print(Media_name, Media_link)
        return Media_name[:], Media_link
    except:
        print('Fatal Error')
        return 'перезапустите бота и попробуйте ввести запрос подругому'


async def result3():
    try:
        browser = webdriver.Chrome(executable_path=r'D:\KargASS\Utorrent_Edition\Chrome\chromedriver.exe')
        browser.get('https://www.croxyproxy.com/')
        assert 'Free' in browser.title

        res1 = cur.execute("""SELECT name FROM Games;""")
        res = res1.fetchall()
        elem = browser.find_element(By.ID, 'url')  # Find the search box
        elem.send_keys('thepiratebay.org' + Keys.RETURN)
        time.sleep(8)
        elem = browser.find_element(By.XPATH, "/html/body/main/section/form/div[2]/span[2]/label").click()
        elem = browser.find_element(By.XPATH, '/html/body/main/section/form/div[1]/input')
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ol/li[2]/span[2]/a').click()

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Songs_name = soup.find('section', class_='col-center').find('label').text
        Songs_link = soup.find('div', class_='links').find('a').get('href')
        print(Songs_name, Songs_link)
        return Songs_name[:], Songs_link
    except:
        print('Fatal Error')
        return 'перезапустите бота и попробуйте ввести запрос подругому'
