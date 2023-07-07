import tensorflow as tf

# 检查 GPU 是否可见
gpus = tf.config.list_physical_devices('GPU')
if gpus:
    # 设置 GPU 内存增长选项（可选）
    for gpu in gpus:
        tf.config.experimental.set_memory_growth(gpu, True)

    # 在可见的 GPU 上设置默认设备
    tf.config.experimental.set_visible_devices(gpus, 'GPU')


# Define the client and server model architectures


# Define the client and server model architectures
def create_client_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Flatten(input_shape=(28, 28)),  # Reshape input
        tf.keras.layers.Dense(10, activation='relu'),
        tf.keras.layers.Dense(10, activation='softmax')
    ])
    return model


def create_server_model():
    model = tf.keras.Sequential([
        tf.keras.layers.Dense(10, activation='relu', input_shape=(10,)),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    return model


# Define the loss and metrics
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy()
metrics = [tf.keras.metrics.SparseCategoricalAccuracy()]


# Define the federated learning process
def client_update(model, dataset, client_optimizer):
    with tf.GradientTape() as tape:
        loss = tf.keras.metrics.Mean()
        x, y = dataset
        logits = model(x)
        loss_value = loss_fn(y, logits)

    grads = tape.gradient(loss_value, model.trainable_variables)
    client_optimizer.apply_gradients(zip(grads, model.trainable_variables))
    return model


def server_update(server_model, aggregated_client_weights):
    server_model.set_weights(aggregated_client_weights)
    return server_model


# Define the Federated Averaging algorithm
def federated_averaging(server_model, client_data, client_optimizer):
    client_models = []
    for dataset in client_data:
        client_model = create_client_model()
        updated_model = client_update(client_model, dataset, client_optimizer)
        client_models.append(updated_model)

    flattened_weights = [tf.reshape(model_weights, (-1,)) for model_weights in
                         [model.trainable_variables for model in client_models]]

    aggregated_weights = tf.math.reduce_mean(flattened_weights, axis=0)
    aggregated_weights = [tf.reshape(aggregated_weights, shape=w.shape) for w in
                          client_models[0].trainable_variables]

    updated_server_model = server_update(server_model, aggregated_weights)
    return updated_server_model


# Main federated learning loop
def main():
    # Load and preprocess the dataset
    mnist_train, mnist_test = tf.keras.datasets.mnist.load_data()
    train_data = tf.data.Dataset.from_tensor_slices(mnist_train).batch(32)
    test_data = tf.data.Dataset.from_tensor_slices(mnist_test).batch(32)

    # Create the initial server model and optimizer
    server_model = create_server_model()
    client_optimizer = tf.keras.optimizers.SGD(0.1)

    # Train the federated model
    for round_num in range(10):
        server_model = federated_averaging(server_model, train_data, client_optimizer)

        # Evaluate the federated model
        if round_num % 5 == 0:
            accuracy = tf.keras.metrics.SparseCategoricalAccuracy()
            for dataset in test_data:
                x, y = dataset
                logits = server_model(x)
                accuracy.update_state(y, logits)
            print(f'Round {round_num}: {accuracy.result()}')


if __name__ == '__main__':
    main()
