import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from funktiot import Bot
from funktiot import Selain
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkmacosx import Button as macButton
from tkmacosx import CircleButton as cButton


class Application(tk.Frame):

    def __init__(self):
        super().__init__()
        self.bot = Bot()
        self.configure(background="#5e35b1")
        self.naytto()

    #nostaa containerin päällimmäiseksi halutun framen
    def raiseFrame(frame):
        frame.tkraise()
    
    #vaihtaa nappien tilaa painettavaksi tai toisinpäin
    def switchButtonState(button):
        if (button['state'] == "normal"):
            button['state'] = "disabled"
        else:
            button['state'] = "normal"

    #lähettää viestin käyttiksen yläosan viesti-ikkunaan
    def viesti(ikkuna, viesti):
        ikkuna.configure(text=viesti)


    def tulosta(laatikko, txt):
        laatikko.configure(insert=txt)
        
    #Palautetaan perus nappi
    def nappi(parent, txt, tila, w, h):
        button = macButton(
            parent,
            text=txt,
            borderless=True,
            focusthickness=0,
            foreground='#5331A1',
            background='white',
            overbackground='#d4c6f5',
            overforeground='#41189e',
            activebackground='#5F4B8B',
            activeforeground='white',
            disabledbackground="#e0dede",
            disabledforeground="#5331A1",
            takefocus=0,
            width=w,
            height=h,
            state= tila,
        )
        return button

    #luodaan elementit käyttikseen
    def naytto(self):
        self.master.title("v.1.0.0.2   © turilas")
        self.pack(fill=BOTH, expand=True)
        
        #ykkösframe, softan yläosa
        frame1 = tk.Frame(self, background="#5e35b1", height=50, width=400)
        frame1.pack(
            side="top",
            fill=X,
            expand=False,
            padx=3,
            pady=3
        )
        
        #kakkosframe, softan vasen sivu
        frame2 = tk.Frame(self, background="#F5F5F5", width=100)
        frame2.pack(
            fill=Y,
            side="left",
            expand=False,
            padx=(3,3),
            pady=(0,3)
        )

        #container softan viimeiselle alueelle, oikea alaosa. tämän sisällä framet vaihtuvat
        container = tk.Frame(self, background="#F5F5F5", width=300)
        container.pack(
            fill=BOTH,
            expand=True,
            padx=(0,3),
            pady=(0,3)
        )
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        #frame ostamiseen tarvittaville napeille yms.
        frameOsta = tk.Frame(container, background="#F5F5F5")
        frameOsta.grid(row=0, column=0, sticky="nsew")
        
        #frame alustamiseen tarvittaville napeille yms.
        frameAlusta = tk.Frame(container, background="#F5F5F5")
        frameAlusta.grid(row=0, column=0, sticky="nsew")
        
        
        #logo ja sille pohja
        logo = Image.open("/Users/Artturi/Koodaus/Python/kide_bot/content/KooBee.png")
        resized_image = logo.resize((200, 50), Image.ANTIALIAS)
        kideBot = ImageTk.PhotoImage(resized_image)

        logoPohja = Label(frame1, image=kideBot, width=198)
        logoPohja.image = kideBot
        logoPohja.pack(
            side=LEFT,
            padx=(0,3)
        )

        #ikkuna viesteille
        ikkuna = Message(frame1, text="Alusta Botti", width=200)
        ikkuna.pack(
            fill=BOTH,
            expand=True,
            padx=(0,0)
        )

        #nappi, joka nostaa alustusframen sisältöineen containerin päälimmäiseksi
        avaaAlustus = Application.nappi(frame2,"Alustus", "normal", 120, 40)
        avaaAlustus.pack(padx=2, pady=(4,8))
        avaaAlustus.configure(command=lambda: [
                Application.raiseFrame(frameAlusta),
                ])
        
        #nappi, joka nostaa ostoframen sisältöineen containerin päälimmäiseksi
        avaaOsto = Application.nappi(frame2,"Osta", "normal", 120, 40)
        avaaOsto.pack(padx=2, pady=(4,8))
        avaaOsto.configure(command=lambda: [
                Application.raiseFrame(frameOsta),
                ])

        #nappi, joka avaa selaimen ja vaihtaa 
        alustaBotti = Application.nappi(frameAlusta,"Alusta Botti", "normal", 200, 40)
        alustaBotti.pack(padx=2, pady=(4,8))
        alustaBotti.configure(command=lambda: [
                Application.switchButtonState(avaaKide),
                Application.switchButtonState(alustaBotti),
                Selain.avaaSelain(self.bot),
                Application.viesti(ikkuna, "Botti alustettu, etsi liput."),
                ])

        #nappi, joka avaa kideappin nettisivut
        avaaKide = Application.nappi(frameAlusta,"Avaa KideApp", "disabled", 200, 40)
        avaaKide.pack(padx=2, pady=(4,0))
        avaaKide.configure(command=lambda: [
                Bot.avaaSivu(self.bot),
                Application.switchButtonState(osta),
                Application.switchButtonState(btnTulossa),
                Application.switchButtonState(btnIlmaiset),
                Application.switchButtonState(btnSuosikit),
                avaaKide.configure(command=lambda: [Bot.avaaSivu(self.bot)])
                ])
        
        #nappi, joka avaa liput, jotka ovat tulossa myyntiin
        btnTulossa = Application.nappi(frameAlusta,"Tulossa", "disabled", 120, 40)
        btnTulossa.pack(padx=(78,2), pady=(4,0))
        btnTulossa.configure(command=lambda: [
                Bot.avaaTulevat(self.bot),
                ])
        
        #nappi, joka avaa ilmaiset liput
        btnIlmaiset = Application.nappi(frameAlusta,"Ilmaiset", "disabled", 120, 40)
        btnIlmaiset.pack(padx=(78,2), pady=(4,0))
        btnIlmaiset.configure(command=lambda: [
                Bot.avaaIlmaiset(self.bot),
                ])

        #nappi, joka avaa kirjautuneen käyttäjän suosikkiliput
        btnSuosikit = Application.nappi(frameAlusta,"Suosikit", "disabled", 120, 40)
        btnSuosikit.pack(padx=(78,2), pady=(4,0))
        btnSuosikit.configure(command=lambda: [
                Bot.avaaSuosikit(self.bot),
                ])

        
        lippumaara = tk.Entry(
            frameOsta,
            width= 10,
            )
        lippumaara.pack()
        
        alustaMaara = Application.nappi(frameOsta,"tallenna", "normal", 120, 40)
        alustaMaara.pack()
        alustaMaara.configure(command=lambda: [
                Bot.alustaLippumaara(self.bot, lippumaara.get()),
                ])

        osta = cButton(
            frameOsta,
            text='Osta',
            command=lambda: [Bot.v2_botti(self.bot)],
            borderless=True,
            focusthickness=0,
            foreground='#5331A1',
            background='white',
            overbackground='#d4c6f5',
            overforeground='#41189e',
            activebackground='#5F4B8B',
            activeforeground='white',
            disabledbackground="#e0dede",
            disabledforeground="#5331A1",
            takefocus=0,

            width=120,
            height=120,
            state= "disabled",
            )
        osta.pack(pady=(65,0))
        
        
def main():
    
    #luodaan root elementti, ja pyöräytetään tk mainloop käyntiin
    root = tk.Tk()
    root.geometry("400x300+100+200")
    root.resizable(width=False, height=False)
    root.configure(bg="#5F37B1")
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
