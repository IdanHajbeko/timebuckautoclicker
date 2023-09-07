import pyautogui
import time
import os
import requests
from bs4 import BeautifulSoup
import socket


print(os.system('ipconfig'))
hostname = socket.gethostname()
IPAddr = socket.gethostbyname(hostname)

print(hostname)
print(IPAddr)


url = 'https://www.youtube.com/watch?v=6POZlJAZsok&list=PLw_4bxaqWDlYT0vOCxMrrYXIfonbE9AOc&index=38'


x_coordinate = 1828
y_coordinate = 39

x_coordinate1 = 1828
y_coordinate2 = 39

def get_time():
    while True:
        try:
            response = requests.get(url)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, 'html.parser')

            title_tag = soup.title

            if title_tag is not None:
                print("Title of the website:", int(title_tag.text))
                return int(title_tag.text)
                break
            else:
                print("Title not found on the webpage.")

        except requests.exceptions.RequestException as e:
            print(f"An error occurred while fetching the webpage: {e}")

        except Exception as e:
            print(f"An error occurred: {e}")


def clickk(x, y, x1, y2):
    pyautogui.moveTo(x, y, duration=0.1)

    pyautogui.click()

    time.sleep(get_time())

    pyautogui.moveTo(x1, y2, duration=0.1)

    pyautogui.click()

    time.sleep(get_time())


try:

    clickk(x_coordinate, y_coordinate, x_coordinate1 , y_coordinate2)


except Exception as e:
    print(f"An error occurred: {e}")

