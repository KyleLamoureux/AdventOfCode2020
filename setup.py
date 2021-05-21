import os
import sys

path = "./" + sys.argv[-1]

os.makedirs(path)
open(path + "/q1.py", 'w')
open(path + "/q2.py", 'w')
open(path + "/input.txt", 'w')