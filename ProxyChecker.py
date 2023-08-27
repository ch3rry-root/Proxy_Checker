import socket
import os
import time
from colorama import Fore, Back, Style
from lolpython import lol_py
import datetime
import datetime
import calendar
import concurrent.futures
def main():
    current_date = datetime.datetime.now()
    month_name = calendar.month_name[current_date.month]
    formatted_date = f"   {month_name} {current_date.day}, {current_date.year}   "

    proxyascii = f"""
╔═╗┬─┐┌─┐─┐ ┬┬ ┬  ╔═╗┬ ┬┌─┐┌─┐┬┌─┌─┐┬─┐
╠═╝├┬┘│ │┌┴┬┘└┬┘  ║  ├─┤├┤ │  ├┴┐├┤ ├┬┘
╩  ┴└─└─┘┴ └─ ┴   ╚═╝┴ ┴└─┘└─┘┴ ┴└─┘┴└─
 """
    today = "    Todays Date:"
    dev = """ >Software Developer< 
 |   ch3rry root    |"""

    lol_py(proxyascii)
    lol_py(today)
    lol_py(formatted_date)
    print()
    lol_py(dev)
    print()
    welcome = """Welcome to ProxyChecker!
    
Plz add proxies to proxies.txt file 
Proxies Format : IP:PORT

If you have already loaded the proxies into proxies.txt, press Enter.
"""
    lol_py(welcome)
    input()
main()


def check_proxy(ip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(5)  
            sock.connect((ip, port))
        return True
    except Exception as e:
        return False

def main2():
    proxy_file = "proxies.txt"
    good_proxies = []
    options = """
Done...
Good proxies saved in goods.txt!

Options:
>1- Back to menu
>2- Check new proxies (This option remove proxies.txt and goods.txt)
>3- Exit 
Plz choose an option"""

    with open(proxy_file, "r") as file:
        proxies = file.readlines()

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = []
        for proxy in proxies:
            proxy_parts = proxy.strip().split(":")
            if len(proxy_parts) != 2:
                print(f"{Fore.RED}Incorrect format for proxy: {proxy.strip()}")
                print(Fore.RESET)
                continue

            ip = proxy_parts[0]
            port = int(proxy_parts[1])

            results.append(executor.submit(check_proxy, ip, port))

        for idx, future in enumerate(concurrent.futures.as_completed(results)):
            if future.result():
                good_proxies.append(proxies[idx].strip())
                print(f"{Fore.LIGHTGREEN_EX}Valid proxy: {Fore.WHITE}{proxies[idx].strip()}")
            else:
                print(f"{Fore.RED}Invalid proxy: {Fore.WHITE}{proxies[idx].strip()}")

    with open("goods.txt", "w") as goods_file:
        for proxy in good_proxies:
            goods_file.write(proxy + "\n")
    lol_py(options)
    choice = input()

    if choice == "1":
        main()
    elif choice == "2":
        os.remove("goods.txt")
        with open("proxies.txt", "w") as proxy_file:
            pass
        main()
    elif choice == "3":
        pass
    else:
        print(f"{Fore.RED}Invalid option! Please choose 1, 2, or 3.")
        print(Fore.RESET)
if __name__ == "__main__":
    main2()