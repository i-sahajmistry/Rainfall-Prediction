import pandas as pd
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import ReLU

# define encoder
def get_model(layers):
    visible = Input(shape=(layers[0],))
    e = visible
    # encoder level 1
    for layer in layers[:-1]:
        e = Dense(layer)(e)
        e = ReLU()(e)

    e = Dense(layers[-1])(e)
     
    for layer in layers[-2:0:-1]:
        e = Dense(layer)(e)
        e = ReLU()(e) 
       
    # output layer
    output = Dense(layers[0], activation='linear')(e)
    # define autoencoder model
    model = Model(inputs=visible, outputs=output)
    # compile autoencoder model
    model.compile(optimizer='adam', loss='mse')
    # plot the autoencoder
    # plot_model(model, 'autoencoder_compress.png', show_shapes=True)
    return model
