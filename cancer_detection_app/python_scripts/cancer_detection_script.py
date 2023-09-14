import sys
from PIL import Image
from ultralytics import YOLO

# Gets the path to the image by argument
image_path = sys.argv[1]

# Gets the path to the neural network model
model_path = "neural_network_model\\model.pt"

# Load the neural network model
model = YOLO(model_path)

# Load the image
image = Image.open(image_path)

# Perform the prediction on the image with the model
result = model.predict(source=image)

# Post-process the result
im_array = result[0].plot()

# Get the result
result_image = Image.fromarray(im_array[..., ::-1])

# Save the result
result_image.save("processed_images\\result.jpg")
