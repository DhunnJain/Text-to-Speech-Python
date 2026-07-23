# 🎙️ RoboSpeaker

RoboSpeaker is a cross-platform Python command-line application that converts text into speech using the native speech engine available on the user's operating system.

The application automatically detects the operating system and uses the appropriate speech engine:
- **macOS** → `say`
- **Windows** → PowerShell SpeechSynthesizer
- **Linux** → `espeak`

## ✨ Features

- 🗣️ Converts user input into speech
- 💻 Cross-platform support
- 🔍 Automatic operating system detection
- ⌨️ Interactive command-line interface
- 🚪 Exit the application by typing `exit`

---

## 🛠️ Technologies Used

- Python
- `platform` module
- `subprocess` module

---

## 📂 Project Structure

```
Text-to-Speech-Python/
│
├── main.py
├── README.md
└── LICENSE
```

---

## 🚀 Installation

Clone the repository:

```bash
git clone https://github.com/DhunnJain/Text-to-Speech-Python.git
```

Navigate to the project directory:

```bash
cd Text-to-Speech-Python
```

Run the application:

```bash
python3 main.py
```

---

## 💡 Example

```
Welcome to my First Project: RoboSpeaker

Enter what you want me to speak (type 'exit' to quit):
Hello, everyone!

(RoboSpeaker speaks: "Hello, everyone!")
```

---

## 🖥️ Supported Operating Systems

| Operating System | Speech Engine |
|------------------|--------------|
| macOS | `say` |
| Windows | PowerShell SpeechSynthesizer |
| Linux | `espeak` |

> **Note:** Linux users should have `espeak` installed.

---

## 📚 Key Concepts Demonstrated

- Python functions
- User input handling
- Loops and conditional statements
- Cross-platform programming
- Operating system detection using the `platform` module
- Executing system commands with the `subprocess` module
- Basic exception handling
- Command-line application development
- Git and GitHub workflow (repository creation, commits, branches, merging, and pushing changes)

---

## 🔮 Future Improvements

- Allow users to select different voices.
- Add speech speed and volume controls.
- Build a graphical user interface (GUI).
- Read text from a file and convert it to speech.
- Save spoken text as an audio file (where supported).

  ---
  
## 📄 License

This project is licensed under the MIT License.
