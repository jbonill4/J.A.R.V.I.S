# J.A.R.V.I.S

 A voice assitant that uses [Speech Recognintion](https://pypi.org/project/SpeechRecognition/), [PyAudio](http://people.csail.mit.edu/hubert/pyaudio/#downloads), and [pyttsx3](https://pypi.org/project/pyttsx3/). The modules pick up speech through a microphone and then convert that text into speech 
 
 # Instuctions (exclusive to MAC OS) #
 
  Make sure Python 3.4+ is installed on the machine
 
  Create a virtual environment using venv: 
  - **python3 -m venv venv**
 
  Activate virtual environment: 
  - **source venv/bin/activate**

  Install modules if they aren't already on the machine: 
   
- **pip install SpeechRecognition**
 
- **brew install portaudio**
 
- **pip install pyaudio**

Run program: 
- **python main.py**

### Warning ###
When installing portaudio I encountered an error that was fixed with the following: xcode-select --install

