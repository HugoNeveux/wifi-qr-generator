# coding: utf8

import shutil
import re
import subprocess
from exceptions import *


def get_ssid() -> str:
    """
    Get current wifi network SSID using NetworkManager

    :return: str
    """
    if shutil.which("nmcli") is not None:
        ssid_regex = r"yes:(.*)\n"

        tmp = subprocess.check_output(["nmcli", "-t", "-f", "active,ssid", "dev", "wifi"]).decode('utf8')
        search = re.search(ssid_regex, tmp)
        if search is None:
            raise WifiNotFoundError("The system has no wifi connection; can't find network SSID.")
        else:
            ssid = search[1]
    else:
        raise DependencyNotFoundError("nmcli not found. NetworkManager is required to run this program.")
    return ssid


def get_psk(ssid: str) -> str:
    """
    Get wifi password from SSID using nmcli

    :param ssid:
    :return:
    """

    if shutil.which("nmcli") is not None:
        psk = subprocess.check_output(
                ["nmcli", "-s", "-g", "802-11-wireless-security.psk", "connection", "show", ssid]).decode("utf8")
    else:
        raise DependencyNotFoundError("nmcli not found. NetworkManager is required to run this program.")
    return psk.strip()
