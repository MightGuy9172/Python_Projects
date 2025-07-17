# ISS Overhead Notifier

This project checks if the International Space Station (ISS) is currently overhead at your location and sends you an email notification if it is visible at night.

## Features

- Uses the ISS location API to determine if the ISS is above your coordinates.
- Checks local sunrise and sunset times to ensure notifications are sent only at night.
- Sends an email alert when the ISS is overhead and visible.

## Usage

1. Set your email credentials and location coordinates in the `.env` file.
2. Run the script to receive notifications when the ISS is overhead at night.

## Requirements

- Python 3
- `requests`
- `python-dotenv`

## How it works

The script periodically checks the ISS position and your local time. If the ISS is overhead and it is nighttime, you will receive an email notification.
