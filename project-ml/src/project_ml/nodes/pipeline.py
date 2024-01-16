# ECHO is on.

# src/<your_project_name>/nodes/pipeline.py
from kedro.pipeline import node, Pipeline
from nodes.pipeline import dataset_node, model_node


def create_pipeline(**kwargs):
    return Pipeline(
        [
            node(
                dataset_node,
                inputs="sp500",
                outputs=["sp500_train_x", "sp500_train_y", "sp500_test_x", "sp500_test_y"],
            ),
            node(
                model_node,
                inputs= Model():
                         model = tf.keras.models.Sequential([
                                      tf.keras.layers.LSTM(200, input_shape = (5, 1), activation = tf.nn.leaky_relu, return_sequences = True),
                                      tf.keras.layers.LSTM(200, activation = tf.nn.leaky_relu),
                                      tf.keras.layers.Dense(200, activation = tf.nn.leaky_relu),
                                      tf.keras.layers.Dense(100, activation = tf.nn.leaky_relu),
                                      tf.keras.layers.Dense(50, activation = tf.nn.leaky_relu),
                                      tf.keras.layers.Dense(5, activation = tf.nn.leaky_relu)
                                      ])
                         return model,
                outputs= model,
            )
        ]
    )

