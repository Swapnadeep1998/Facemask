import numpy as np 
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model
import gc
import os 
import psutil 
import tensorflow as tf

class FaceMask:
    def __init__(self,filename):        
        self.filename=filename          
        self.model=load_model('facemask_VGG16.h5')  
         

    def classify(self):            
                     
        imagename=self.filename
        test_img=image.load_img(imagename,target_size=(150,150))
        test_img=image.img_to_array(test_img)              
        test_img=np.expand_dims(test_img,axis=0)
        result=self.model.predict(test_img)                    
        
        tf.keras.backend.clear_session()
        gc.collect()

        process=psutil.Process(os.getpid())
        mem_used=process.memory_info()[0] >> 20        
        
        if result[0][0]==1:
            pred='Without Mask'
        else:
            pred='With Mask'

        return {'image': pred,'memory_used':mem_used}






