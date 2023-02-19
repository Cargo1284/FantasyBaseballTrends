from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd
from bs4 import BeautifulSoup



def searchPlayer(browser, player):
    searchBox = browser.find_element(By.XPATH, '//*[@id="header"]/div[3]/form/div/div/input[2]')
    searchBox.send_keys(player + Keys.RETURN)  



def get2023Projected(browser, player):
    searchPlayer(browser, player)
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_proj"})
    tables = pd.read_html(str(stats))
    print(tables)
    

def getLastGame(browser, player):
    searchPlayer(browser, player)
    

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

    
    browser = webdriver.Chrome()
    browser.get("https://www.baseball-reference.com/")
    search = input("Which player to search for: ")
    #searchPlayer(browser, search)
    get2023Projected(browser, search)
    #stats = input("Which stats do you want to see from: " + searchPlayer +
                    #"\n 1. 2022 Stats \n 2. 2023 projected stats \n 3. Career stats \n 4. Last game stats \n ")
    #get2023Projected(browser, searchPlayer)
    #getTable(browser)

main()