from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import ReLU


def get_model_slp1(n_inputs=324):
    visible = Input(shape=(n_inputs,))
    e = Dense(n_inputs)(visible)
    e = ReLU()(e)
    bottleneck = Dense(97)(e)
    output = Dense(n_inputs, activation='linear')(bottleneck)
    model = Model(inputs=visible, outputs=output)
    model.compile(optimizer='adam', loss='mse')
    return model

def get_model_2(n_inputs=97):
  visible = Input(shape=(n_inputs,))
  e = Dense(n_inputs)(visible)
  e = ReLU()(e)
  bottleneck = Dense(29)(e)
  output = Dense(n_inputs, activation='linear')(bottleneck)
  model = Model(inputs=visible, outputs=output)
  model.compile(optimizer='adam', loss='mse')
  return model