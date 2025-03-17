import cv2
import numpy as np  # Make sure numpy is imported
import matplotlib.pyplot as plt

# Step 2: Load the image
image = cv2.imread(r'C:\Users\user\Desktop\Computer Vision\images\DOG 1.jpeg')  # Make sure the image path is correct
if image is None:
    print("Error: Image not found!")
else:
    print("Image loaded successfully!")

# Step 3: Convert to RGB format
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # Convert to RGB format

# Step 4: Display the image
plt.imshow(image_rgb)
plt.title("Original Image")
plt.axis("off")
plt.show()

# Step 5: Simulate Different Camera Parameters (Focal Length)

# Define focal lengths to simulate (e.g., 50mm, 100mm, and 200mm)
focal_lengths = [50, 100, 200]

# Get the image dimensions (height and width)
(h, w) = image.shape[:2]

# Display the images with different focal lengths
plt.figure(figsize=(12, 4))  # Create a large figure to display 3 images side by side

for i, f in enumerate(focal_lengths):
    # Camera intrinsic matrix
    # This matrix defines how the camera relates 3D world coordinates to 2D image coordinates
    f_matrix = np.array([[f, 0, w // 2], [0, f, h // 2], [0, 0, 1]], dtype=np.float32)  # Convert to np.float32
    
    # Apply the perspective transformation using the focal length matrix
    warped_image = cv2.warpPerspective(image, f_matrix, (w, h))
    
    # Plot the warped image with the corresponding focal length
    plt.subplot(1, 3, i + 1)
    plt.imshow(cv2.cvtColor(warped_image, cv2.COLOR_BGR2RGB))
    plt.title(f"Focal Length: {f}")
    plt.axis("off")

plt.show()  # Display all the images at once
