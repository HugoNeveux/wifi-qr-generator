# wifi-qr-generator
Generate wifi Qr Code on Linux

## Installation

Python dependancies : see requirements.txt
System depandancies : libopengl0 (install with apt : `sudo apt-get install libopengl0`)

## Usage

```
usage: main.py [-h] [--ssid SSID] [--show-password] [--input-password] [--output OUTPUT] [--save-image] [--show-image]

Parse command line arguments

optional arguments:
  -h, --help            show this help message and exit
  --ssid SSID           Create QR code for Wi-Fi with provided SSID
  --show-password       Print Wi-Fi password
  --input-password      Manually input Wi-Fi password
  --output OUTPUT, -o OUTPUT
                        Save generated QR code to OUTPUT
  --save-image          Save generated QR code in PNG file
  --show-image          Show QR code in separate window instead of printing it in console. Use this option if the QR code isn't displayed correctly.
```
