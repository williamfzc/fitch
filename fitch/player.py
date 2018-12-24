from pyminitouch import MNTDevice
import time

from fitch.logger import logger


class ActionPlayer(object):
    def __init__(self, device_id):
        self.device_id = device_id
        self.mnt = MNTDevice(device_id)

    def stop(self):
        self.mnt.stop()

    def tap(self, point, duration=100):
        x, y = map(int, point)
        logger.info('tap point: ({}, {})'.format(x, y))
        self.mnt.tap([(x, y)], duration=duration)
        time.sleep(duration / 1000)


if __name__ == '__main__':
    ap = ActionPlayer('4df189487c7b6fef')
    ap.tap((500, 500))
    ap.stop()
