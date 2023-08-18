import pyaudio
import wave

class VoiceRecorder:
    def __init__(self,
                 channels:int,
                 framerate:int,
                 chunk:int,
                 output_format='.mp3')->None:
        self.frames = []
        self.audio = pyaudio.PyAudio()
        self.isRecording = False
        self.channels = channels
        self.framerate = framerate
        self.chunk = chunk
        self.format = pyaudio.paInt16
        self.output_format = output_format


    def __openStream(self)->pyaudio.object:
        return self.audio.open(format=self.format,
                               channels=self.channels,
                               rate=self.framerate,
                               frames_per_buffer=self.chunk,
                               input=True)
    
    def startRecording(self)->None:
        self.isRecording = True
        stream = self.__openStream()
        while self.isRecording:
            temp_data = stream.read(self.chunk)
            self.frames.append(temp_data)
        

    def stopRecording(self)->None:
        self.isRecording = False
    
    def saveState(self):
        frames = self.frames
        self.frames = []
        return frames
    

        