

import platform
import subprocess


def speak(text):
    system = platform.system()

    try:
        if system == "Darwin":  # macOS
            subprocess.run(["say", text], check=True)

        elif system == "Windows":
            command = (
                'Add-Type -AssemblyName System.Speech; '
                f'(New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak("{text}")'
            )
            subprocess.run(["powershell", "-Command", command], check=True)

        elif system == "Linux":
            subprocess.run(["espeak", text], check=True)

        else:
            print("Speech is not supported on this operating system.")

    except FileNotFoundError:
        print("Speech engine not found on this system.")


if __name__ == "__main__":
    print("Welcome to my First Project: RoboSpeaker")

    while True:
        x = input("Enter what you want me to speak (type 'exit' to quit): ").strip()

        if not x:
            continue

        if x.lower() == "exit":
            speak("Thank you for using RoboSpeaker. Have an amazing day!")
            break

        speak(x)