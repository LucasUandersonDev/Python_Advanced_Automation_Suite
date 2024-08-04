'''
PyAutoGUI é um módulo de automação de GUI multiplataforma
Você pode controlar o mouse e o teclado, reconhecimento básico 
de imagem para automatizar tarefas em seu computador.
'''
import pyautogui as positionMouse

# Pausa de 2 segundos 
positionMouse.sleep(2) 
# Posição do mouse 
print(positionMouse.position()) 
# Move o cursor para a posição
positionMouse.moveTo(x=801, y=1047) 
# Clica na posição definida
positionMouse.click(x=801, y=1047) 
positionMouse.sleep(2)
 # Digita o texto
positionMouse.typewrite("bloco") 