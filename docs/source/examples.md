# Examples

## getCarrerSplits(browser, player)
The code below will return Aaron Judge's career splits
```python

import FantasyBaseballTrends as fbt

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

print(fbt.getVsRhpCurrent(browser, "Mike Trout"))
```

Output:
``` 
           Split    G    GS   PA   AB     R  ...  SF  IBB  ROE  BAbip  tOPS+  sOPS+
0         vs RHP  111   NaN  401  320  74.0  ...   4   11    3  0.320    107    193
4  vs RH Starter   82  82.0  361  290  65.0  ...   4   10    3  0.322    105    191
```

