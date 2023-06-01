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
        elem.send_keys('https://51.159.194.223/tag/1/%D1%81%D0%BB%D1%8D%D1%88%D0%B5%D1%80?__cpo=aHR0cDovL3J1dG9yLmluZm8' + Keys.RETURN)
        time.sleep(8)
        elem = browser.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/center/table/tbody/tr[1]/td[2]/input')
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        elem = browser.find_element(By.XPATH, "/html/body/div[4]/div[2]/div[2]/center/table/tbody/tr[2]/td/input").click()
        elem = browser.find_element(By.XPATH, '/html/body/div[4]/div[1]/div[2]/table/tbody/tr[2]/td[2]/a[3]').click()

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Mlink = soup.find('a', class_='downgif').find('href').text
        Mname = soup.find('div', ).find('a').get('href')
        print(Media_name, Media_link)
        return Media_name[:], Media_link
    except:
        print('Fatal Error')
        return 'напишите запрос правильно'

async def result4():
    try:
        browser = webdriver.Chrome(executable_path=r'D:\KargASS\Utorrent_Edition\Chrome\chromedriver.exe')
        browser.get('https://www.croxyproxy.com/')
        assert 'Free' in browser.title

        res1 = cur.execute("""SELECT name FROM Games;""")
        res = res1.fetchall()
        elem = browser.find_element(By.ID, 'url')  # Find the search box
        elem.send_keys('thepiratebay.org' + Keys.RETURN)
        time.sleep(8)
        elem = browser.find_element(By.XPATH, '/html/body/main/section/form/div[2]/span[5]/label/input').click()
        elem = browser.find_element(By.XPATH, '/html/body/main/section/form/div[1]/input')
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/main/div[2]/section[2]/ol/li[2]/span[2]/a').click()

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Mname = soup.find('section', class_='col-center').find('label').text
        Mlink = soup.find('div', class_='links').find('a').get('href')
        print(Media_name, Media_link)
        return Media_name[:], Media_link

    except:
          print('Fatal Error')
          return 'перезапустите бота и попробуйте ввести запрос подругому'

async def result5():
    try:
        browser = webdriver.Chrome(executable_path=r'D:\KargASS\Utorrent_Edition\Chrome\chromedriver.exe')
        browser.get('https://www.croxyproxy.com/')
        assert 'Free' in browser.title

        res1 = cur.execute("""SELECT name FROM Games;""")
        res = res1.fetchall()
        elem = browser.find_element(By.ID, 'url')  # Find the search box
        elem.send_keys('rutraker.org' + Keys.RETURN)
        time.sleep(8)
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td/div/a[2]/b').click()
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td/div/div/form[2]/input[1]')
        elem.send_keys('tester356654'+ Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td/div/div/form[2]/input[2]')
        elem.send_keys('sc67Ui192sdL'+ Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td/div/div/form[2]/input[3]').click()
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/form/input[2]')
        elem.send_keys(str(res[0][0]) + Keys.RETURN)
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[1]/div[3]/table/tbody/tr/td[2]/div/form/input[3]').click()
        elem = browser.find_element(By.XPATH, '/html/body/div[6]/div[1]/div[3]/table/tbody/tr/td/div/div[1]/table/tbody/tr[1]/td[4]/div[1]/a').click()

        page = browser.page_source
        soup = BeautifulSoup(page, "html.parser")
        Mname = soup.find('ul', class_='inlined middot-separated').find('a').get('href')
        Mlink = soup.find('span', class_='post-align').find('span').get('__cpp')
        print(Media_name, Media_link)
        return Media_name[:], Media_link





