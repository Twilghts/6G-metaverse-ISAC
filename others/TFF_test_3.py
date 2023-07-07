from DQN.agent import DQN
import tensorflow as tf
from tensorflow.keras import backend as K

if __name__ == '__main__':
    agent = DQN(1, 20)
    model_weights = agent.target_model.trainable_variables
    # flattened_weights = tf.reshape(model_weights, (-1,))
    # print(model_weights)
    aggregated_weights = []
    for model_weight in model_weights:
        aggregated_weights.append(tf.math.reduce_mean(model_weight, axis=0))
    print(aggregated_weights)