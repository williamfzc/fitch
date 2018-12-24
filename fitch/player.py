from pyminitouch import safe_device
import time


def tap(device_id, point):
    point = map(int, point)
    with safe_device(device_id) as d:
        d.tap([point], duration=200)
        time.sleep(0.2)


if __name__ == '__main__':
    tap('3d33076e', (500, 500))
