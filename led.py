from tkinter import *
from time import sleep
from platform import system

#import RPi.GPIO as gpio

#gpio.setmode(gpio.BOARD)

#gpio.setup(8, gpio.OUT)
#gpio.setup(12, gpio.OUT)
#gpio.setup(18, gpio.OUT)

class inicio:

    def __init__(self):

        self.janela = Tk()
        self.janela.geometry('800x600')
        self.janela['bg'] = '#001333'

        os = system()
        if os == 'Windows':
            self.janela.state('zoomed')
        else:
            self.janela.attributes('-zoomed', True)

        self.pisca1 = False
        self.pisca2 = False
        self.pisca3 = False

        frame = Frame(self.janela, width=800, height=600, bg='#001333')
        frame.pack()

        lb1 = Label(frame, text='1º LED', font=('arial', 30, 'bold'), bg='#001333', fg='green')
        lb1.place(x=150, y=150)

        self.led1 = Button(frame, text='Desligado', font=('arial', 15, 'bold'), command = lambda: self.acender(1), bg='red', activebackground='red', fg='white', activeforeground='white', width=10)
        self.led1.place(x=150, y=350)

        lb2 = Label(frame, text='2º LED', font=('arial', 30, 'bold'), bg='#001333', fg='yellow')
        lb2.place(x=350, y=150)

        self.led2 = Button(frame, text='Desligado', font=('arial', 15, 'bold'), command = lambda: self.acender(2), bg='red', activebackground='red', fg='white', activeforeground='white', width=10)
        self.led2.place(x=350, y=350)

        lb3 = Label(frame, text='3º LED', font=('arial', 30, 'bold'), bg='#001333', fg='red')
        lb3.place(x=550, y=150)

        self.led3 = Button(frame, text='Desligado', font=('arial', 15, 'bold'), command = lambda: self.acender(3), bg='red', activebackground='red', fg='white', activeforeground='white', width=10)
        self.led3.place(x=550, y=350)

        self.led4 = Button(frame, text='Desligado', font=('arial', 15, 'bold'), command = self.verifica, bg='red', activebackground='red', fg='white', activeforeground='white', width=10)
        self.led4.place(x=0, y=0)

        self.chave = False

        self.janela.mainloop()

    def acender(self, led):

        if led == 1 and self.pisca1 == False:
            self.chave = True
            #gpio.output(8, gpio.HIGH)
            self.pisca1 = True
            self.led1['text'] = 'Ligado'
            self.led1['bg'] = 'green'
            self.led1['activebackground'] = 'green'
            print('LIGADO')

        elif led == 1 and self.pisca1 == True:
            self.chave = True         
            #gpio.output(8, gpio.LOW)
            self.pisca1 = False
            self.led1['text'] = 'Desligado'
            self.led1['bg'] = 'red'
            self.led1['activebackground'] = 'red'
            print('DESLIGADO')

        elif led == 2 and self.pisca2 == False:
            self.chave = True   
            #gpio.output(12, gpio.HIGH)
            self.pisca2 = True
            self.led2['text'] = 'Ligado'
            self.led2['bg'] = 'green'
            self.led2['activebackground'] = 'green'
            print('LIGADO')

        elif led == 2 and self.pisca2 == True:
            self.chave = True       
            #gpio.output(12, gpio.LOW)
            self.pisca2 = False
            self.led2['text'] = 'Desligado'
            self.led2['bg'] = 'red'
            self.led2['activebackground'] = 'red'
            print('DESLIGADO')

        elif led == 3 and self.pisca3 == False:
            self.chave = True
            #gpio.output(18, gpio.HIGH)
            self.pisca3 = True
            self.led3['text'] = 'Ligado'
            self.led3['bg'] = 'green'
            self.led3['activebackground'] = 'green'
            print('LIGADO')

        elif led == 3 and self.pisca3 == True:
            self.chave = True
            #gpio.output(18, gpio.LOW)
            self.pisca3 = False
            self.led3['text'] = 'Desligado'
            self.led3['bg'] = 'red'
            self.led3['activebackground'] = 'red'
            print('DESLIGADO')
    
    def verifica(self):

        if self.pisca1 == True or self.pisca2 == True or self.pisca3 == True:
            
            self.chave = False

            self.pisca1 = False
            self.pisca2 = False
            self.pisca3 = False

            self.led1['text'] = 'Desligado'
            self.led1['bg'] = 'red'
            self.led1['activebackground'] = 'red'
            self.led2['text'] = 'Desligado'
            self.led2['bg'] = 'red'
            self.led2['activebackground'] = 'red'
            self.led3['text'] = 'Desligado'
            self.led3['bg'] = 'red'
            self.led3['activebackground'] = 'red'
 
        self.c = 0

        self.brilhar()

    def brilhar(self):
        
        self.c += 1

        if self.chave == False and self.c == 1:
            #gpio.output(8, gpio.HIGH)
            #gpio.output(12, gpio.LOW)
            #gpio.output(18, gpio.LOW)
            print('1')
            if self.c == 3:
                self.c = 0

        elif self.chave == False and self.c == 2:
            #gpio.output(8, gpio.LOW)
            #gpio.output(12, gpio.HIGH)
            #gpio.output(18, gpio.LOW)
            print('2')
            if self.c == 3:
                self.c = 0

        elif self.chave == False and self.c == 3:
            #gpio.output(8, gpio.LOW)
            #gpio.output(12, gpio.LOW)
            #gpio.output(18, gpio.HIGH)
            print('3')
            if self.c == 3:
                self.c = 0
        
        if self.chave == False:        
            self.led4.after(1000, self.brilhar)


inicio()