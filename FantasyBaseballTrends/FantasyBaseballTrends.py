import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def setUpWebsite():
    """
    Before using any function in this library, run this first to set up the website!
    This function sets up baseball-reference and returns the browser.

    """
    global broswer
    browser = webdriver.Chrome()

    browser.get("https://www.baseball-reference.com/")

    return browser


def searchPlayer(browser, player):
    """A function to search for a given player on the website.

    Args:
        browser (webdriver): the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        Url of the players home stats page

    """
    searchBox = browser.find_element(
        By.XPATH, '//*[@id="header"]/div[3]/form/div/div/input[2]'
    )
    searchBox.send_keys(player + Keys.RETURN)

    url = browser.current_url

    return url


def get2023Season(browser, player):
    """
    A function that retrieves the current 2023 Stats for a player.
    Returns a pandas DataFrame that contains the information from the 2023 stats table on baseball-reference.

    Args:
        browser : the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains the season stats

    """
    # search the player needed
    searchPlayer(browser, player)

    # parse the page to get the projected 2023 stats table and return it
    # soup = BeautifulSoup(browser.page_source, features="lxml")
    # stats = soup.find("table", {"id": "batting_proj"})
    # table = pd.read_html(str(stats))
    # projected = table[0]
    # # print(projected)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_standard"})
    table = pd.read_html(str(stats))
    seasonStats = table[0].iloc[-3, 3:]
    seasonStats = seasonStats.to_frame()
    seasonStats = seasonStats.transpose()

    # projected.to_csv('AaronJudgeProj.csv')

    return seasonStats


def getCareer(browser, player):
    """
    A function that retrieves the career stats for a player.
    Returns a pandas DataFrame that contains the information from the career stats table on baseball-reference.

    Args:
        browser : the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains the career stats

    """
    # search the player needed
    searchPlayer(browser, player)

    # parse the page to get the projected 2023 stats table and return it
    # soup = BeautifulSoup(browser.page_source, features="lxml")
    # stats = soup.find("table", {"id": "batting_proj"})
    # table = pd.read_html(str(stats))
    # projected = table[0]
    # # print(projected)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_standard"})
    table = pd.read_html(str(stats))
    seasonStats = table[0].iloc[-2, 3:]
    seasonStats = seasonStats.to_frame()
    seasonStats = seasonStats.transpose()

    # projected.to_csv('AaronJudgeProj.csv')

    return seasonStats


def getLastGame(browser, player):
    """
    A function that retrieves a players last game stats.
    Returns a pandas DataFrame that contains the stats from a players last game.

    Args:
        browser: the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains a players last game stats

    """
    # search the player needed
    searchPlayer(browser, player)

    # get to the link for 2022 stats,
    # will have to change once 2023 season starts
    link = browser.find_element(
        By.XPATH, '//*[@id="inner_nav"]/ul/li[5]/div/ul[1]/li[19]/a'
    )
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


def getPostseasonStats(browser, player):
    """
    A function that retrieves the Postseason stats for a player.
    Returns a pandas DataFrame that contains the information from the postseason stats section on baseball-reference.

    Args:
        browser : the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains the postseason stats

    """

    searchPlayer(browser, player)

    link = browser.find_element(
        By.XPATH, '//*[@id="inner_nav"]/ul/li[5]/div/ul[1]/li[20]/a'
    )
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_gamelogs_post"})
    table = pd.read_html(str(stats))
    postseason = table[0].iloc[:, 2:]

    # print(lastGame.shape)

    return postseason


