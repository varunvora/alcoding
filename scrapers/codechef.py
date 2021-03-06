import re
import logging
from sys import stdin


data = stdin.read()

'''
Stdin is created by copy pasting the scoreboard as it is.
It would look something like this if you copy paste from the webpage
for e.g.

229
India3★varun_07
PES University, Bengaluru
625
-
100
25
100
100
-
-
100
100
100
-
558
India1★neeleshca26
PES University, Bengaluru
500
-
100
-
100
-
-
-
100
100
100
-
'''

score_list = re.findall(r"(\d+)\sIndia..(\w+)\sPES University, Bengaluru\s\d+", data)
if not score_list:
    logging.error('Verify input file and regex')
    quit()

lowest_so_far = int(score_list[0][0])
for row in score_list:
    rank, handle = row
    rank = int(rank)
    if rank > lowest_so_far:
        print()
        lowest_so_far = rank
    print(handle, end=' ')
