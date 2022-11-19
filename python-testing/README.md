# Dice Results
## Best of 2 or best of 3
This was to help test what would be the most rounded character creation method. It looks like best of 2 is the optimal choice.
|Result| best of 3 | best of 2 |
| --- | --- | --- |
| 6   | 409 | 303 |
| 5   | 307 | 262 |
| 4   | 177 | 200 |
| 3   | 73  | 140 |
| 2   | 32  | 77  |
| 1   | 1   | 17  |

After some script improvements, here are some runs of 10k rolls:
```
» python3 best-of-dice.py 
best of one [1721, 1605, 1700, 1565, 1672, 1736]
SIDE ... PERCENT
1 ...... 17 %
2 ...... 16 %
3 ...... 17 %
4 ...... 15 %
5 ...... 16 %
6 ...... 17 %
best of two [276, 863, 1339, 2007, 2506, 3008]
SIDE ... PERCENT
1 ...... 2 %
2 ...... 8 %
3 ...... 13 %
4 ...... 20 %
5 ...... 25 %
6 ...... 30 %
best of three [42, 334, 869, 1710, 2806, 4238]
SIDE ... PERCENT
1 ...... 0 %
2 ...... 3 %
3 ...... 8 %
4 ...... 17 %
5 ...... 28 %
6 ...... 42 %
```
