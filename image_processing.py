import cv2
import matplotlib.pyplot as plt

# Load the image (make sure you have the correct path here)
image_path = r'C:\Users\user\Desktop\Computer Vision\images\DOG 1.jpeg'
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()

# Get image dimensions
(h, w) = image.shape[:2]

# Define the center of the image and the angle of rotation (e.g., 45 degrees)
center = (w // 2, h // 2)
angle = 45
scale = 1.0  # No scaling (keep the size same)

# Generate the rotation matrix
rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

# Apply the rotation to the image
rotated_image = cv2.warpAffine(image, rotation_matrix, (w, h))

# Display the rotated image
rotated_image_rgb = cv2.cvtColor(rotated_image, cv2.COLOR_BGR2RGB)
plt.imshow(rotated_image_rgb)
plt.title("Rotated Image (45°)")
plt.axis("off")
plt.show()