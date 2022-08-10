#imports
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns
from glob import glob
import librosa
import librosa.display
import IPython
#from itertools import cycle

#cargar audio(s)

#espectrograma
y, sr = librosa.load('../input/prueba/pruab.mp3')
#IPython.lib.display.Audio(audio[0], rate = 22050)

#grafico de forma de onda
pd.Series(y).plot(figsize=(10, 5))

D = librosa.stft(y)
S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
S_db.shape

fig, ax = plt.subplots(figsize=(10, 5))
img = librosa.display.specshow(S_db,
                              x_axis='time',
                              y_axis='log',
                              ax=ax)
ax.set_title('espectrograma ejemplo', fontsize=20)
fig.colorbar(img, ax=ax, format=f'%0.2f')
plt.show()
