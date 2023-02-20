from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.options import Options
import requests



def searchPlayer(browser, player):
    searchBox = browser.find_element(By.XPATH, '//*[@id="header"]/div[3]/form/div/div/input[2]')
    searchBox.send_keys(player + Keys.RETURN)  



def get2023Projected(browser, player):
    searchPlayer(browser, player)
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_proj"})
    table = pd.read_html(str(stats))
    projected = table[0]
    print(projected)

    return projected
    

def getLastGame(browser, player):
    
    #search the player needed
    searchPlayer(browser, player)

    #get to the link for 2022 stats, will have to change once 2023 season starts
    link = browser.find_element(By.XPATH, '//*[@id="bottom_nav_container"]/ul[2]/li[7]/a')
    statsLink = link.get_attribute('href')
    
    #load the new page
    browser.get(statsLink)

    #get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_gamelogs"})
    table = pd.read_html(str(stats))
    lastGame = table[0].iloc[-2]
    print(lastGame)

    return lastGame
  

    

def getVsRhp():

    return

def getVsLhp():

    return

def getTable(browser, statsTable):
    html = browser.statsTable.page_source
    table = pd.read_html(html)
    df = table
    print(df)


def main():

    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # browser = webdriver.Chrome(options=options)

    browser = webdriver.Chrome()

    browser.get("https://www.baseball-reference.com/")
    search = input("Which player to search for: ")
    
    #get2023Projected(browser, search)
    getLastGame(browser, search)

main()