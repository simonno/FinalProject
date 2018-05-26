import csv
import random

from sklearn.model_selection import train_test_split

from PIL import Image
import numpy as np
import pandas as pd
import xgboost as xgb

with open("classification_data.csv", "wb") as csv_file:
    writer = csv.writer(csv_file)
    newArray = []
    for i in range(1000):
        image = Image.open("Images/image" + str(i) + ".png")
        image_array = np.array(image)
        output_string = ""
        for row in image_array:
            for column in row:
                value_string = ""
                try:
                    for value in column:
                        if value < 10:
                            value_string += "00" + str(value)
                        elif value < 100:
                            value_string += "0" + str(value)
                        else:
                            value_string += str(value)
                except:
                    value_string += str(column)
                output_string += value_string + ","
            output_string += ""
        if i < 500:
            output_string += "1"
        else:
            output_string += "0"
        newArray_I = output_string.split(',')
        newArray.append(newArray_I)
        print i
    random.shuffle(newArray)
    for i in range(1000):
        writer.writerow(newArray[i])
