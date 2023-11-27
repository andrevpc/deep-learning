from keras.models import load_model
from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np
import os

def load_image(img_path, show=False):

    img = image.load_img(img_path, target_size=(64, 64))
    img_tensor = image.img_to_array(img)                    # (height, width, channels)
    img_tensor = np.expand_dims(img_tensor, axis=0)         # (1, height, width, channels), add a dimension because the model expects this shape: (batch_size, height, width, channels)
    img_tensor /= 255.                                      # imshow expects values in the range [0, 1]

    if show:
        plt.imshow(img_tensor[0])                           
        plt.axis('off')
        plt.show()

    return img_tensor

def get_classes():
    class_list = [c_name for c_name in os.listdir("./images")]
    
    return class_list

def get_best_model():
    epochs_path = ".\\epochs"

    lower_model = { 'model_path' : '', 'loss' : 1000}

    for item in os.listdir(epochs_path):
        item_path = os.path.join(epochs_path, item)

        if not os.path.isfile(item_path):
            continue

        splited = item.split("_")

        loss = splited[2]

        loss = float(loss.replace(".keras", ""))

        if loss <= lower_model['loss']:
            lower_model = { 'model_path' : item_path, 'loss' : loss }

    return lower_model['model_path'] # model = get_best_model()
        


if __name__ == "__main__":

    classes = get_classes()
    best_model_path = get_best_model()

    # # load model
    model = load_model(best_model_path)

    # # image path
    img_path = 'test4.jpg'  

    # # load a single image
    new_image = load_image(img_path)

    # # check prediction
    pred = model.predict(new_image)

    predicted_class = np.argmax(pred)
    predicted_class_name = classes[predicted_class]

    #     # Exibir a imagem
    img = image.load_img(img_path, target_size=(64, 64))
    plt.imshow(img)
    plt.title(f'Predicted Class: {predicted_class_name}')
    plt.axis('off')
    plt.show()


    # print(pred)