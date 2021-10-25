import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np
import pickle

def mymodel(mystr):
    with open('models/myCounter.pickle', 'rb') as inputfile: 
        token_counts=pickle.load(inputfile)
    try:
        encoder = tfds.features.text.TokenTextEncoder(token_counts)
    except AttributeError:
        encoder = tfds.deprecated.text.TokenTextEncoder(token_counts)


    new_model = tf.keras.models.load_model('models/Bidir-LSTM-full-length-seq.h5')

    # my = input('Please input a sentence:')
    a = np.array((encoder.encode(mystr),))
    result = new_model.predict(x=a)

    if result[0][0] > 0.5:
        return('it is a positive sentence!')
    else:
        return('it is a negative sentence!')