from tensorflow.keras.applications.vgg16 import VGG16 
from tensorflow.keras.layers import Dense, Flatten
from tensorflow.keras.models import Model


class Pretrained_VGG16:
    def __init__(self,shape=None):        
        self.model=VGG16(input_shape=shape,weights='imagenet',include_top=False)
        for layer in self.model.layers:
            layer.trainable=False 
        self.x=Flatten()(self.model.output)
        self.predictions=Dense(units=1,activation='sigmoid')(self.x)
        self.final_model=Model(inputs=self.model.input,outputs=self.predictions)
        self.final_model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
    def summary(self):
        return self.final_model.summary()
    
    def fit(self,train_dataset,validation_dataset,epochs,steps_per_epoch,validation_steps,save_model=False,model_dir=None):
        self.final_model.fit_generator(train_dataset,
                         steps_per_epoch=steps_per_epoch,
                         epochs=epochs,
                         validation_data=validation_dataset,
                         validation_steps=validation_steps)
        if save_model:
            self.final_model.save(model_dir)


        
