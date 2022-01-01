import librosa
import librosa.display
import numpy as np
import matplotlib.pyplot as plt

class stft:
    '''
        Calculate Short Term Fourier Transfrom and displaying the STFT in linear and log scale
        frame_size:- frame size of the FT to be calculated. Default:- 2048
        hop_length:- hoping length to get next frame in FT. Default:- 512
        
        Functions:-
            1) calculate_stft(self, signal, frame_size=None, hop_length=None)
                Actually calculates the stft
                signal:- Signal of which we will find STFT
                frame_size:- frame size of the FT to be calculated. Default:- None (Will be set according to class's value if given with the constructor)
                hop_length:- hoping length to get next frame in FT. Default:- None (Will be set according to class's value if given with the constructor)
            2) calcuate_spectrogram(self, stft)
                calculate the spectrogram value of the stft.
                    Formula.
                       |stft|^2
                stft:- value of short term fourier transform. Default:- None (Will be set according to class's value if given with the constructor)
            3) display_spectrogram(self, Y=None, sr=None, hop_length=None, y_axis='linear')
                Display the calculated spectrogram.
                Y:- Value of calculated Spectrogram. Default: None (Will be set according to function calculated spectrogram if run before)
                sr:- Sample rate of the signal. This value is must. 
                hop_length: Hop Length of the given signal. Default: None (Will be set according to class's value if given with the constructor)
                y_axis:- shows how to display the data according to the scale. Default: linear. In the case of log. the Y value is changed into log scale too
    '''
    def __init__(self, frame_size=2048, hop_length=512):
        self.frame_size=frame_size
        self.hop_length=hop_length
    def calculate_stft(self,signal, frame_size=None, hop_length=None):
        '''
            calculate_stft(self, signal, frame_size=None, hop_length=None)
                Actually calculates the stft
                signal:- Signal of which we will find STFT
                frame_size:- frame size of the FT to be calculated. Default:- None (Will be set according to class's value if given with the constructor)
                hop_length:- hoping length to get next frame in FT. Default:- None (Will be set according to class's value if given with the constructor)
        '''
        if frame_size==None:
            frame_size=self.frame_size
        if hop_length==None:
            hop_length=self.hop_length
        self.S_scale = librosa.stft(signal, n_fft=frame_size, hop_length=hop_length)
        return self.S_scale
    def calculate_spectrogram(self, stft=None):
        '''
            calculate the spectrogram value of the stft.
                    Formula.
                       |stft|^2
                stft:- value of short term fourier transform. Default:- None (Will be set according to class's value if given with the constructor)
        '''
        if stft == None:
            stft=self.S_scale
        self.Y_scale = np.abs(stft) ** 2
        return self.Y_scale
    def display_spectrogram(self, Y=None, sr=None, hop_length=None, y_axis='linear'):
        '''
        Display the calculated spectrogram.
                Y:- Value of calculated Spectrogram. Default: None (Will be set according to function calculated spectrogram if run before)
                sr:- Sample rate of the signal. This value is must. 
                hop_length: Hop Length of the given signal. Default: None (Will be set according to class's value if given with the constructor)
                y_axis:- shows how to display the data according to the scale. Default: linear. In the case of log. the Y value is changed into log scale too
        '''
        if(Y==None):
            Y=self.Y_scale
        if(hop_length==None):
            hop_length = self.hop_length
        if(sr == None):
            return "Error"
        if(y_axis=='log'):
            Y = librosa.power_to_db(Y)
        plt.figure(figsize=(25, 10))
        librosa.display.specshow(Y, 
                                 sr=sr, 
                                 hop_length=hop_length, 
                                 x_axis="time", 
                                 y_axis=y_axis)
        plt.colorbar(format="%+2.f")
        plt.plot()