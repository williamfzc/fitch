import subprocess

from fitch import config
from fitch.logger import logger


def restart_adb():
    """ restart adb server """
    _ADB = config.ADB_EXECUTOR
    subprocess.check_call([_ADB, 'kill-server'])
    subprocess.check_call([_ADB, 'start-server'])


def is_device_connected(device_id):
    """ return True if device connected, else return False """
    _ADB = config.ADB_EXECUTOR
    try:
        device_name = subprocess.check_output([_ADB, '-s', device_id, 'shell', 'getprop', 'ro.product.model'])
        device_name = device_name.decode(config.DEFAULT_CHARSET).replace('\n', '').replace('\r', '')
        logger.info('device {} online'.format(device_name))
    except subprocess.CalledProcessError:
        return False
    return True
