import pyaudio
import wave
import threading

#123
FORMAT = pyaudio.paInt16

CHANNELS = 1
FRAMERATE = 44100
CHUNK = 1024


audio = pyaudio.PyAudio()
stream = audio.open(format=FORMAT, channels=CHANNELS, rate=FRAMERATE, input=True, frames_per_buffer=CHUNK)

print("Press Enter to start recording...")

l = 0
frames = []
record = True

stop_event = threading.Event()

def wait_for_input():
    global record, stop_event
    x = input('Stop?')
    if x =='y':
        record = False
        stop_event.set()

input_thread = threading.Thread(target=wait_for_input)

input_thread.start()

while record:
    if stop_event.is_set():
        break
    data = stream.read(CHUNK)
    frames.append(data)

print("Recording stopped.")

ipt = str(input('Nadaj nazwę pliku: '))
WAVE_OUTPUT_FILENAME = ipt+'.mp3'
stream.stop_stream()
stream.close()
audio.terminate()

wave_file = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wave_file.setnchannels(CHANNELS)
wave_file.setsampwidth(audio.get_sample_size(FORMAT))
wave_file.setframerate(FRAMERATE)
wave_file.writeframes(b''.join(frames))
wave_file.close()
