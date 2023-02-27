# sourcery skip: for-index-underscore, identity-comprehension, remove-redundant-fstring
from pathlib import Path
from json import load
from time import time, sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from json import dumps
from selenium.common.exceptions import NoSuchElementException
POKEMON_INFO_PATH = f'{Path(__file__).parent.parent.resolve()}\\Main Project\\assets\\pokemonInformation-1674801501.txt'
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--headless')  # Headless chrome browser
# Get rid of annoying "Cannot find targeting attribute" & "blocked by CORS policy"
options.add_argument('--log-level=3')
MAX_POKEMON = 240
link = 'https://pokemondb.net/pokedex/bulbasaur'
if __name__ == "__main__":
    startsFrom, fileName, startTime = 1, f'pokemonMoveset-{time()}.json', datetime.now(
    ).strftime('%H:%M:%S')
    with open(fileName, 'w', encoding='utf-8') as f:
        driver = webdriver.Chrome(
            executable_path=r'C:\Program Files\PY-Drivers\chromedriver.exe', chrome_options=options)
        driver.get(link)
        f.write('{')
        for count in range(MAX_POKEMON):
            eachStart = time()
            pokemonName = driver.find_element(
                By.XPATH, '//*[@id="main"]/h1').text
            '—'
            try:
                tabMoves = 21 if driver.find_element(
                    By.XPATH, f'//*[@id="tab-moves-19"]/div/div[1]/div[1]/table/tbody/tr[1]/td[2]/a').text == '' else 19
            except NoSuchElementException:
                tabMoves = 21
            movesetLvlUp = [{"name": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[2]/a').text,
                             "level": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[1]').text,
                             "type": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[3]/a').text.capitalize(),
                             "power": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[5]').text,
                             "accuracy": '100' if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[6]').text else driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[6]').text}
                            for levelUpCount in range(len(driver.find_elements(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr')))
                            if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[4]/img')
                            .get_attribute('title').lower() in ['physical', 'special']
                            and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[5]').text != '—'
                            and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[1]/table/tbody/tr[{levelUpCount+1}]/td[6]').text != '—']
            movesetTM = [{"name": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[2]/a').text,
                          "type": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[3]/a').text.capitalize(),
                          "power": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[5]').text,
                          "accuracy": '100' if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[6]').text == '∞' else driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[6]').text}
                         for countTM in range(len(driver.find_elements(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr')))
                         if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[4]/img')
                         .get_attribute('title').lower() in ['physical', 'special']
                         and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[5]').text != '—'
                         and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[2]/div/table/tbody/tr[{countTM+1}]/td[6]').text != '—']
            movesetEgg = [{"name": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[1]/a').text,
                           "type": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[2]/a').text.capitalize(),
                           "power": driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[4]').text,
                           "accuracy": '100' if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[5]').text == '∞' else driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[5]').text}
                          for countEgg in range(len(driver.find_elements(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr')))
                          if driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[3]/img')
                          .get_attribute('title').lower() in ['physical', 'special']
                          and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[4]').text != '—'
                          and driver.find_element(By.XPATH, f'//*[@id="tab-moves-{tabMoves}"]/div/div[1]/div[2]/table/tbody/tr[{countEgg+1}]/td[5]').text != '—']
            moveset = {
                "levelUp": movesetLvlUp,
                "random": {"tm": movesetTM, "egg": movesetEgg}
            }
            f.write(f'"{pokemonName}":{dumps(moveset)}'if count ==
                    MAX_POKEMON-1 else f'"{pokemonName}":{dumps(moveset)},')

            print(
                f'{pokemonName} moveset successfully stored. ({round((time()-eachStart),2)}s)')
            driver.find_element(
                By.XPATH, '//*[@id="main"]/nav[1]').find_element(By.CLASS_NAME, 'entity-nav-next').click()
        f.write('}')
        print(
            f'Written all {MAX_POKEMON} pokemon\'s movesets successfully. ({datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")})')
