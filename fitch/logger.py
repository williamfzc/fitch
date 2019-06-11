"""
MIT License

Copyright (c) 2018 williamfzc

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import os
import datetime
import random
import string
import sys
from loguru import logger

# remove default logger
logger.remove()
logger.add(sys.stderr, level="DEBUG")

# save log to file
# create log dir
log_dir = os.path.join(os.getcwd(), 'log')
os.makedirs(log_dir, exist_ok=True)

# build random char (length is 4)
random_char = ''.join(random.sample(string.ascii_letters + string.digits, 4))
# build timestamp
timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")

# save entire log to file
log_file = os.path.join(log_dir, 'fitch_{}_{}.log'.format(timestamp, random_char))
logger.add(log_file, level="DEBUG")

# ignore the third-party library by default
logger.disable('pyminitouch')
logger.disable('fastcap')
