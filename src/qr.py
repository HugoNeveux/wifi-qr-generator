# coding: utf8

import qrcode


def generate(ssid: str, psk: str, output: str = "wifi_QR.png"):
    """
    Generate QR code used to connect to wifi network

    :param ssid: network SSID
    :param psk: network password
    :param output: file name and path
    :return:
    """
    data = f"WIFI:S:{ssid};T:WPA;P:{psk};;"

    qrcode.make(data).save(output)
