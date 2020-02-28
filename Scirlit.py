# edx skirlit
from sklearn.feature_extraction.text import CountVectorizer
corpus = [ "Authman ran faster than Harry because he is an athlete.","Authman and Harry ran faster and faster."]
bow =  CountVectorizer()
X = bow.fit_transform(corpus)    # Sparse Matrix
print(  bow.get_feature_names()  )
print ( X.toarray())

print("Explanation:")
print("Some new points of interest. X is not the regular [n_samples, n_features] dataframe you are used to. Rather, it is a SciPy compressed, sparse, row matrix. SciPy is a collection of mathematical algorithms and convenience functions that further extend NumPy. The reason X is now a sparse matrix instead of a classical dataframe is because even with this small example of two sentences, 11 features were created. The average English speaker knows around 8000 unique words. If each sentence were to be an 8000 vector sample in your dataframe, consisting mostly of 0's, it would be a poor use of memory.")

# Image analysis
# Output of example belows depends on imageDatei

# Uses the Image module (PIL)
from scipy import misc

# Load the image up
imageDatei = "C:\\Users\\Public\\Documents\\Pub_CodeDev\\Python\\TestDataPandas\\CourseGoldenRatio.png"
img = misc.imread(imageDatei)

# Is the image too big? Shrink it by an order of magnitude
img = img[::2, ::2]

# Scale colors from (0-255) to (0-1), then reshape to 1D Array
X = (img / 255.0).reshape(-1, 3)

# To-Do: Machine Learning with X!
#

## Audio analysis
print("Audio can be encoded with similar methods as graphical features, with the caveat that your 'audio-image' is already a one-dimensional waveform data type instead of a two-dimensional array of pixels. Rather than looking for graphical gradients, you would look for auditory ones, such as the length of sounds, power and noise ratios, and histogram counts after applying filters.")

import scipy.io.wavfile as wavfile

sample_rate, audio_data = wavfile.read('sound.wav')
print ("audio_data")  # Sollte ohneparathis gehen

# To-Do: Machine Learning with audio_data!
#
