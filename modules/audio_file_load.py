import os
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import librosa
import librosa.display
import scipy

class original_signal_process:
    '''
        Class for doing loading audio signal and using FFT.
    '''
    def __init__(self):
        self.file_location = './audioFiles'
    def load_signal(self, filename):
        '''
            Load audio file using librosa named `filename`
        '''
        self.path = os.path.join(self.file_location, filename + ".wav")
        self.signal, self.sr = librosa.load(self.path)
        return self.signal, self.sr
    def get_path(self):
        return self.path
    def plot_signal(self, signal=None):
        '''
        To display original signal given in Time domain
        '''
        if signal==None:
            signal=self.signal
        plt.figure(figsize=(15, 10))
        librosa.display.waveplot(signal, alpha=0.5)
        plt.show()
    def calculate_fft(self, signal=None):
        '''
            Return the absolute value of fft after being calculated.
        '''
        if signal==None:
            signal=self.signal
        self.fft=np.abs(np.fft.fft(signal))
        return self.fft
    def display_fft(self, fft_signal=None, sr=None, title="FFT", f_ratio = 1):
        '''
            Display the FFT of resultant FFT with sample rate sr
        '''
        if fft_signal==None:
            fft_signal=self.fft
        if sr == None:
            sr = self.sr
        f = np.linspace(0, sr, len(fft_signal))
        f_bins = int(len(fft_signal)*f_ratio)
        plt.plot(f[:f_bins], fft_signal[:f_bins])
        plt.xlabel('Frequency (Hz)')
        plt.title(title)
    def z_score_normalization(self, signal=None):
        '''
            Normalize the signal using z score normalization
        '''
        if signal == None:
            signal = self.signal
        mean = np.mean(signal)
        std = np.std(signal)
        a = (signal - mean) / std
        self.signal = a
        return a
class processingDataFrame:
    def __init__(self):
        self.csv_file_location = './labels/final.csv'
    def get_dataFrame(self):
        return pd.read_csv(self.csv_file_location)