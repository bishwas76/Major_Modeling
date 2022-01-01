import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import h5py

class mfcc:
    def calculate_mfcc(self,y ,n_mfcc=13, sr=22050):
        self.mfcc = librosa.feature.mfcc(y=y, n_mfcc=n_mfcc, sr=sr)
        return self.mfcc
    def calculate_delta_mfcc(self, mfcc=None, order=1):
        if mfcc.all() == None:
            mfcc = self.mfcc
        delta_mfcc = librosa.feature.delta(self.mfcc, order=2)
        return delta_mfcc
    def plot_mfcc(self, mfcc=None, sr=22050):
        if mfcc.all() == None:
            mfcc = self.mfcc
        delta_mfcc = self.calculate_delta_mfcc(mfcc=mfcc, order=1)
        delta2_mfcc = self.calculate_delta_mfcc(mfcc = mfcc, order=2)
        fig, ax = plt.subplots(nrows = 3, ncols=1, figsize=(25, 10))
        librosa.display.specshow(mfcc, 
                                 x_axis="time", 
                                 sr=sr,
                                ax=ax[0])
        librosa.display.specshow(delta_mfcc,
                                 x_axis="time",
                                 sr=sr,
                                 ax=ax[1])
        librosa.display.specshow(delta2_mfcc,
                                 x_axis="time",
                                 sr=sr,
                                 ax=ax[2])
        plt.show()
    def calculate_all_mfcc(self,y, n_mfcc=13, sr=22050, save_to_file=False, unique_id=None):
        mfcc = self.calculate_mfcc(y=y, n_mfcc=n_mfcc, sr=sr)
        delta_mfcc = self.calculate_delta_mfcc(mfcc=mfcc, order=1)
        delta2_mfcc = self.calculate_delta_mfcc(mfcc=mfcc, order=2)
        mfcc_features = np.concatenate((mfcc, delta_mfcc, delta2_mfcc))
        if save_to_file==True and not unique_id==None:
            h5f = h5py.File('data.h5', 'a')
            if unique_id in h5f:
                del h5f[unique_id]
            h5f.create_dataset(unique_id, data=mfcc_features)
            h5f.close()
        return mfcc_features
    
