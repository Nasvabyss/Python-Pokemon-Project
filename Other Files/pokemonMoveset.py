# sourcery skip: dict-comprehension, identity-comprehension
from pathlib import Path
from json import load
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
POKEMON_INFO_PATH = f'{Path(__file__).parent.parent.resolve()}\\Main Project\\assets\\pokemonInformation-1674801501.txt'
options = Options()
# options.add_argument('--headless')  # Headless chrome browser
MAX_POKEMON = 240
link = 'https://pokemondb.net/pokedex/bulbasaur'
if __name__ == "__main__":
    with open(POKEMON_INFO_PATH, 'r', encoding='utf-8') as f:
        pokemonTypes = []
        # Compile the
        for type in list(f):
            if 'Program has finished.' in type:
                break
            # pokemonTypes[<name>] = <pokemonTypes>
            pokemonTypes.append(type[43:74].strip().split('|'))
    startsFrom, fileName, startTime = 1, f'pokemonMoveset-{int(time())}.json', datetime.now(
    ).strftime('%H:%M:%S')
    # TODO: Movesets
    # with open(fileName, 'w', encoding='utf-8') as f:
    #     driver = webdriver.Chrome(
    #         r'C:\Program Files\PY-Drivers\chromedriver.exe', options=options)
    #     driver.get(link)
    #     f.write('{"movesets":')
    #     for count in range(MAX_POKEMON):
    #         movesets = {}
    #         for moveset in driver.find_elements(By.XPATH, '//*[@id="tab-moves-19"]/div/div[1]/div[1]/table/tbody/tr'):
    #             if moveset.find_element(By.CLASS_NAME, 'img-fixed').get_attribute('alt').lower() in ['special', 'physical'] and moveset.find_element(
    #                     By.CLASS_NAME, 'cell-icon').find_element(By.TAG_NAME, 'a').text in pokemonTypes[count]:
    #                 movesets[moveset.find_element(By.TAG_NAME, 'ent-name').text] = (moveset.find_elements(
    #                     By.CLASS_NAME, 'cell-num')[1], moveset.find_elements(By.CLASS_NAME, 'cell-num')[2])
