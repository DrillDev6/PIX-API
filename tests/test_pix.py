import sys 
sys.path.append('../')
import pytest
import os
from payments.pix import Pix


def test_pix_create_payment():
    pix_instance = Pix()

    payment_info = pix_instance.create_payment(base_dir="../")

    assert "bank_payment_id" in payment_info
    assert "qrcode_path" in payment_info

    qrcode_path = payment_info["qrcode_path"]
    
    os.path.isfile("../static/img/{qr_code_path}.png")
