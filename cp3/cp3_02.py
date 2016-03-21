# _*_ coding:utf-8_*_
# import math
#
# print math.pow(2, 0.5)
#
# print math.pi

# from math import pow, sin, log
#
# print pow(2, 0.5)
#
# print sin(3.14)

# import math, logging
#
# print math.log(10)
# print logging.log(10, 'something')

# from math import log
# from logging import log as logger
#
# print log(10)
# logger(10, 'import from logging')

#task
# import os
# print os.path.isdir(r'C:\Windows')
# print os.path.isfile(r'C:\Windows')

from os.path import isdir as isdir
from os.path import isfile as isfile

print isdir(r'C:\Windows')
print isfile(r'C:\Windows')