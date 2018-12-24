import cv2
import os
import subprocess
import platform


# PROJECT
PROJECT_PATH = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))

# system
# 'Linux', 'Windows' or 'Darwin'.
SYSTEM_NAME = platform.system()
NEED_SHELL = SYSTEM_NAME != 'Windows'
ADB_EXECUTOR = 'adb'
if SYSTEM_NAME == 'Windows':
    ADB_EXECUTOR = subprocess.getoutput('where adb')
else:
    ADB_EXECUTOR = subprocess.getoutput('which adb')

# encoding
DEFAULT_CHARSET = 'utf-8'

# detector cv method
# TODO SQDIFF is not supported now ( it takes min value, but default is max value. )
CV_METHOD = cv2.TM_CCOEFF_NORMED
