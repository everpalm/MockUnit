import pytest
import RPi.GPIO as gpio
from rasperberry.gpio import PowerPin
from rasperberry.gpio import OperatePWR


@pytest.fixture
def my_pwr_pin():
    return PowerPin('gpio_pins.json', 'GPIO.2')


@pytest.fixture
def pwr_operation(my_pwr_pin):
    # my_pwr = OperatePWR(my_pwr_pin, gpio.BOARD)
    # yield my_pwr
    # my_pwr.clear_gpio()
    pass
