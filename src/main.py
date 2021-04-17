#!/usr/bin/python3
# coding: utf8

import argparse as agp
import wifi
import qr
import sys
from exceptions import *


def print_error(msg: str) -> None:
    """
    Print an error (in red) and exit

    :param msg:
    :return:
    """
    print(f"\033[31mERROR: {msg}\033[0m", file=sys.stderr)
    sys.exit(1)


def print_success(msg: str) -> None:
    """
    Print msg in green

    :param msg:
    :return:
    """
    print(f"\033[32m{msg}\033[0m")


def main() -> None:
    parser = agp.ArgumentParser(description="Parse command line arguments")
    parser.add_argument('--output', '-o', type=str, default="wifi_QR.png", help="Output path for QR code")
    parser.add_argument('--ssid', type=str, default=None, help="Create QR code for Wi-Fi with provided SSID.")
    parser.add_argument('--show-password', action='store_true', default=False, help="Print Wi-Fi password")
    args = parser.parse_args()
    ssid, psk = "", ""

    if args.ssid is None:
        try:
            ssid = wifi.get_ssid()
        except WifiNotFoundError:
            print_error("The system has no wifi connection; couldn't find current SSID. Please use the --ssid option.")
        except DependencyNotFoundError:
            print_error("This program only works with NetworkManager.")
    else:
        ssid = args.ssid

    try:
        psk = wifi.get_psk(ssid)
    except DependencyNotFoundError:
        print("This program only works with NetworkManager")

    qr.generate(ssid, psk, args.output)
    print_success(f"Successfully generated QR code for {ssid} as {args.output}")

    if args.show_password:
        print(f"Current password for {ssid} : {psk}")


if __name__ == "__main__":
    main()
