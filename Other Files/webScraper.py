import contextlib
from datetime import datetime
from time import sleep, time

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException,NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options=Options()
options.add_argument('--headless') # Headless chrome browser
MAX_POKEMON=240

def awaitLoad(driver, by, string):
    WebDriverWait(driver,10).until(lambda d:d.find_element(by,string))
    sleep(0.2)
    return driver.find_element(by,string)

def pokemonInfo(fileName,name,count,link):

    """Converts link to text"""

    with open(fileName,'r',encoding='utf-8') as f:
        subDriver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',options=options)
        subDriver.get(link)

        # Ensure that the evolution's list is Loaded
        WebDriverWait(subDriver, 10).until(lambda d: d.find_element(
            By.XPATH, '/html/body/div[4]/section[4]/div'))

        # Get pokemon's stats
        stats = [subDriver.find_element(By.XPATH,
            f'/html/body/div[4]/section[3]/div[1]/div[2]/ul/li[{stats}]/ul/li[1]')
            .get_attribute('data-value')for stats in range(1,7)]

        # Get pokemon's types & weaknesses
        pokemonAttr=subDriver.find_element(By.CLASS_NAME,'pokedex-pokemon-attributes').find_elements(By.TAG_NAME,'div')

        # Unpacking list
        (types,weaknesses)= [
            [
                count.text for count in pokemonAttr[counter].find_element(
                    By.TAG_NAME,'ul').find_elements(By.TAG_NAME,'a')
            ]
            for counter in range(len(pokemonAttr))
        ]

        # Check if pokemon has a choice evolution
        with contextlib.suppress(NoSuchElementException):
            for checkChoice in subDriver.find_elements(By.XPATH, '/html/body/div[4]/section[4]/div/ul/li'):
                # Compiles all choice evolutions into a list
                choiceEvol = [
                    compileEvols.find_element(By.TAG_NAME, 'h3').text.replace(
                        compileEvols.find_element(By.TAG_NAME,'span').text,'',).strip()
                    for compileEvols in checkChoice.find_element(By.CLASS_NAME,'match-height')
                    .find_elements(By.TAG_NAME, 'a')if int(compileEvols.find_element(
                        By.CLASS_NAME,'pokemon-number').text.replace('#',''))<=MAX_POKEMON
                ]

        if len(choiceEvol)==0:del choiceEvol # Prevent list comprehension w/ try-except failure from creating empty lists

        # Obtain pokemon's name and tag number
        evolList = [
            formatName.find_element(By.TAG_NAME,'h3').text.replace(
                formatName.find_element(By.TAG_NAME,'span').text,'').strip()
            for formatName in subDriver.find_elements(By.XPATH,
            '/html/body/div[4]/section[4]/div/ul/li')if int(formatName.find_element(
                By.TAG_NAME,'span').text.replace('#',''))<=MAX_POKEMON
        ]

        # Check if pokemon has a choice evolution, then merge with evolutions
        if 'choiceEvol' in locals():
            for count,insert in enumerate(evolList):
                if insert==choiceEvol[0]:
                    evolList[count]=choiceEvol

        for evolStage,evolPoke in enumerate(evolList):
            # Check if current evolution matches current name
            if evolPoke==name:
                # If current evolution stage is final, mark as final, else provide the next evolution name
                evolution='FINAL'if len(evolList)==evolStage+1 else evolList[evolStage+1]

        if'evolution'not in locals():evolution='FINAL' #Mark evolutions after choice evolutions as final

        # Quit the session & return information
        subDriver.quit()
        return(stats,types,weaknesses,evolution)


if __name__ == '__main__':
    startsFrom,fileName,startTime=1,f'pokemonInformation-{int(time())}.txt',datetime.now().strftime('%H:%M:%S')

    with open(fileName,'w',encoding='utf-8') as f:
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
        
        # Scrap the website for pokemon information to store in a file for future use
        for pokemon in driver.find_element(By.CLASS_NAME, 'results').find_elements(By.TAG_NAME,'li'):
            count,name=pokemon.find_element(By.CLASS_NAME,'id').text.replace('#',''),pokemon.find_element(By.TAG_NAME,'h5').text
            if startsFrom<=int(count)<=MAX_POKEMON:
                startedTime=time()
                (stats, types, weaknesses, evol)=pokemonInfo(fileName, name, int(count), pokemon.find_element(By.TAG_NAME, 'a').get_attribute('href'))
                
                # Progress update & output data to file
                print(f'Name: {name} #{count}\nAtk: {stats[0]}, Def: {stats[1]}, SAtk: {stats[2]}, SDef: {stats[3]}, Spd: {stats[4]}\nTypes: {" ".join(types)}, Weaknesses: {" ".join(weaknesses)}, ',end='')
                if type(evol)==list:
                    f.write(f'{count} {name:20} {"|".join(stats):20} {"|".join(types):40} {"|".join(weaknesses):40} {"|".join(evol):50}\n')
                    print(f'Evolutions: {" ".join(evol)}') # Progress update
                else:
                    f.write(f'{count} {name:20} {"|".join(stats):20} {"|".join(types):40} {"|".join(weaknesses):40} {evol:50}\n')
                    print(f'Evolution: {evol}') # Progress update
                print(f'Loaded {name} #{count}. ({round(time()-startedTime,2)}s)')

        # Quit the session
        driver.quit()
        #Output the total time used, should take around 35-40 minutes to complete
        # Due to the nature of my fast wifi network, it only took me less than 30 minutes to complete
        f.write(f'Program has finished. {datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")}')
    print(f'Program has finished. ({datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")})')

# Test cases - ignore
# print(pokemonInfo('test.txt','Eevee',133,'https://www.pokemon.com/us/pokedex/eevee'))
# print(pokemonInfo('test.txt','Ditto', 132,'https://www.pokemon.com/us/pokedex/ditto'))
# print(pokemonInfo('test.txt','Magikarp',129,'https://www.pokemon.com/us/pokedex/magikarp'))
# print(pokemonInfo('test.txt','Gyarados',130,'https://www.pokemon.com/us/pokedex/gyarados'))