import numpy as np
import cv2
from keras.models import Sequential
from keras.layers import Dense, Activation

num_inputs=18
depth=8

image=cv2.imread('lena.png')
out = image.reshape(len(image)**2, 3)
inp = np.array(list(map(lambda x: list(("{0:"+str(num_inputs)+"b}").format(x).replace(' ', '0')), range(len(out))))) 



model = Sequential()
model.add(Dense(128, input_dim=num_inputs, activation='relu'))
for i in range(depth-1):
    model.add(Dense(128, activation='relu'))
model.add(Dense(3))


model.compile(optimizer='rmsprop',
              loss='mse')

#model.load_weights("weights.hdf5", by_name=False)
model.fit(inp, out, epochs=100, batch_size=len(inp))
model.save_weights("weights.hdf5")

#predicted_image=model.predict(inp).reshape(512,512,3)
#cv2.imwrite('a.png', predicted_image)
