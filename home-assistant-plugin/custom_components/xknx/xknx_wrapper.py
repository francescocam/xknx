import threading
import time
import logging

from xknx import XKNX,Config,MulticastSender,MulticastReceiver,StateUpdater

_LOGGER = logging.getLogger(__name__)

class XKNX_Wrapper(object):
    """Representation of XKNX Object."""

    def __init__(self, hass, xknx_config):

        self.xknx = XKNX()

        self.initialized = False
        self.lock = threading.Lock()
        self.hass = hass
        self.config_file = xknx_config.config_file()

    @staticmethod
    def callback(  xknx, device, telegram):
        print("{0}".format(device.name))


    def start(self):

        Config(self.xknx).read(file=self.config_file)

        MulticastSender.start_thread(self.xknx)
        MulticastReceiver.start_thread(self.xknx, self.callback)
        StateUpdater.start_thread(self.xknx)

        self.initialized = True

