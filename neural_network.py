import math
import pandas as pd
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Activation
from keras.optimizers import SGD
from keras.callbacks import ModelCheckpoint

from sklearn.feature_extraction.text import TfidfVectorizer
df = pd.read_csv("fake_or_real_news/fake_or_real_news.csv")
fake_df = pd.read_csv("fake.csv")
fale_df_text = fake_df['text']

v = TfidfVectorizer()

fale_df_text = fale_df_text.dropna()

v.fit(np.append(df['text'], fale_df_text))


fale_df_text = v.transform(fale_df_text[:700]).toarray()
# print df['text'].shape
X = v.transform(df['text']).toarray()
Y = np.array([[0,1] if i=="FAKE" else [1,0] for i in df['label']])

def model(X, Y, Xtest=[],Ytest=[]):
    limit = 7000
    X = X[:limit]
    Y = Y[:limit]
    input_size = len(X)
    split = int(0.7*input_size)

    x_train = X[:split]
    y_train = Y[:split]
    if(len(Xtest) and len(Ytest)):
        print "EXTERNAL DATA"
        x_test = Xtest
        y_test = Ytest
    else:
        x_test = X[split:]
        y_test = Y[split:]
    
    model = Sequential()

    model.add(Dense(256, activation='linear', input_dim=len(X[0])))
    model.add(Dropout(0.5))
	# model.add(Dense(1, activation='linear'))
    model.add(Dense(2, activation='softmax'))

    sgd = SGD(lr=0.08, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy',
            optimizer=sgd,
            metrics=['accuracy'])
    checkpoint = ModelCheckpoint(filepath='./checkpoints/checkpoint-{epoch:02d}-{loss:.2f}.hdf5')

    model.fit(x_train, y_train,
            epochs=5,
            batch_size=32,
            verbose=1,
            callbacks=[checkpoint])
    score = model.evaluate(x_test, y_test, batch_size=32)
    print score

# model(X, Y, fale_df_text, [[0,1] for i in fale_df_text])
model(X, Y)

