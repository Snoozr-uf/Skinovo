import tensorflow as tf
import numpy as np
from PIL import Image
from huggingface_hub import hf_hub_download


MODEL_ID = "SopanhaZinII/panha1"

LABELS = [
    "Acne",
    "Dry Skin",
    "Oily Skin",
    "Dark Spots",
    "Wrinkles",
]


# Download the model file from the owner's Hugging Face repository
model_path = hf_hub_download(
    repo_id=MODEL_ID,
    filename="finetuned_best.h5"
)


# Load the owner's TensorFlow/Keras model
model = tf.keras.models.load_model(model_path)


def analyze_skin(image):

    image = image.convert("RGB")

    # The owner's model expects 224x224 RGB images
    image = image.resize((224, 224))

    image_array = np.array(
        image,
        dtype=np.float32
    )

    image_array = np.expand_dims(
        image_array,
        axis=0
    )

    predictions = model.predict(
        image_array,
        verbose=0
    )[0]

    results = {
        label: float(score)
        for label, score in zip(
            LABELS,
            predictions
        )
    }

    return results