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
import platform


# PROJECT
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# system
# 'Linux', 'Windows' or 'Darwin'.
SYSTEM_NAME = platform.system()
NEED_SHELL = SYSTEM_NAME != 'Windows'
ADB_EXECUTOR = 'adb'

# strict mode
# setting this True, fitch will not catch error.
STRICT_MODE = False

# encoding
DEFAULT_CHARSET = 'utf-8'

# detector cv method
# SQDIFF is not supported now ( it takes min value, but default is max value. )
CV_METHOD_NAME = 'cv2.TM_CCOEFF_NORMED'
CV_THRESHOLD = 0.8

# 图像模板的缩放范围
# (1, 3, 10) 即 在 1-3 倍范围内，等距离取10张图片进行匹配
CV_PIC_SCALE = (0.5, 3, 10)

# findit relative
FINDIT_SERVER_IP = '127.0.0.1'
FINDIT_SERVER_PORT = 9410
REMOTE_MODE = False

DEFAULT_PYTHON_EXECUTOR = 'python'
DEFAULT_LOCAL_PIC_DIR = '.'
