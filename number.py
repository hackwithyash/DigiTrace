import requests
from bs4 import BeautifulSoup
import re
import logging
import webbrowser
import pyfiglet
import sys


def print_banner():
    ascii_banner = pyfiglet.figlet_format("DigiTrace")
    print(ascii_banner)


def escape_markdown(text):
    return re.sub(r"([_*()~`>#+\-=|{}.!])", r"\\\1", text)


def setup_logging():
    logging.basicConfig(format="%(message)s", level=logging.INFO)
    return logging.getLogger(__name__)


logger = setup_logging()


def trace_number(phone_number):
    url = "https://calltracer.in"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {"country": "IN", "q": phone_number}

    try:
        response = requests.post(url, headers=headers, data=payload, timeout=10)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        fields = [
            ("📞 Number", phone_number),
            ("❗️ Complaints", "Complaints"),
            ("👤 Owner Name", "Owner Name"),
            ("📶 SIM card", "SIM card"),
            ("📍 Mobile State", "Mobile State"),
            ("🔑 IMEI number", "IMEI number"),
            ("🌐 MAC address", "MAC address"),
            ("⚡️ Connection", "Connection"),
            ("🌍 IP address", "IP address"),
            ("🏠 Owner Address", "Owner Address"),
            ("🏘 Hometown", "Hometown"),
            ("🗺 Reference City", "Refrence City"),
            ("👥 Owner Personality", "Owner Personality"),
            ("🗣 Language", "Language"),
            ("📡 Mobile Locations", "Mobile Locations"),
            ("🌎 Country", "Country"),
            ("📜 Tracking History", "Tracking History"),
            ("🆔 Tracker Id", "Tracker Id"),
            ("📶 Tower Locations", "Tower Locations")
        ]

        details = {}
        for key, label in fields:
            if key == "📞 Number":
                details[key] = label
            else:
                element = soup.find(text=re.compile(f"^{label}$"))
                details[key] = element.find_next("td").text.strip() if element else "N/A"

        return details

    except requests.RequestException as e:
        return f"❌ Network error: {e}"
    except Exception as e:
        return f"⚠️ Parsing error: {e}"


def main():
    print_banner()
    telegram_channel_url = "https://t.me/hack_with_yash"
    print("*🔍 Welcome to DigiTrace - Number OSINT Tool!*")
    print("\n📢 For more tools & updates, join our Telegram channel:")
    print(f"👉 {telegram_channel_url}\n")
    webbrowser.open(telegram_channel_url)

    while True:
        try:
            phone_number = input("\n📞 Enter a phone number to trace (or type 'exit'): +91 ").strip()
            if phone_number.lower() == 'exit':
                print("👋 Goodbye!")
                sys.exit()

            print(f"\n🔍 Tracing number +91 {phone_number}... Please wait!")
            details = trace_number(phone_number)
            
            print("\n📋 Results:")
            if isinstance(details, dict):
                for key, value in details.items():
                    print(f"{key}: {value}")
            else:
                print(details)

        except KeyboardInterrupt:
            print("\n👋 Exiting... Stay safe!")
            break


if __name__ == "__main__":
    main()
