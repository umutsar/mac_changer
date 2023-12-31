import subprocess
import re
import time

ascii_code = '''
 -----------------------------------------@utsr_---------------------------------------
/  _|      _|  _|      _|  _|      _|  _|_|_|_|_|   _|_|_|_|_|  _|_|_|_|_|  _|_|_|     /
/  _|      _|  _|_|  _|_|  _|      _|      _|       _|          _|      _|  _|    _|   /
/  _|      _|  _|  _|  _|  _|      _|      _|       _|_|_|_|_|  _|_|_|_|_|  _|_|_|_|   /
/  _|      _|  _|      _|  _|      _|      _|               _|  _|      _|  _|  _|     /
/  _|_|_|_|_|  _|      _|  _|_|_|_|_|      _|       _|_|_|_|_|  _|      _|  _|    _|   /
/                                                       _|                             /
 -----------------------------------CREATED BY UMUT SAR-------------------------------

              *************************sar_scanner*************************
'''
def show_ascii_art(art):
    for line in art.splitlines():
        print(line)
        time.sleep(0.08)

show_ascii_art(ascii_code)

def change_mac(interface, new_mac):
    print(f"Mac address is changing: {interface} -> {new_mac}")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("MAC not found.")

interface = input("MAC adresini değiştirmek için ağ arabirimini girin (örneğin, wlan0): ")
"Enter network interface for changing mac address"
current_mac = get_current_mac(interface)
print(f"Current MAC address: {current_mac}")

new_mac = input("Enter new MAC address (example, 00:11:22:33:44:55): ")


change_mac(interface, new_mac)

current_mac = get_current_mac(interface)
if current_mac == new_mac:
    print(f"Successful: {current_mac}")
else:
    print("Error.")
