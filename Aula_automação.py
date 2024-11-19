import pyautogui as auto
import time

#Pausa de 0.3 segundos (300 milisegundos)
auto.PAUSE = 0.3

#delay para rodar
time.sleep(5)

#Pegar posição do mouse
print(auto.position())

#Pegar o tamanho da tela/resolução
print(auto.size())

#Clicar com o mause
auto.click(x=606, y=1063)
auto.click(x=266, y=417)

#Clicar com notão direito do mouse
auto.click(x=266, y=417, button="right")

#Dois clicks no mouse
auto.click(x=266, y=417, clicks="2")

#duration para fazer a ação mais lentamente

#Mover o mouse 
auto.moveTo(x=672, y=229, duration=0.5)
auto.click(x=1170, y=315)

#Rolar a pagina, numero negativo = scroll para baixo
auto.scroll(-1350)
auto.click(x=940, y=990)

#funções do teclado
auto.press("win")

#Para escrever
auto.write("Clima")

auto.press("enter")

#Para arrastar o mouse dragTo 