from core import listen, speak, process_command
from config import WAKE_WORD

def run():
    speak(f"Hello, I am Manahil.")

    while True:
        command = listen()

        if not command:
            continue

        if WAKE_WORD in command:
            speak("Yes boss.")
            command = listen()

            if not command:
                continue

            response = process_command(command)
            speak(response)

if __name__ == "__main__":
    run()
