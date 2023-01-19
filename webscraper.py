from selenium import webdriver;from time import time,sleep;from selenium.webdriver.chrome.options import Options;from datetime import datetime;from selenium.common.exceptions import NoSuchElementException
options=Options()
options.add_argument('--headless')
def pokemonInfo(fileName,count,link):# sourcery skip: avoid-builtin-shadow
    """Converts link to text"""
    with open(fileName,'r',encoding='utf-8') as f:
        subDriver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',chrome_options=options)
        subDriver.get(link)
        sleep(0.1)
        #Check if pokemon has evolution
        try:evo=sum(subDriver.find_element_by_xpath(f'/html/body/div[4]/section[4]/div/ul/li[{i+1}]/a/h3').text for i in range(9**99)if subDriver.find_element_by_xpath(f'/html/body/div[4]/section[4]/div/ul/li[{i}]/a/h3/span')==count)
        except NoSuchElementException:evo=None
        try:evol=subDriver.find_element_by_xpath('/html/body/div[4]/section[4]/div/ul/li[3]/ul/li[1]/a/h3/span').text
        except NoSuchElementException:evo=None
        _=[[subDriver.find_element_by_xpath(f'/html/body/div[4]/section[3]/div[1]/div[2]/ul/li[{i}]/ul/li[1]').get_attribute('data-value') for i in range(1,7)],[count.text for count in subDriver.find_element_by_class_name('dtm-type').find_element_by_tag_name('ul').find_elements_by_tag_name('a')],[count.text for count in subDriver.find_element_by_class_name('dtm-weaknesses').find_element_by_tag_name('ul').find_elements_by_tag_name('a')]]
        subDriver.quit()
        return _
if __name__ == '__main__':
    SITE='https://www.pokemon.com/us/pokedex'
    startsFrom=62
    fileName=f'pokemonInfoList-{int(time())}.txt'
    startTime=datetime.now().strftime('%H:%M:%S')
    with open(fileName,'w',encoding='utf-8') as f:
        driver=webdriver.Chrome(r'C:\Program Files\PY-Drivers\chromedriver.exe',chrome_options=options)
        driver.get(SITE)
        sleep(4)
        driver.find_element_by_xpath('//*[@id="loadMore"]/span').click()
        for _ in range(15):
            driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            print('Scrolling...')
            sleep(1)
        for pokemon in driver.find_element_by_class_name('pokedex-results').find_element_by_class_name('results').find_elements_by_tag_name('li'):
            count,name=pokemon.find_element_by_class_name('id').text,pokemon.find_element_by_tag_name('h5').text
            if int(count.replace('#',''))>=startsFrom:
                [[hp,atk,defe,satk,sdef,spd],types,weaknesses]=pokemonInfo(fileName,count,pokemon.find_element_by_tag_name('a').get_attribute('href'))
                f.write(f'{count.replace("#","")} {name:20} {atk} {defe} {satk} {sdef} {spd}{" "*8}{"|".join(types):30} {"|".join(weaknesses):30}\n')
                print(f'Name: {name} {count}\nAtk: {atk}, Def: {defe}, SAtk: {satk}, SDef: {sdef}, Spd: {spd}\nTypes: {" ".join(types)}, Weaknesses: {" ".join(weaknesses)}')
        driver.quit()
        f.write(f'Program has finished. {datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")}')
    print(f'Program has finished. ({datetime.strptime(datetime.now().strftime("%H:%M:%S"),"%H:%M:%S")-datetime.strptime(startTime,"%H:%M:%S")})')