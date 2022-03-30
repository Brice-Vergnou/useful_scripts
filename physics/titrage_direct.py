from tkinter import *
from math import ceil, floor

class Application(Tk):
  def __init__(self, n1, n2):
    """
    n1 : nb mole de diiode
    n2 :nb mole réactif titrant
    """
    Tk.__init__(self)
    self.geometry("1200x400")
    self.anim = False
    self.ini = True
    self.n1 = n1
    self.n2 = n2 
    self.V = 0 # volume versé
    self.text0 = Label(self, text="Titrage d'une solutin de diiode par les ions thiosulfate")
    self.text0.grid(row=0,column=3)
    ##### Diiode #####
    self.can1 = Canvas(self, width=150,height=250,bg="white")
    self.can1.grid(row=1, column=1)
    self.text1=Label(self, text="")
    self.text1.grid(row=4,column=1)
    ##### Ion thiosulfate #####
    self.can2 = Canvas(self, width=150,height=250,bg="white")
    self.can2.grid(row=1, column=2)
    self.text2=Label(self, text="")
    self.text2.grid(row=4,column=2)
    ##### Ion iodure #####
    self.can3 = Canvas(self, width=150,height=250,bg="white")
    self.can3.grid(row=1, column=3)
    self.text3=Label(self, text="")
    self.text3.grid(row=4,column=3)
    ##### Ion tétrathionate #####
    self.can4 = Canvas(self, width=150,height=250,bg="white")
    self.can4.grid(row=1, column=4)
    self.text4=Label(self, text="")
    self.text4.grid(row=4,column=4)
    ## Boutons
    boutonGo = Button(self,text="GO",width=3, command=self.start)
    boutonGo.grid(row=5, column=2)
    boutonStop = Button(self,text="STOP",width=3, command=self.stop)
    boutonStop.grid(row=5, column=3)

  def start(self):
    self.anim = True
    if self.ini:
      self.V = 0
      self.creer_rectangles()
      self.p3.taille=0
      self.p4.taille=0
    self.move()

  def stop(self):
    self.anim = False
    self.ini = False

  def creer_rectangles(self):
    self.r1 = Rectangle(self.can1, 75, 220, "red", self.n1)
    self.r2 = Rectangle(self.can2, 75, 220, "blue", self.n2)
    self.p3 = Rectangle(self.can3, 75, 220, "red", 0)
    self.p4 = Rectangle(self.can4, 75, 220, "red", 0)

  def move(self):
    self.r1.dessine_rectangle()
    self.r2.dessine_rectangle()
    self.p3.dessine_rectangle()
    self.p4.dessine_rectangle()
    self.text0.configure(text="Titrage d'une solution de diiode par les ios thiosulfate\nComposition du système pour un volume versé de thiosulfate de sodium en mL:" + str(ceil(self.V)))
    self.text1.configure(text="Diiode : "+str(floor(self.r1.valeur))+" mmole")
    self.text2.configure(text="Ion thiosulfate : "+str(floor(self.r2.valeur))+" mmole")
    self.text3.configure(text="Ion iodure : "+str(floor(self.p3.valeur))+" mmole")
    self.text4.configure(text="Ion tétrathionate : "+str(floor(self.p4.valeur))+" mmole")
    self.V += 0.5 # +0.5 mL
    if (self.n1-self.V/2)>0:
      self.r1.valeur = self.n1-self.V/2
      self.p3.valeur = self.V
      self.p4.valeur = self.V/2
    if (self.n1-self.V)/2 < 0:
      self.r2.valeur = self.V-2*self.n1
    if self.anim and self.V < 25:
      self.after(250, self.move) #rafraichit toutes les 250ms
    else:
      self.V = 0
      self.ini = True


class Rectangle(object):
  def __init__(self, canvas, x, y, couleur, valeur):
    self.canvas = canvas
    self.x = x
    self.y = y
    self.couleur = couleur
    self.valeur = valeur

  def dessine_rectangle(self):
    a,b,c = self.x -20, self.y -200, self.y-self.valeur*15
    self.canvas.create_rectangle(a, c, self.x, self.y, fill=self.couleur, width=0)
    self.canvas.create_rectangle(a, b, self.x, c, fill="white", width=0)


def titrage_main():
  app = Application(12,5)