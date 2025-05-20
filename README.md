📱 DigiTrace – Phone Number OSINT Tool


DigiTrace is a Python-based OSINT (Open Source Intelligence) tool for tracing Indian phone numbers. It fetches detailed information like owner name, SIM card provider, location, IP address, and more, using publicly available resources like calltracer.in.

🧠 Features

🔍 Search details of Indian phone numbers

👤 Find SIM provider, owner name, and state

📍 Get IP address, IMEI, MAC, and more (if available)

🌐 Opens Telegram channel for updates

📲 Supports CLI interaction with improved error handling.



💻 Installation Guide

<pre> 

🪟 Windows

git clone https://github.com/hackwithyash/DigiTrace.git

cd DigiTrace

pip install -r requirements.txt

python number.py
</pre>

<pre> 
🐧Linux(Debian/Ubuntu)
  
sudo apt update
  
sudo apt install python3 python3-pip git -y
  
git clone https://github.com/hackwithyash/DigiTrace.git
  
cd DigiTrace
  
pip3 install -r requirements.txt
  
python3 number.py
  
</pre>
  <pre> 
📱 Termux (Android)
    
pkg update && pkg upgrade
    
pkg install python git -y
    
git clone https://github.com/hackwithyash/DigiTrace.git
    
cd DigiTrace
    
pip install -r requirements.txt
    
python number.py
    
</pre>

🚀 Usage
1. Run the script:
   python number.py
2. It will open a Telegram channel for updates.
3. Enter the phone number you want to trace (just the number, without +91).
4. View results in the console.

Example:

Enter a phone number to trace (or 'exit' to quit): +91 9876543210

🔍 Tracing number: 9876543210...

📋 Results:

📞 Number: 9876543210

👤 Owner Name: Rahul Sinha

📶 SIM card: Jio

📍 Mobile State: Maharashtra

...


📜 Legal Disclaimer
🛑 DigiTrace is strictly for educational, ethical hacking, and cybersecurity research purposes only.

❌ Do not use this tool for harassment, stalking, or any illegal activities.

⚖️ The author is not responsible for misuse or damages caused by this tool.

👨‍💻 Author
Yash Raj

Telegram: https://t.me/hack_with_yash

⭐️ Star the Repo
If you found this useful, don't forget to give this repo a ⭐️ and share it with other cybersecurity learners!
