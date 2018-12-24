from pyminitouch import safe_device
import time

from fitch.logger import logger


def tap(device_id, point):
    x, y = map(int, point)
    logger.info('tap point: ({}, {})'.format(x, y))
    with safe_device(device_id) as d:
        d.tap([(x, y)], duration=200)
        time.sleep(0.2)


if __name__ == '__main__':
    tap('3d33076e', (500, 500))
