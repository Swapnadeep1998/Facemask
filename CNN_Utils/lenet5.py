from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten
from tensorflow.keras.models import Sequential


class Lenet_5(Sequential):
    def __init__(self,*args):
        super().__init__(*args)        
        self.model=Sequential([
            Conv2D(6,(5,5),activation='relu',input_shape=(32,32,3)),
            MaxPooling2D(pool_size=(2,2)),
            Conv2D(6,(5,5),activation='relu'),
            MaxPooling2D(pool_size=(2,2)),
            Flatten(),
            Dense(120,activation='relu'),
            Dense(84,activation='relu'),
            Dense(1,activation='sigmoid')
        ])
        self.model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

    def summary(self):
        return self.model.summary()

    def fit(self,train_dataset, steps_per_epoch, epochs,validation_data, validation_steps,save_model=False,model_dir=None):
        self.model.fit_generator(train_dataset,
                         steps_per_epoch=steps_per_epoch,
                         epochs=epochs,
                         validation_data=validation_data,
                         validation_steps=validation_steps)
        if save_model:
            self.model.save(model_dir)


    

    




