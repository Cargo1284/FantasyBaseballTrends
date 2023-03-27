from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options


def setUpWebsite():
    global broswer
    browser = webdriver.Chrome()

    browser.get("https://www.baseball-reference.com/")

    return browser


def searchPlayer(browser, player):
    searchBox = browser.find_element(By.XPATH, '//*[@id="header"]/div[3]/form/div/div/input[2]')
    searchBox.send_keys(player + Keys.RETURN)

    url = browser.current_url

    return url


def get2023Projected(browser, player):

    # search the player needed
    searchPlayer(browser, player)

    # parse the page to get the projected 2023 stats table and return it
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_proj"})
    table = pd.read_html(str(stats))
    projected = table[0]
    # print(projected)

    # projected.to_csv('AaronJudgeProj.csv')

    return projected


def getLastGame(browser, player):

    # search the player needed
    searchPlayer(browser, player)

    # get to the link for 2022 stats, will have to change once 2023 season starts
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[2]/li[7]/a')
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_gamelogs"})
    table = pd.read_html(str(stats))
    lastGame = table[0].iloc[-2, 3:]
    lastGame = lastGame.to_frame()
    lastGame = lastGame.transpose()

    # print(lastGame.shape)

    return lastGame


def getVsRhpCurrent(browser, player):

    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits, might have to change to get to 2023
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[8]/a')
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # find the table with rhp and return it
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "plato"})
    table = pd.read_html(str(stats))
    statsVsRhp = table[0].iloc[[0, -2]]

    # print(statsVsRhp)

    return statsVsRhp


def getVsLhpCurrent(browser, player):

    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits, might have to change to get to 2023
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[8]/a')
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # find the table with rhp and return it
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "plato"})
    table = pd.read_html(str(stats))
    statsVsLhp = table[0].iloc[[1, -1]]

    # print(statsVsLhp)

    return statsVsLhp


def getCareerSplits(browser, player):

    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits, might have to change to get to 2023
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[1]/a')
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # find the table with rhp and return it
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "plato"})
    table = pd.read_html(str(stats))
    careerSplits = table[0].iloc[[0, -2, 1, -1]]
    # print(careerSplits)

    return careerSplits


def getLastxGames(browser, player, gamesNum):

    # search the player needed
    searchPlayer(browser, player)

    # get to the link for 2022 stats, will have to change once 2023 season starts
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[2]/li[7]/a')
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_gamelogs"})
    table = pd.read_html(str(stats))
    lastxGames = table[0].iloc[-gamesNum - 1 : -1, 3:]

    # print(lastxGames)

    return lastxGames


# work on this part
'''
def getAvgOverLastXGames(browser, player, gamesNum):
    xGames = getLastxGames(browser, player, gamesNum)
    avgXGames = xGames.mean(axis=0,numeric_only=True,skipna=True)

    #print(avgXGames)

    return(avgXGames)
'''


def main():
    # global browser

    # browser = setUpWebsite()

    # browser = webdriver.Chrome()

    # browser.get("https://www.baseball-reference.com/")

    # print("hello")

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # browser = webdriver.Chrome(options=options)

    # browser = webdriver.Chrome()

    # browser.get("https://www.baseball-reference.com/")
    # search = input("Which player to search for: ")

    # print(get2023Projected("Aaron Judge"))
    # getLastGame(browser, search)
    # getVsRhpCurrent(browser, search)
    # getVsLhpCurrent(browser, search)
    # getCareerSplits(browser, search)
    # getAvgOverLastXGames(browser, search, 5)

    # get a save the csv's for aaron judge and mike trout for each function

    # Aaron_Judge = get2023Projected("Aaron Judge")
    # Aaron_Judge.to_csv('AaronJudgeProj.csv')

    # Aaron_Judge = getLastGame("Aaron Judge")
    # Aaron_Judge.to_csv('JudgeLastGame.csv')

    # Aaron_Judge = getVsRhpCurrent("Aaron Judge")
    # Aaron_Judge.to_csv('JudgeRhpCurrent.csv')

    # Aaron_Judge = getVsLhpCurrent("Aaron Judge")
    # Aaron_Judge.to_csv('JudgeLhpCurrent.csv')

    # Aaron_Judge = getCareerSplits("Aaron Judge")
    # Aaron_Judge.to_csv('JudgeCarrerSplits.csv')

    # Aaron_Judge = getLastxGames("Aaron Judge", 5)
    # Aaron_Judge.to_csv('JudgeLast5.csv')

    # Aaron_Judge = getLastxGames("Aaron Judge", 10)
    # Aaron_Judge.to_csv('JudgeLast10.csv')

    # maybe find one that gets the

    return


main()
