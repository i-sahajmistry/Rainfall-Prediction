from keras.models import Model
from keras.layers import Input
from keras.layers import Dense
from keras.layers import ReLU


def get_model(layers):
    visible = Input(shape=(layers[0],))
    e = visible

    for layer in layers[1:-1]:
        e = Dense(layer, use_bias=False)(e)
        e = ReLU()(e) 

    e = Dense(layers[-1])(e)
     
    for layer in layers[-2:0:-1]:
        e = Dense(layer)(e)
        e = ReLU()(e) 
       
    output = Dense(layers[0], activation='linear')(e)
    model = Model(inputs=visible, outputs=output)
    model.compile(optimizer='adam', loss='mse')
    return model


def full_model(layers):
    model = []
    for i in range(len(layers)):
        model.append(get_model(layers[i:i+2]))
    model.append(get_model(layers))
    return model


def train(models, x, epochs):
    for model in models:
        model.fit(x, x, epochs=epochs, batch_size=16, verbose=2, validation_data=(x,x))
        model_temp = Model(inputs=model.input, outputs=model.layers[3].output)
        x = model_temp(x)


def get_trained_model(layers, inputs):
    models = full_model(layers)
    train(models, inputs, 800)
    return models