def getVsRhpCurrent(browser, player):
    """
    A function that retrieves a players current season stats against right handed pitching.
    Returns a pandas DataFrame that contains a players current season stats against right handed pitching.

    Args:
        browser: the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains stats against all right handed pitchers split by starter and reliever

    """
    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits,
    # might have to change to get to 2023
    link = browser.find_element(
        By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[8]/a'
    )
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
    """
    A function that retrieves a players current season stats against left handed pitching.
    Returns a pandas DataFrame that contains a players current season stats left right handed pitching.

    Args:
        browser: the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: contains stats against all left handed pitchers split by starter and reliever

    """
    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits,
    #  might have to change to get to 2023
    link = browser.find_element(
        By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[8]/a'
    )
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
    """
    A function that retrieves a players career stats against all pitching.
    Returns a pandas DataFrame that contains a players career stats against all pitching.

    Args:
        browser (webdriver): the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve

    Returns:
        pandas.DataFrame: each row represents stats against different handed starting pitchers and all pitchers

    """
    # search the player needed
    searchPlayer(browser, player)

    # get to the the link with 2022 batting splits,
    # might have to change to get to 2023
    link = browser.find_element(
        By.XPATH, '//*[@id="bottom_nav_container"]/ul[1]/li[1]/a'
    )
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
    """
    A function that retrieves a players stats over gamesNum amount of games.
    Returns a pandas DataFrame that contains a players stats in each of the last games.

    Args:
        browser (webdriver): the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve
        gamesNum (int): how many games do retrieve stats for

    Returns:
        pandas.DataFrame: each row represents stats a game with their latest game as the last row

    """
    # search the player needed
    searchPlayer(browser, player)

    # get to the link for 2022 stats,
    # will have to change once 2023 season starts
    link = browser.find_element(
        By.XPATH, '//*[@id="inner_nav"]/ul/li[5]/div/ul[1]/li[8]/a'
    )
    statsLink = link.get_attribute('href')

    # load the new page
    browser.get(statsLink)

    # get the last row of the table and print out the stats for last game
    soup = BeautifulSoup(browser.page_source, features="lxml")
    stats = soup.find("table", {"id": "batting_gamelogs"})
    # stats = soup.find(id = "batting_gamelogs")
    table = pd.read_html(str(stats))
    lastxGames = table[0].iloc[-gamesNum - 1 : -1, 3:]

    # print(lastxGames)

    return lastxGames


# work on this part


def getAvgOverLastxGames(browser, player, gamesNum):
    """
    A function that retrieves the players avg stats over 'gamesNum' amount of games.
    Returns a pandas DataFrame that contains a players avg stats over the last games.

    Args:
        browser (webdriver): the browser that you are using, returned by setUpWebsite
        player (str): the player whose stats you are trying to retrieve
        gamesNum (int): how many games do retrieve stats for

    Returns:
        pandas.DataFrame: shows the average of that stat over specified number of games

    """
    xGames = getLastxGames(browser, player, gamesNum)
    avgXGames = xGames.mean(axis=0, numeric_only=True, skipna=True)
    avgXGames = avgXGames.to_frame()

    return avgXGames


# def main():
#     # global browser

#     browser = setUpWebsite()
#     # print(get2023Season(browser, "Yadier Molina"))
#     # print(getLastxGames(browser, "Aaron Judge", 7))
#     # print(getAvgOverLastXGames(browser, "Aaron Judge", 7))

#     # browser = webdriver.Chrome()

#     # browser.get("https://www.baseball-reference.com/")

#     # print("hello")

#     # options = webdriver.ChromeOptions()
#     # options.add_argument('headless')
#     # browser = webdriver.Chrome(options=options)

#     # browser = webdriver.Chrome()

#     # browser.get("https://www.baseball-reference.com/")
#     # search = input("Which player to search for: ")

#     # print(get2023Projected("Aaron Judge"))
#     # getLastGame(browser, search)
#     # getVsRhpCurrent(browser, "Gleyber Torres")
#     # getVsLhpCurrent(browser, search)
#     # getCareerSplits(browser, search)
#     # getAvgOverLastXGames(browser, search, 5)

#     # get a save the csv's for aaron judge and mike trout for each function

#     Yadier_Molina = get2023Season(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaSeason.csv')

#     Yadier_Molina = getCareer(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaCareer.csv')

#     Yadier_Molina = getPostseasonStats(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaPostseason.csv')

#     Yadier_Molina = getLastGame(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaLastGame.csv')

#     Yadier_Molina = getVsRhpCurrent(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaRhpCurrent.csv')

#     Yadier_Molina = getVsLhpCurrent(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaLhpCurrent.csv')

#     Yadier_Molina = getCareerSplits(browser, "Yadier Molina")
#     Yadier_Molina.to_csv('MolinaCarrerSplits.csv')

#     Yadier_Molina = getLastxGames(browser, "Yadier Molina", 5)
#     Yadier_Molina.to_csv('MolinaLast5.csv')

#     Yadier_Molina = getLastxGames(browser, "Yadier Molina", 10)
#     Yadier_Molina.to_csv('MolinaLast10.csv')

#     Yadier_Molina = getAvgOverLastxGames(browser, "Yadier Molina", 10)
#     Yadier_Molina.to_csv('MolinaLast10Avg.csv')

#     # maybe find one that gets the

#     return


# main()
