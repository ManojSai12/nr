import os
from skimage import io, color
import numpy as np


input_directory = "E:\\graysacle_oct"

output_directory = "E:\\NRSC Project"

if not os.path.exists(output_directory):
    os.makedirs(output_directory)


image_files = os.listdir(input_directory)

# Process each grayscale image
for image_file in image_files:
   
    grayscale_image = io.imread(os.path.join(input_directory, image_file))

    binary_image = (grayscale_image > 45).astype(np.uint8) * 255

    output_file = os.path.join(output_directory, image_file)
    io.imsave(output_file, binary_image)

    print(f"Converted and saved {image_file}")

print("All images converted and saved.")
