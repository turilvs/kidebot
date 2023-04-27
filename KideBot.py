import tkinter as tk
import tkinter.font as TkFont
from tkinter import *
from funktiot import Bot
from funktiot import Selain
from tkinter import Tk, RIGHT, BOTH, RAISED
from tkmacosx import Button as macButton
from tkmacosx import CircleButton as cButton


class Application(tk.Frame):
    # colors
    moi = "#654E92"
    text = "#2A2F4F"
    highlight = "#917FB3"

    def __init__(self):
        super().__init__()
        self.bot = Bot()
        self.configure(background="#654E92")
        self.naytto()

    # nostaa parametrina tuodun framen päällimmäiseksi
    def raiseFrame(frame):
        frame.tkraise()

    # vaihtaa nappien tilaa painettavaksi tai toisinpäin
    def switchButtonState(button):
        if (button['state'] == "normal"):
            button['state'] = "disabled"
        else:
            button['state'] = "normal"

    def changeColor(btn, colorbg, colorfg):
        if colorbg == '#4f3a78':
            btn.configure(
                overbackground='#d4c6f5',
                overforeground='#654E92',

            )
        else:
            btn.configure(
                overbackground='#654E92',
                overforeground='white',
            )
        btn.configure(
            bg=colorbg,
            fg=colorfg

        )

    # lähettää viestin käyttiksen yläosan viesti-ikkunaan
    def message(ikkuna, viesti):
        ikkuna.configure(text=viesti)

    def tulosta(laatikko, txt):
        laatikko.configure(insert=txt)

    # Luo ja palauttaa napin
    def nappi(parent, txt, tila, w, h):
        button = macButton(
            parent,
            text=txt,
            font=TkFont.Font(family="Verdana", size=14, weight="bold"),
            borderless=True,
            focusthickness=0,
            foreground='#5331A1',
            background='white',
            overbackground='#d4c6f5',
            overforeground='#5331A1',
            activebackground='#dcc2f2',
            activeforeground='white',
            disabledbackground="#917FB3",
            disabledforeground="#70618c",
            takefocus=0,
            width=w,
            height=h,
            state=tila,
        )
        return button

    # luodaan elementit käyttikseen
    def naytto(self):
        self.master.title("v.1.0.0.2   ©artturi rantala")
        self.pack(fill=BOTH, expand=True)

        # ykkösframe, softan yläosa
        frame2 = tk.Frame(self, background="#654E92", height=50, width=400)
        frame2.pack(
            side="top",
            fill=X,
            expand=False
        )

        # #kakkosframe, softan vasen sivu
        # frame2 = tk.Frame(self, background="#F5F5F5", width=100)
        # frame2.pack(
        #     fill=Y,
        #     side="left",
        #     expand=False,
        #     padx=(3,3),
        #     pady=(0,3)
        # )

        # container softan viimeiselle alueelle, oikea alaosa. tämän sisällä framet vaihtuvat
        container = tk.Frame(self, background="#654E92", width=300)
        container.pack(
            fill=BOTH,
            expand=True
        )
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        # frame ostamiseen tarvittaville napeille yms.
        frameOsta = tk.Frame(container, background="#654E92")
        frameOsta.grid(row=0, column=0, sticky="nsew")

        # frame alustamiseen tarvittaville napeille yms.
        frameAlusta = tk.Frame(container, background="#654E92")
        frameAlusta.grid(row=0, column=0, sticky="nsew")

        # #logo ja sille pohja
        # logo = Image.open("./content/KooBee.png")
        # resized_image = logo.resize((200, 50), Image.LANCZOS) #Image.ANTIALIAS
        # kideBot = ImageTk.PhotoImage(resized_image)

        # logoPohja = Label(frame1, background="#F5F5F5", image=kideBot, width=198)
        # logoPohja.image = kideBot
        # logoPohja.pack(
        #     side=LEFT,
        #     padx=(0,3)
        # )

        # #ikkuna viesteille
        # ikkuna = Message(frame1, background="#F5F5F5", fg="#000000", text="Alusta Botti", width=200)
        # ikkuna.pack(
        #     fill=BOTH,
        #     expand=True,
        #     padx=(0,0)
        # )

        # nappi, joka nostaa alustusframen sisältöineen containerin päälimmäiseksi
        avaaAlustus = Application.nappi(frame2, "Alustus", "normal", 200, 50)
        avaaAlustus.pack(side="left")
        avaaAlustus.configure(
            font=TkFont.Font(family="Verdana", size=20, weight="bold"),
            borderwidth=3,
            overbackground='',
            overforeground='',
            background='#654E92',
            foreground='white',
            command=lambda: [
                Application.raiseFrame(frameAlusta),
                Application.changeColor(avaaOsto, '#4f3a78', 'white'),
                Application.changeColor(avaaAlustus, '#654E92', 'white')
            ])

        # nappi, joka nostaa ostoframen sisältöineen containerin päälimmäiseksi
        avaaOsto = Application.nappi(frame2, "Osta", "normal", 200, 50)
        avaaOsto.pack(side="left")
        avaaOsto.configure(
            font=TkFont.Font(family="Verdana", size=20, weight="bold"),
            bg='#4f3a78',
            fg='white',
            borderwidth=3,
            command=lambda: [
                Application.raiseFrame(frameOsta),
                Application.changeColor(avaaAlustus, '#4f3a78', 'white'),
                Application.changeColor(avaaOsto, '#654E92', 'white')
            ])

        # nappi, joka avaa selaimen, ja vaihtaa kideappin avaavan napin käytettäväksi. asettaa myös itsensä tilan niin, ettei nappia voida
        # painaa uusiksi
        alustaBotti = Application.nappi(
            frameAlusta, "Alusta Botti", "normal", 200, 40)
        alustaBotti.pack(padx=2, pady=(20, 0))
        alustaBotti.configure(command=lambda: [
            Application.switchButtonState(btnEtusivu),
            Application.switchButtonState(btnTulossa),
            Application.switchButtonState(btnIlmaiset),
            Application.switchButtonState(btnSuosikit),
            Application.switchButtonState(alustaBotti),
            Selain.avaaSelain(self.bot),
            # Application.message(ikkuna, "Botti alustettu, etsi liput."),
        ])

        # nappi, joka avaa kideappin nettisivut ja vaihtaa loppujen nappien tilat käytettäväksi
        btnEtusivu = Application.nappi(
            frameAlusta, "Etusivu", "disabled", 120, 40)
        btnEtusivu.pack(padx=(0, 80), pady=(4, 0))
        btnEtusivu.configure(command=lambda: [
            Bot.avaaSivu(self.bot),
            Application.switchButtonState(osta),
            btnEtusivu.configure(command=lambda: [Bot.avaaSivu(self.bot)])
        ])

        # nappi, joka avaa liput, jotka ovat tulossa myyntiin
        btnTulossa = Application.nappi(
            frameAlusta, "Tulossa", "disabled", 120, 40)
        btnTulossa.pack(padx=(0, 80), pady=(4, 0))
        btnTulossa.configure(command=lambda: [
            Bot.avaaTulevat(self.bot),
        ])

        # nappi, joka avaa ilmaiset liput
        btnIlmaiset = Application.nappi(
            frameAlusta, "Ilmaiset", "disabled", 120, 40)
        btnIlmaiset.pack(padx=(0, 80), pady=(4, 0))
        btnIlmaiset.configure(command=lambda: [
            Bot.avaaIlmaiset(self.bot),
        ])

        # nappi, joka avaa kirjautuneen käyttäjän suosikkiliput
        btnSuosikit = Application.nappi(
            frameAlusta, "Suosikit", "disabled", 120, 40)
        btnSuosikit.pack(padx=(0, 80), pady=(4, 0))
        btnSuosikit.configure(command=lambda: [
            Bot.avaaSuosikit(self.bot),
        ])

        # pyöreä ostonappi, joka aloittaa ostoprosessin
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
            disabledbackground="#917FB3",
            disabledforeground="#70618c",
            takefocus=0,
            width=120,
            height=120,
            state="disabled",
            font=TkFont.Font(family="Verdana", size=14, weight="bold"),
        )
        osta.pack(pady=(65, 0))


def main():

    # luodaan root elementti, ja pyöräytetään tk mainloop käyntiin
    root = tk.Tk()
    root.geometry("400x300+2000+500")
    root.resizable(width=False, height=False)
    root.configure(bg="#654E92")
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()
