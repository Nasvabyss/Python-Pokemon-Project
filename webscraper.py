from datetime import datetime
from time import sleep, time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException,ElementNotInteractableException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

options=Options()
#options.add_argument('--headless') # Headless chrome browser
MAX_POKEMON=240
def awaitLoad(driver, by, string):
    WebDriverWait(driver,10).until(lambda d:d.find_element(by,string))
    sleep(0.2)
    return driver.find_element(by,string)
def pokemonInfo(fileName,name,count,link):    # sourcery skip: assign-if-exp, avoid-builtin-shadow, for-index-underscore, inline-immediately-returned-variable, inline-variable, low-code-quality, merge-nested-ifs, move-assign-in-block
    """Converts link to text"""
    with open(fileName,'r',encoding='utf-8') as f:
        subDriver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',options=options)
        subDriver.get(link)
        # Check if pokemon has evolution, if not, mark as final evolution
        # Then check if pokemon can evolve, if not, mark as final evolution 
        # Check if child pokemon has more than 1 parent to evolve
        # In that case, choose the first, then second, then final for the fallback
        evolution='init'
        # Obtain pokemon's name and tag number
        WebDriverWait(driver, 10).until(lambda d: d.find_element(
            By.XPATH, '/html/body/div[4]/section[4]/div'))
        evolList = [
            [
                formatName.find_element(By.TAG_NAME,'h3').text.replace(
                    formatName.find_element(By.TAG_NAME,'span').text,'').strip(),
                int(formatName.find_element(By.TAG_NAME,'span').text.replace('#',''))
            ]
            for formatName in subDriver.find_elements(By.XPATH,'/html/body/div[4]/section[4]/div/ul/li')
            if int(formatName.find_element(By.TAG_NAME,'span').text.replace('#',''))<=MAX_POKEMON
        ]
        for evolStage,evolInfo in enumerate(evolList):
            # Get pokemon's X evolution and check if it is the current pokemon (  evolInfo = [name,tagNo]  )
            if evolInfo[0] == name:
                # Check if current pokemon is at its final evolution (Adding 1 to offset the 0 index)
                # Mark evolution as final when pokemon is last in list, if not mark next pokemon in list as evolution
                evolution='FINAL'if len(evolList)==evolStage+1 else evolList[evolStage+1][0]

        # TODO Account for multiple evolution choices like evolutions of Tyrogue & Eevee
        pokemonAtt=subDriver.find_element(By.CLASS_NAME,'pokedex-pokemon-attributes').find_elements(By.TAG_NAME,'div')
        pokemonAttr = [
            [
                count.text
                for count in pokemonAtt[counter]
                .find_element(By.TAG_NAME, 'ul')
                .find_elements(By.TAG_NAME, 'a')
            ]
            for counter in range(len(pokemonAtt))
        ]
        [types,weaknesses]=pokemonAttr
        stats = [subDriver.find_element(By.XPATH, f'/html/body/div[4]/section[3]/div[1]/div[2]/ul/li[{stats}]/ul/li[1]')
                 .get_attribute('data-value') for stats in range(1, 7)]
        _=[stats,types,weaknesses,evolution]
        subDriver.quit()
        return _

# sourcery skip: de-morgan, while-to-for
if __name__ == '__main__':
    startsFrom,fileName,startTime=83,f'pokemonInfoList-{int(time())}.txt',datetime.now().strftime('%H:%M:%S')
    fileName='test.txt'
    with open(fileName,'w',encoding='utf-8') as f:
        driver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',options=options)
        driver.get('https://www.pokemon.com/us/pokedex')
        # Click to load more
        try:awaitLoad(driver,By.XPATH,'//*[@id="loadMore"]/span').click()
        except ElementNotInteractableException:awaitLoad(driver,By.XPATH,'//*[@id="loadMore"]/span').click()
        for currPokemon in range(24,MAX_POKEMON,12):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)") # Scroll to load more pokemon
            awaitLoad(driver,By.XPATH,f'/html/body/div[4]/section[5]/ul/li[{currPokemon}]')
            print(f'Scrolling completion: {round(currPokemon/(MAX_POKEMON-12)*100,1)}%')
        if len(driver.find_element(By.CLASS_NAME,'results').find_elements(By.TAG_NAME,'li'))>240:print(f'This program has loaded {len(driver.find_element(By.CLASS_NAME,"results").find_elements(By.TAG_NAME,"li"))-240} more pokemon than required. This is not an error.')
        for pokemon in driver.find_element(By.CLASS_NAME, 'results').find_elements(By.TAG_NAME,'li'):
            count,name=int(pokemon.find_element(By.CLASS_NAME,'id').text.replace('#','')),pokemon.find_element(By.TAG_NAME,'h5').text
            if startsFrom<=count<=MAX_POKEMON:
                startedTime=time()
                ((hp,atk,defe,satk,sdef,spd),types,weaknesses,evol)=pokemonInfo(fileName,name,count,pokemon.find_element(By.TAG_NAME,'a').get_attribute('href'))
                f.write(f'{count} {name:20} {atk:2}|{defe:2}|{satk:2}|{sdef:2}|{spd:2}{" "*8}{"|".join(types):30} {"|".join(weaknesses):30} {evol:20}\n')
                print(f'Loaded {name} #{count}. ({round(time()-startedTime,2)}s)')
                print(f'Name: {name} #{count}\nAtk: {atk}, Def: {defe}, SAtk: {satk}, SDef: {sdef}, Spd: {spd}\nTypes: {" ".join(types)}, Weaknesses: {" ".join(weaknesses)}, Evolution: {evol}') # Progress update
        driver.quit()
        f.write(f'Program has finished. {datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")}')
    print(f'Program has finished. ({datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")})')