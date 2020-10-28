from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Dropout


class AlexNet(Sequential):
    def __init__(self,*args):
        super().__init__(*args)
        self.model=Sequential([
            Conv2D(96,kernel_size=(11,11),strides=(4,4),padding='valid',input_shape=(227,227,3),activation='relu'),
            MaxPooling2D(pool_size=(3,3),strides=(2,2)),
            Conv2D(256,padding='same',kernel_size=(5,5),activation='relu'),
            MaxPooling2D(pool_size=(3,3),strides=(2,2)),
            Conv2D(384,kernel_size=(3,3),padding='same',activation='relu'),
            Conv2D(384,kernel_size=(3,3),padding='same',activation='relu'),
            Conv2D(256,kernel_size=(3,3),padding='same',activation='relu'),
            MaxPooling2D(pool_size=(3,3),strides=(2,2)),
            Flatten(),
            Dropout(0.5),
            Dense(4096,activation='relu'),
            Dropout(0.5),
            Dense(4096,activation='relu'),
            Dense(1,activation='sigmoid')
        ])
        self.model.compile(optimizer='adam',
        loss='binary_crossentropy',
        metrics=['accuracy']
        )

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

    