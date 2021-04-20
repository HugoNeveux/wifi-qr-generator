# coding: utf8

import qrcode


def generate(ssid: str, psk: str):
    """
    Generate QR code used to connect to wifi network

    :param ssid: network SSID
    :param psk: network password
    :return: QR code image object
    """
    data = f"WIFI:S:{ssid};T:WPA;P:{psk};;"
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
    qr.add_data(data)
    qr.make()

    return qr
