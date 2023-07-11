import io
import random
from pathlib import Path

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

matplotlib.use('Agg')


def predict_image(input_data):
    # load model
    model_file = r"./cicapp/model/best_model_2.13.0.h5"
    model = load_model(model_file)

    # predict image
    cuisine_dict = {0: "salad", 1: "sushi", 2: "tofu"}

    image_file = io.BytesIO(input_data)
    img = image.load_img(image_file, target_size=(150, 150))

    img_tensor = image.img_to_array(img)
    img_tensor = np.expand_dims(img_tensor, axis=0)
    img_tensor /= 255.

    p = model.predict(img_tensor)[0]
    answer = np.argmax(p)
    print(f"{answer= }")

    plt.title(cuisine_dict[answer], fontsize=12)
    plt.grid()
    plt.imshow(Image.open(image_file))

    # clear wdir
    wdir_path = r"./static/wdir"

    for path in Path(wdir_path).iterdir():
        path.unlink()

    # add 10 digits prefix in order to fix browser cash problem
    result_image = str(random.randrange(10**9, 10**10)) + "_result.png"

    save_name = f"{wdir_path}/{result_image}"
    plt.savefig(save_name)
    plt.close()

    images = [Path(save_name).name]
    return cuisine_dict[answer], images
