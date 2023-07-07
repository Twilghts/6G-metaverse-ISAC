import tensorflow as tf
import numpy as np

if __name__ == '__main__':
    # Create a sequential model
    model = tf.keras.models.Sequential()

    # Add the Conv2D layer to the model
    model.add(tf.keras.layers.Conv2D(
        16, kernel_size=(8, 8), strides=(4, 4),
        padding="valid", activation='relu'
    ))

    # Print the summary of the model
    model.summary()

