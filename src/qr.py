# coding: utf8

import qrcode


def generate(ssid: str, psk: str):
    """
    Generate QR code used to connect to wifi network

    :param ssid: network SSID
    :param psk: network password
    :param output: file name and path
    :return: QR code image object
    """
    data = f"WIFI:S:{ssid};T:WPA;P:{psk};;"
    img = qrcode.make(data)

    return img
