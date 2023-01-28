from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webScraper import awaitLoad

options=Options()
options.add_argument('--headless') # Headless chrome browser
MAX_POKEMON=240
if __name__ == '__main__':
    with open('config.json','w',encoding='utf-8') as f:
        driver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',options=options)
        driver.get('https://www.pokemon.com/us/pokedex')

        # Click 'Load More' button, failure to click will result in another 10 second timeout (Highly unlikely unless you've got bad internet)
        try:awaitLoad(driver,By.XPATH,'//*[@id="loadMore"]/span').click()
        except ElementNotInteractableException:awaitLoad(driver,By.XPATH,'//*[@id="loadMore"]/span').click()

        # Scrolling to load pokemon elements required
        for currPokemon in range(24,MAX_POKEMON+12,12):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # Scroll to load more pokemon
            awaitLoad(driver,By.XPATH,f'/html/body/div[4]/section[5]/ul/li[{currPokemon}]')
            print(f'Scrolling completion: {round(currPokemon/MAX_POKEMON*100,1)}%')

        # Produce an Assertion Error if the program did not load the default 240 pokemon required
        assert len(driver.find_element(By.CLASS_NAME,"results").find_elements(By.TAG_NAME,"li"))>=MAX_POKEMON,f'ERROR! This program only managed to load {len(driver.find_element(By.CLASS_NAME,"results").find_elements(By.TAG_NAME,"li"))} of the {MAX_POKEMON} required pokemon, please contact the software developer.'
        paths = {
            str(i.find_element(By.TAG_NAME, 'h5').text):
            str(i.find_element(By.TAG_NAME, 'img')
            .get_attribute('src'))
            for i in driver.find_element(By.CLASS_NAME,
            'results').find_elements(By.TAG_NAME, 'li')
        }
        f.write('{"pokemonPaths":'+str(paths).replace("'", '"')+'}')