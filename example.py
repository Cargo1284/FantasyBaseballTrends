import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

# print("output for getprojected2023: \npyth")

# print(fbt.get2023Projected(browser, "Aaron Judge"))

print("output for splits career: \n")

print(fbt.getCareerSplits(browser, "Aaron Judge"))

print("output for lhp: \n")
print(fbt.getVsLhpCurrent(browser, "Mike Trout"))

print("output for rhp: \n ")

print(fbt.getVsRhpCurrent(browser, "Mike Trout"))

print("output for last game : \n")
print(fbt.getLastGame(browser, "Gleyber Torres"))

print("output for last 4 games: \n")
print(fbt.getLastxGames(browser, "Gleyber Torres", 4))