# FantasyBaseballTrends

[![Build Status](https://github.com/Cargo1284/FantasyBaseballTrends/workflows/Build%20Status/badge.svg?branch=main)](https://github.com/Cargo1284/FantasyBaseballTrends/actions?query=workflow%3A%22Build+Status%22)
[![codecov](https://codecov.io/gh/Cargo1284/FantasyBaseballTrends/branch/main/graph/badge.svg)](https://app.codecov.io/gh/Cargo1284/FantasyBaseballTrends)
![Crates.io](https://img.shields.io/crates/l/ap)
![GitHub issues](https://img.shields.io/github/issues/cargo1284/fantasybaseballtrends)
[![PyPI](https://img.shields.io/pypi/v/FantasyBaseballTrends)](https://pypi.org/project/FantasyBaseballTrends/)
[![readthedocs](https://img.shields.io/readthedocs/fantasybaseballtrends)](https://fantasybaseballtrends.readthedocs.io/en/latest/fantasybaseballtrends.html)



## Overview

This library scrapes specific hitter stats from BaseballReference.
The purpose of this library is to provide fantasy owners a chance to see how the players in their lineup have been performing over a number of games and how they perform against a certain pitcher. This will help facilitate their daily lineup constuction and to see which players on the wire are having a hot streak as well as players that have been trending downwards. 

## Instalation
To install, run the following:
```
pip install FantasyBaseballTrends
```

## Usage
### Projected Stats
This function will return a specific hitters projected offensive stats for the 2023 season. 
```
get2023Projected(browser, player)
```
### Last Game Stats
This function will return all of offensive stats of a players most recent game.
```
getLastGame(browser, player)
```
### Current stats vs RHP
This function will return a players current season hitting stats against right handed pitchers.
```
getVsRhpCurrent(browser, player)
```
### Current stats vs LHP
This function will return a players current season hitting stats against left handed pitchers.
```
getVsLhpCurrent(browser, player)
```
### Career Splits
This function will return a hitter's carrer splits. The returning data frame is split up by the opposing pitchers handedness and if they are a starter or not.
```
getCareerSplits(browser, player)
```
### Stats over number of games
This funciton will return a hitter's stats over a user specified number of games. 
```
getLastxGames(browser, player, gamesNum)
```

