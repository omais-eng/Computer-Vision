import cv2
import matplotlib.pyplot as plt

# Correct path to the image (with .jpeg extension)
image_path = r'C:\Users\user\Desktop\Computer Vision\images\DOG 1.jpeg'

# Load the image
image = cv2.imread(image_path)

# Check if the image was loaded properly
if image is None:
    print(f"Error: Could not load image from {image_path}")
    exit()  # Exit the program if the image cannot be loaded

# Convert the image to RGB format (OpenCV loads images in BGR format by default)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Display the original image
plt.imshow(image_rgb)
plt.title("Original Image (DOG 1.jpeg)")
plt.axis("off")  # Hide axis for better display
plt.show()