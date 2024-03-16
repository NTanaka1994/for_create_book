#必要なライブラリのインポート
from keras.models import Sequential
from keras.layers import Dense,Activation
from keras.layers.recurrent import LSTM
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv("1301_2017.csv", encoding="shift-jis")
v = df["終値調整値"].values
time = np.arange(0, len(v)-1, 1)

#最大値で割る
yt = v / max(v)
yt = yt.reshape(-1, 1)

#データのズレを作成
x = []
y = []
for i in range(len(yt)-25):
    x.append(time[i: i+25])
    #x.append(yt[i:i+25])
    y.append(yt[i+25])
x = np.array(x).reshape(len(x), 25, 1)
y = np.array(y).reshape(len(y), 1)

#パラメータ
n_hidden = 300
in_out_neurons = 1
length_of_sequence = x.shape[1]
future_test = x[len(x)-1].T
future_result = np.empty((0))
time_length = future_test.shape[1]

#モデル作成
model = Sequential()
model.add(LSTM(n_hidden, batch_input_shape=(None, length_of_sequence, in_out_neurons), return_sequences=False))
model.add(Dense(in_out_neurons))
model.add(Activation('linear'))
model.compile(loss="mean_squared_error", optimizer=Adam(lr=1e-3))

#学習
early_stopping = EarlyStopping(monitor="val_loss", mode="min", patience=10)
model.fit(x, y, batch_size=100, epochs=100, validation_split=1.0, callbacks=[early_stopping])

#予測
y_pred1 = model.predict(x)

#未来のデータ
test = np.arange(len(v)-1, len(v)-1+75, 1)
x_test = []
for i in range(50):
    x_test.append(test[i: i+25])
x_test = np.array(x_test).reshape(len(x_test), 25, 1)

y_pred2 = model.predict(x_test)

y_pred = np.vstack((y_pred1, y_pred2))   


plt.plot(y*max(v), label="real")
plt.plot(y_pred*max(v), label="predict")
plt.legend()
plt.show()
