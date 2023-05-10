# Examples

## getCareer(browser, plater)
The code below will return Yadier Molina's career stats
```python
import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(getCareer(browser, "Yadier Molina"))

```
Output:
```
        Lg     G    PA    AB    R     H   2B  ...  GDP HBP  SH  SF IBB  Pos Awards
27  19 Yrs  2224  8554  7817  777  2168  408  ...  287  76  43  75  50  NaN    NaN

[1 rows x 27 columns]
```



## getPostseasonStats(browser, player)
Ther code below will return Yadier Molina's post season stats
```python

import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getPostseasonStats(browser, "Yadier Molina"))

```
Output:
```
[1 rows x 27 columns]
              Series    Date   Tm Unnamed: 5  ...    acLI    cWPA   RE24  Pos
0            NLCS g4  Oct 17  STL          @  ...   32.67  -1.24%  -0.54    C
1              WS g1  Oct 23  STL          @  ...  115.03  -1.83%  -0.40    C
2              WS g3  Oct 26  STL        NaN  ...     NaN     NaN    NaN    C
3              WS g4  Oct 27  STL        NaN  ...   21.13  -0.73%  -0.61    C
4    2005 Postseason    Date   Tm        NaN  ...    acLI    cWPA   RE24  Pos
..               ...     ...  ...        ...  ...     ...     ...    ...  ...
112          NLWC g1   Oct 6  STL          @  ...   34.48  -2.20%  -1.38    C
113  2022 Postseason    Date   Tm        NaN  ...    acLI    cWPA   RE24  Pos
114          NLWC g1   Oct 7  STL        NaN  ...    8.65  -0.53%  -0.84    C
115          NLWC g2   Oct 8  STL        NaN  ...   15.48  -0.29%  -0.37    C
116              NaN     NaN  NaN        NaN  ...     NaN     NaN    NaN  NaN

[117 rows x 36 columns]
```

## getLastGame(browser, player)
The code below will return Yadier Molina's last game stats
```python

import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getLastGame(browser, "Yadier Molina"))
```
Ouput:
```
     Date   Tm Unnamed: 5  Opp   Rslt  ...   cWPA   RE24 DFS(DK) DFS(FD) Pos
81  Oct 5  STL          @  PIT  L,3-5  ...  0.00%  -0.16    0.00    0.00  PH

[1 rows x 37 columns]
```


## getLastxGames(browser, player, gamesNum)
The code below will return Yadier Molina's stats over the past 10 games
```python

import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getLastxGames(browser, "Yadier Molina", 10))
```

Ouput
```
       Date   Tm Unnamed: 5  Opp    Rslt  ...     WPA  acLI    cWPA   RE24 Pos
134  Sep 18  STL          @  PHI   W,5-0  ...  -0.059   .27  -0.02%  -1.08   C
135  Sep 20  STL        NaN  NYM  W,11-6  ...   0.075  2.32   0.09%   0.68   C
136  Sep 21  STL        NaN  NYM   W,6-5  ...   0.078  1.17   0.09%   0.52   C
137  Sep 22  STL        NaN  NYM   L,6-8  ...   0.060  1.84   0.12%   1.64   C
138  Sep 23  STL        NaN  CHC   L,1-5  ...   0.175  2.85   0.25%   1.19   C
139  Sep 24  STL        NaN  CHC   W,2-1  ...  -0.069  2.04  -0.03%  -0.51   C
140  Sep 25  STL        NaN  CHC   W,3-2  ...   0.219  3.13   0.23%   0.52   C
141  Sep 26  STL          @  HOU   L,4-5  ...   0.191  5.36   0.46%   1.13   C
142  Sep 27  STL          @  HOU  W,13-6  ...   0.021  5.51   0.06%   0.62   C
143  Sep 28  STL          @  HOU   W,8-0  ...  -0.017  3.00  -0.10%  -0.22   C

[10 rows x 35 columns]
```

## getCareerSplits(browser, player)
The code below will return Aaron Judge's career splits
```python

import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getCareerSplits(browser, "Aaron Judge"))

```
Output:
```
    I          Split    G     GS    PA    AB  ...  SH  SF  IBB  ROE  BAbip  tOPS+
0 NaN         vs RHP  711    NaN  2361  1998  ...   0  17   21   18  0.351     99
4 NaN  vs RH Starter  518  497.0  2224  1870  ...   0  17   29   14  0.364    106
1 NaN         vs LHP  374    NaN   826   663  ...   0   4   18    3  0.332    101
5 NaN  vs LH Starter  217  214.0   963   791  ...   0   4   10    7  0.306     86

```

## getVsLhpCurrent(browser, player)
The code below will return Mike Trouts stats against Left Handed Pitchers
```python
import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getVsLhpCurrent(browser, "Mike Trout"))
```

Output:
```

           Split   G    GS   PA   AB     R  ...  SF  IBB  ROE  BAbip  tOPS+  sOPS+
1         vs LHP  43   NaN  106   82  18.0  ...   0    4    2  0.313     74    146
5  vs LH Starter  32  32.0  146  112  27.0  ...   0    5    2  0.310     88    166

```

## getVsRhpCurrent(browser, player)
The code below will return Mike Trouts stats against Right Handed Pitchers
```python
import FantasyBaseballTrends as fbt

browser = fbt.setUpWebsite()

print(fbt.getVsRhpCurrent(browser, "Mike Trout"))
```

Output:
``` 
           Split    G    GS   PA   AB     R  ...  SF  IBB  ROE  BAbip  tOPS+  sOPS+
0         vs RHP  111   NaN  401  320  74.0  ...   4   11    3  0.320    107    193
4  vs RH Starter   82  82.0  361  290  65.0  ...   4   10    3  0.322    105    191
```
