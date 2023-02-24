# sourcery skip: dict-comprehension, for-index-underscore, identity-comprehension, remove-redundant-fstring
from pathlib import Path
from json import load
from time import time,sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
POKEMON_INFO_PATH = f'{Path(__file__).parent.parent.resolve()}\\Main Project\\assets\\pokemonInformation-1674801501.txt'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
# options.add_argument('--headless')  # Headless chrome browser
MAX_POKEMON = 240
link = 'https://pokemondb.net/pokedex/bulbasaur'
if __name__ == "__main__":
    startsFrom, fileName, startTime = 1, f'pokemonMoveset.json', datetime.now(
    ).strftime('%H:%M:%S')
    with open(fileName, 'w', encoding='utf-8') as f:
        driver = webdriver.Chrome(
            r'C:\Program Files\PY-Drivers\chromedriver.exe', options=options)
        driver.get(link)
        f.write('{"movesets":')
        for count in range(MAX_POKEMON):
            movesets = {}
            # Check if moveset is either physical or 
            if driver.find_element(By.XPATH,'//*[@id="tab-moves-19"]/div/div[1]/div[1]/table/tbody/tr[1]/td[4]/img').get_attribute('Status').lower() in ['physical','special']:

