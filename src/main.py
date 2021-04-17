#!/usr/bin/python3
# coding: utf8

import argparse as agp
import wifi
import qr
import sys
from exceptions import *


def print_error(msg: str):
    """
    Print an error (in red) and exit

    :param msg: error message
    """
    print(f"\033[31mERROR: {msg}\033[0m", file=sys.stderr)
    sys.exit(1)


def print_success(msg: str):
    """
    Print msg in green

    :param msg: string to print
    """
    print(f"\033[32m{msg}\033[0m")


def main():
    parser = agp.ArgumentParser(description="Parse command line arguments")
    parser.add_argument('--ssid', type=str, default=None, help="Create QR code for Wi-Fi with provided SSID")
    parser.add_argument('--show-password', action='store_true', default=False, help="Print Wi-Fi password")
    parser.add_argument('--input-password', action='store_true', default=False, help="Manually input Wi-Fi password")
    parser.add_argument('--show-image', action='store_true', default=False, help="Do not show generated QR code")
    parser.add_argument('--output', '-o', type=str, default="wifi_QR.png", help="Save generated QR code to PATH")
    args = parser.parse_args()
    ssid, psk = "", ""

    if args.ssid is None:
        try:
            # Get current network SSID
            ssid = wifi.get_ssid()
        except WifiNotFoundError:
            print_error("The system has no wifi connection; couldn't find current SSID. Please use the --ssid option.")
        except DependencyNotFoundError:
            print_error("This program only works with NetworkManager.")
    else:
        # Use provided SSID
        ssid = args.ssid

    if args.input_password and args.ssid is not None:
        # Get user input for Wi-Fi password
        psk = input(f"Please enter password for {ssid} :\n")
    else:
        try:
            # Get existing password
            psk = wifi.get_psk(ssid)
        except DependencyNotFoundError:
            print("This program only works with NetworkManager")

    img = qr.generate(ssid, psk)

    # Save generated QR code
    img.save(args.output)

    print_success(f"Successfully generated QR code for {ssid} as {args.output}")

    if args.show_password:
        # Print password if asked by user
        print(f"Current password for {ssid} : {psk}")

    if args.show_image:
        img.show()


if __name__ == "__main__":
    main()
