import logging

logger = logging.getLogger(__name__)


class TestPowerPin:
    def test_get_gpio(self, my_pwr_pin):
        pin_num = int(my_pwr_pin.get_gpio())
        logger.info(f'pin_num = {pin_num}')
        assert pin_num == 13


class TestOperatePWR:
    pass