# License: GLP
# Author: Fábio Ferraz Fernandez

import time
import picamera

from PIL import Image
import zbarlight

import Adafruit_CharLCD as LCD
import socket
import os
import time

import RPi.GPIO as GPIO
from socket import error as SocketError
from time import sleep

tempoPressionadoBtn1 = 0

# Configure IO ports
BUTTON = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(BUTTON, GPIO.IN)

# Pinos LCD x Raspberry (GPIO)
lcd_rs        = 18
lcd_en        = 23
lcd_d4        = 12
lcd_d5        = 16
lcd_d6        = 20
lcd_d7        = 21
lcd_backlight = 4

    # Define numero de colunas e linhas do LCD
lcd_colunas = 16
lcd_linhas  = 2

    # Configuracao para display 20x4
    # lcd_colunas = 20
    # lcd_linhas  = 4

    # Inicializa o LCD nos pinos configurados acima
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5,
                               lcd_d6, lcd_d7, lcd_colunas, lcd_linhas,
                               lcd_backlight)

lcd.clear()
lcd.message('Pronto para\nleitura')

#camera
def foto():
    
    with picamera.PiCamera() as camera:
        camera.start_preview()
        
        time.sleep(2)
        camera.capture('/home/pi/Pictures/teste.jpg')
        camera.stop_preview()

    #qrcode    

    file_path = './Pictures/teste.jpg'
    with open(file_path, 'rb') as image_file:
        image = Image.open(image_file)
        image.load()
    try:
        codes = zbarlight.scan_codes(['qrcode'], image) [0]
    except:
        print('erro')
 
    #imprime qr code
    try:
        lcd.clear()
        lcd.message(codes)
        # Aguarda 5 segundos
        time.sleep(7.0)

        lcd.clear()

        lcd.message('Metodos Ativos')
        lcd.message('\n de Aprendizagem')
    except:
        lcd.clear()
        lcd.message('ERRO')
        # Aguarda 5 segundos
        time.sleep(4.0)

        lcd.clear()
        lcd.message('Pronto para\nleitura')
    
while True:
    
    if GPIO.input(BUTTON) == True:
        print('botao pressionado')
        foto()
# Script starts here
#if __name__ == "__main__":
