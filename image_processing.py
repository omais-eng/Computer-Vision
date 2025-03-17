import cv2
import matplotlib.pyplot as plt
import numpy as np

# Load the image (ensure the correct path)
image_path = r'C:\Users\user\Desktop\Computer Vision\images\DOG 1.jpeg'
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Get image dimensions
(h, w) = image.shape[:2]

### Rotation
# Define rotation parameters
center = (w // 2, h // 2)
angle = 45  # Rotate by 45 degrees
scale = 1.0  # Keep the scale the same
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Display rotated image
rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_image_rgb)
plt.title("Rotated Image (45°)")
plt.axis("off")
plt.show()

### Scaling
# Scale the image by a factor of 1.5 (enlarging the image)
scaled_image = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)

# Display scaled image
scaled_image_rgb = cv2.cvtColor(scaled_image, cv2.COLOR_BGR2RGB)
plt.imshow(scaled_image_rgb)
plt.title("Scaled Image (1.5x)")
plt.axis("off")
plt.show()

### Translation
# Define translation matrix (shift the image 50 pixels to the right and 30 pixels down)
translation_matrix = np.float32([[1, 0, 50], [0, 1, 30]])
translated_image = cv2.warpAffine(image, translation_matrix, (w, h))

# Display translated image
translated_image_rgb = cv2.cvtColor(translated_image, cv2.COLOR_BGR2RGB)
plt.imshow(translated_image_rgb)
plt.title("Translated Image (+50x, +30y)")
plt.axis("off")
plt.show()