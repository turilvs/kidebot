from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import subprocess
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.select import Select
import os

# ÄLÄ PIDÄ MUITA VÄLILEHTIÄ CHROMELLA AUKI


class Bot:
    def __init__(self) -> None:
        self.chrome_options = ""
        self.chrome_driver = ""
        self.browser = ""

    # alustetaan botti käyttämään tiettyjä asetuksia ja driveria
    def alustaBotti(botti):
        botti.options = webdriver.ChromeOptions()
        botti.options.add_argument('--user-data-dir=/Users/artturirantala/Library/Application Support/Google/Chrome')
        # botti.options.add_argument("start-maximized")
        botti.options.add_argument("--remote-debugging-port=9222")
        botti.options.add_argument("--window-size=1920,1300")
        # botti.options.add_argument('--user-data-dir=/Users/Artturi/Library/Application Support/Google/Chrome/Default')
        
        # botti.options.add_experimental_option(
        #     "debuggerAddress", "127.0.0.1:9222"
        # )

        # tiettyä chromedriveria käyttävä versio
        # botti.driver = "/Users/artturirantala/Koodaus/Python/kide_bot/chromedriver"
        # botti.browser = webdriver.Chrome(botti.driver, options=botti.chrome_options)

        # vaihtoehtoinen, automaattisesti chromedriverin päivittävä versio
        botti.browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=botti.options)
        print("Botti alustettu!")

    # koko ostoprosessi lippujen ostoon.
    # yritetään ostaa ensimmäistä lippua, jossei voida, painetaan päivitä-nappia.
    # jossei voida painaa kideappin päivitä-nappia, yritetään ostaa lippuja
    #
    # kun ostonappia painettu, yritetään valita maksimimäärä lippuja kunnes onnistutaan
    # yritetään painaa jatka ostoksia-nappia, jolloin liput maks määrä lippuja tallentuu ostoskoriin
    # jossei onnistu, tod.näk. täyttämättömiä tietoja, jolloin 1kpl lippuja ostoskorissa -> painetaan popup ikkunan sulkevaa raksia
    #
    # yritetään lisää lippuja kunnes ostetut >= montakoLippua TAI ensimmäisen ostetun lipun jälkeen ollaan yritetty uusia lippuja tuloksetta kierros kertaa

    def v2_botti(botti):
        montakoLippua = 20
        kierros = 0
        ostetut = 0
        jatkamisYritys = 0
        ostettu = False

        xpath_paivita = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[2]/button"

        xpath_lippu1 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item/o-accent"
        xpath_lippu2 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[2]/o-accent"
        xpath_lippu3 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[3]/o-accent"
        xpath_lippu4 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[4]/o-accent"
        xpath_lippu5 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[5]/o-accent"
        xpath_lippu6 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[6]/o-accent"
        xpath_lippu7 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[7]/o-accent"
        xpath_lippu8 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[8]/o-accent"
        xpath_lippu9 = "/html/body/main/ui-view/o-page/o-section[2]/o-content/o-grid/div[2]/o-grid/div/div/o-grid/div[2]/o-material/o-list/o-item[9]/o-accent"

        xpath_jatka_ostoksia = "/html/body/o-dialog__container/o-dialog/form/o-dialog__footer/o-dialog__footer__content/button[2]"
        xpath_container = "/html/body/o-dialog__container"
        xpath_sulje_popup = "/html/body/o-dialog__container/o-dialog/form/o-dialog__header/o-dialog__header__content/button"
        xpath_lista = "/html/body/o-dialog__container/o-dialog/form/o-dialog__content/o-input-container/select"

        kaikkiLiput = [
            xpath_lippu1,
            xpath_lippu2,
            xpath_lippu3,
            xpath_lippu4,
            xpath_lippu5,
            xpath_lippu6,
            xpath_lippu7,
            xpath_lippu8,
            xpath_lippu9,
        ]
        print("\naloitetaan lippujen osto")
        while True:
            try:
                print(f"kierros numero {kierros}")
                WebDriverWait(
                    botti.browser,
                    0.05,
                    0.001,
                ).until(EC.presence_of_element_located((By.XPATH, kaikkiLiput[0])))
                jokuLippu = WebDriverWait(
                    botti.browser,
                    0.05,
                    0.001,
                ).until(EC.element_to_be_clickable((By.XPATH, kaikkiLiput[0])))
                jokuLippu.click()
                print("\nliput ostettu")
                ostettu = True
                ostetut += 1
                kaikkiLiput.pop(0)
                while True:
                    try:
                        drop_down = Select(
                            botti.browser.find_element(By.XPATH, xpath_lista)
                        )
                        liput = drop_down.options
                        maara = len(liput)
                        drop_down.select_by_visible_text(str(maara))
                        break
                    except:
                        print(".", end="")
                        continue

                while True:
                    try:
                        WebDriverWait(
                            botti.browser,
                            0.5,
                            0.001,
                        ).until(
                            EC.presence_of_element_located(
                                (By.XPATH, xpath_jatka_ostoksia)
                            )
                        )
                        jatkaOstoksia = WebDriverWait(
                            botti.browser,
                            0.5,
                            0.001,
                        ).until(
                            EC.element_to_be_clickable((By.XPATH, xpath_jatka_ostoksia))
                        )
                        jatkaOstoksia.click()
                        break
                    except:
                        print(f"yritetään jatkaa ostoksia, {jatkamisYritys}")
                        if len(kaikkiLiput) <= 0:
                            print("9 lippua yritetty, lopetetaan")
                            break
                        if jatkamisYritys > 3:
                            try:
                                WebDriverWait(
                                    botti.browser,
                                    0.5,
                                    0.001,
                                ).until(
                                    EC.presence_of_element_located(
                                        (By.XPATH, xpath_sulje_popup)
                                    )
                                )
                                suljePopup = WebDriverWait(
                                    botti.browser,
                                    0.5,
                                    0.001,
                                ).until(
                                    EC.element_to_be_clickable(
                                        (By.XPATH, xpath_sulje_popup)
                                    )
                                )
                                suljePopup.click()
                                print(
                                    "todennäköisesti täyttämättömiä tietoja, suljetaan popup"
                                )
                                break
                            except:
                                continue
                        jatkamisYritys += 1
                        continue

            except:
                if ostettu == False:
                    try:
                        paivita = WebDriverWait(botti.browser, 0.05).until(
                            EC.element_to_be_clickable((By.XPATH, xpath_paivita))
                        )
                        paivita.click()
                        print("päivitetään")
                        continue
                    except:
                        continue
                if ostetut >= montakoLippua: # or kierros >= 10
                    print("\nlopetetaan")
                    break
                kierros += 1
                print("yritetään lisää lippuja")
                continue

    # avataan kideappin sivuja
    def avaaSivu(botti):
        botti.browser.get("https://kide.app/events?filter=upcoming-sales")

    def avaaIlmaiset(botti):
        botti.browser.get("https://kide.app/fi/events?filter=free")

    def avaaTulevat(botti):
        botti.browser.get("https://kide.app/fi/events?filter=upcoming-sales")

    def avaaSuosikit(botti):
        botti.browser.get("https://kide.app/favorites")

    ###


class Selain:
    # avataan chrome portissa 9222, ja käytetään olemassa olevaa profiilia
    # kutsutaan myös botin alustusta
    def avaaSelain(botti):
        # p = subprocess.Popen('python3 KideBot.py', stdin=subprocess.PIPE, stdout=subprocess.PIPE, executable="zsh")
        # --user-data-dir="/Users/Artturi/Library/Application Support/Google/Chrome"
        call = 'Google\ Chrome --remote-debugging-port=9222 --user-data-dir="/Users/artturirantala/Library/Application Support/Google/Chrome/Default"'
        call2 = '/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --user-data-dir="/Users/artturirantala/Library/Application Support/Google/Chrome/Default"'
                                                                                                 
        
        # subprocess.Popen(call2, shell=True)
        print("Selain avattu")
        Bot.alustaBotti(botti)
