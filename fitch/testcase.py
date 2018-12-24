import unittest

from fitch.screen import FDevice
from fitch import detector


class FTestCase(unittest.TestCase):
    def __init__(self, device_id, *args, **kwargs):
        super(FTestCase, self).__init__(*args, **kwargs)
        self.device = FDevice(device_id)
        self.detector = detector
