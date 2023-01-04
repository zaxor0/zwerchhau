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

# 3d6 versus 4d6 drop lowest
- The most expected range shifts from '9 to 12' to '11 to 15'
- The chance of having an 18 quadruples
```
rolled 3d6 10000 times
3 ...... 0.39 %
4 ...... 1.19 %
5 ...... 2.78 %
6 ...... 4.77 %
7 ...... 7.25 %
8 ...... 9.66 %
9 ...... 11.77 %
10 ...... 12.68 %
11 ...... 12.35 %
12 ...... 11.95 %
13 ...... 9.27 %
14 ...... 6.56 %
15 ...... 4.48 %
16 ...... 2.84 %
17 ...... 1.61 %
18 ...... 0.45 %

rolled 4d6 and dropped the lowest 10000 times
3 ...... 0.07 %
4 ...... 0.15 %
5 ...... 0.77 %
6 ...... 1.59 %
7 ...... 3.0 %
8 ...... 5.02 %
9 ...... 7.0 %
10 ...... 8.9 %
11 ...... 11.83 %
12 ...... 12.53 %
13 ...... 12.72 %
14 ...... 12.97 %
15 ...... 10.52 %
16 ...... 7.19 %
17 ...... 3.9 %
18 ...... 1.84 %
```
