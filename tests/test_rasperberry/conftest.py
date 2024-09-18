import pytest
from rasperberry.gpio import PowerPin


@pytest.fixture
def my_pwr_pin():
    return PowerPin('gpio_pins.json', 'GPIO.2')