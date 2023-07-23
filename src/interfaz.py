import tkinter as tk
from PIL import ImageTk, Image
import os
import src.algoritmo
class Interfaz:
    def __init__(self):
        self.coordFoto = [(21,648),(110,637),(136,614),(158,593),(180,569),(203,546),(212,522),(212,485),(212,450),(212,420),(176,370),(193,352),(215,330),(236,308),(256,289),(275,269),(295,250),(312,232),(331,213),(403,205),(431,202),(469,165),(502,133),(534,99),(115,305),(145,338),(176,370),(176,404),(176,431),(212,450),(232,467),(250,485),(253,525),(253,554),(253,584),(253,613),(253,643),(253,672),(53,400),(95,443),(127,475),(212,485),(250,485),(315,485),(369,474),(387,456),(405,439),(421,421),(439,403),(457,385),(475,368),(492,349),(510,332),(539,305),(588,325),(588,371),(588,476),(649,502)]
        self.nombres = ["Piraeus", "Faliro", "Moschato", "Kallithea", "Tavros", "Petrolona", "Thissio", "Monastiraki", "Omonia", "Victoria", "Attiki", "Aghios Nikolaos", "Kato Patissia", "Aghios Eleftherios", "Ano Patissia", "Perissos", "Pefkakia", "Nea Ionia", "Iraklio", "Irini", "Neratziotissa", "Maroussi", "KAT", "Kifissia","Aghios Antonios", "Sepolia", "Attiki", "Larissa Station", "Metaxourghio", "Omonia", "Panepistimio", "Syntagma", "Akropoli", "Sygrou", "Neos Kosmos", "Aghios Ioannis", "Dafni", "Aghios Dimitrios", "Egaleo", "Eleonas", "Kerameikos", "Monastiraki", "Syntagma", "Evangelismos", "Megaro Moussikis", "Ambelokipi", "Panormou", "Katehaki", "Ethniki Amyna", "Holargos", "Nomismatokopio", "Aghia Paraskevi", "Halandri", "Plakentias", "Pallini", "Kantza", "Koropi", "Airport"]
        
        self.win = tk.Tk()
        self.win.title("Shortest Path Finder")

        self.canvas1 = tk.Canvas(self.win, width=1000, height=1000)
        self.canvas1.pack()

        self.entry1 = tk.Entry(self.win)
        self.canvas1.create_window(400, 10, window=self.entry1)

        self.entry2 = tk.Entry(self.win)
        self.canvas1.create_window(600, 10, window=self.entry2)

        self.label = tk.Label(self.canvas1, text="Introduzca a la izquierda la estacion inicial y a la derecha la final")
        self.canvas1.create_window(500, 60, window=self.label)

        self.button1 = tk.Button(text='OK', command=self.get_square_root)
        self.canvas1.create_window(500, 90, window=self.button1)

        self.img = ImageTk.PhotoImage(Image.open(r".\resources\mapa.png"))
        self.canvas1.create_image(500, 500, image=self.img)

    def get_square_root(self):
        self.canvas1.create_image(500, 500, image=self.img)
        x1 = self.entry1.get()
        x2 = self.entry2.get()

        if not (x1 in self.nombres) or not (x2 in self.nombres):
            self.canvas1.create_text(500, 150, text="Error: Esa parada no existe")
            return

        posx1 = self.nombres.index(x1)
        posx2 = self.nombres.index(x2)
        lista = algoritmo.aestrella(posx1, posx2).getCamino()
        self.canvas1.create_text(500, 150, text="Se tardan " + str(algoritmo.aestrella(posx1, posx2).getTiempo()) + " minutos.")
        for i in range(len(lista) - 1):
            self.canvas1.create_line(145 + self.coordFoto[lista[i]][0], 111 + self.coordFoto[lista[i]][1],
                                145 + self.coordFoto[lista[i + 1]][0], 111 + self.coordFoto[lista[i + 1]][1],
                                fill="black", width=7)

    def run(self):
        self.win.mainloop()

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.run()

