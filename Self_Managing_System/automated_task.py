import pyautogui as positionMouse

positionMouse.sleep(2)
print(positionMouse.position())

positionMouse.moveTo(x=801, y=1047)
positionMouse.click(x=801, y=1047)

positionMouse.sleep(2)

positionMouse.typewrite("bloco")