import time

from fitch import FTestCase


# build your own API in this class
class SFTestCase(FTestCase):
    KEY_CODE_HOME = 3
    KEY_CODE_RECENT = 187

    # this function can be directly used in case
    def clean_recent(self):
        self.f_init_store('pictures/global')
        self.f_device.toolkit.input_key_event(self.KEY_CODE_HOME)
        time.sleep(0.5)
        self.f_device.toolkit.input_key_event(self.KEY_CODE_RECENT)
        time.sleep(0.5)
        self.f_tap_target('x')
        time.sleep(1)
        self.f_device.toolkit.input_key_event(self.KEY_CODE_HOME)
