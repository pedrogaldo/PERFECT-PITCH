#librerias
import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import seaborn as sns

from glob import glob

import librosa
import librosa.display
import IPython.display as ipd
from itertools import cycle

#cargar archivos de audio
audio_file = glob('../Documentos/DustInTheWind/*/*.mp3')
ipd.Audio(audio_file[0])
