import pytest
from pytest_embedded import Dut

@pytest.mark.target('esp32s3')
@pytest.mark.env('esp32_s3_lcd_ev_board')
def test_usb_stream(dut: Dut)-> None:
    dut.run_all_single_board_cases()

