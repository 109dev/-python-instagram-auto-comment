from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from myid import ID, PW
import time
import random

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://instagram.com')

    time.sleep(2) #페이지 로딩이 느려지면 다음에 실행 될 동작들이 실행이 될 수 없어 에러가 나기때문에 시간이 지체되는 부분에 대기 시간을 넣어줍니다.

    #login
    login_id = driver.find_element_by_name('username')
    login_id.send_keys(ID)
    login_pw = driver.find_element_by_name('password')
    login_pw.send_keys(PW)
    login_pw.send_keys(Keys.RETURN)

    time.sleep(5)

    #pass popup - 로그인 후 피드 페이지에서 팝업창이 따로 나오지 않을경우 아래 부분은 주석하고 바로 해시태그 검색
    popup = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    popup.send_keys(Keys.ENTER)
    time.sleep(3)
    popup = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    popup.send_keys(Keys.ENTER)

    time.sleep(2)

    #searh
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
    search.send_keys('#집냥')
    time.sleep(5)
    search = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]')
    feedCtn = driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div/div/div[2]/span/span').text
    print('검색된 피드 수 : {}'.format(feedCtn))
    search.send_keys(Keys.ENTER)

    time.sleep(3)

    #select first feed
    feed = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]/a')
    feed.send_keys(Keys.ENTER)

    time.sleep(5)

    feedCtn = 10
    comm_list = [
        '귀여워요!',
        '넘 귀여워요!!',
        '잘 보고갑니다!ㅎ',
        '귀여워요!! 잘 보고갑니다!'
    ]
    while True:
        #comment
        comm = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div[1]/form/textarea')
        ran_comm = random.choice(comm_list)

        ac = ActionChains(driver)
        ac.move_to_element(comm)
        ac.click()
        ac.pause(3)
        ac.send_keys(ran_comm)
        ac.pause(1)
        ac.send_keys(Keys.ENTER)
        ac.perform()


        time.sleep(3)

        nextFeed = driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow')
        ac = ActionChains(driver)
        ac.move_to_element(nextFeed)
        ac.click()
        ac.perform()

        if feedCtn == 1:
            break
        time.sleep(1)
except Exception as e:
    print(e)
finally:
    driver.quit()