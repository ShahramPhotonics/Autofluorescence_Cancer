
from PIL import Image
import numpy as np

# Load the original grayscale image
input_image_path = "image.png"  # Replace with your image file path
original_image = Image.open(input_image_path).convert("L")  # Convert to grayscale

# Convert the grayscale intensity to green scale
# Darker areas -> Darker Green, Lighter areas -> Lighter Green
gray_array = np.array(original_image)

# Create a new RGB array where we map the grayscale to green intensity
green_array = np.zeros((gray_array.shape[0], gray_array.shape[1], 3), dtype=np.uint8)

# Map the green channel based on the intensity of the grayscale
green_array[:, :, 1] = gray_array  # Assign the grayscale values to the green channel

# Create the final image using the mapped green array
green_image = Image.fromarray(green_array, 'RGB')

# Save the new image as image_green.png
output_image_path = "image_green.png"
green_image.save(output_image_path)

print(f"Green scale image saved as {output_image_path}")
