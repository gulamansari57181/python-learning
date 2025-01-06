# Import the libraries
import cv2
import matplotlib.pyplot as plt

# Sub Task1- Load image
input_dir=r"D:/M Tech Assignments/Sem2/Image Processing/OpenCV/Task1-Water Level Detection/"
image = cv2.imread(input_dir + 'Image/bottles2.jpg')
# Display the original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Original Image")
plt.show()



# Sub Task2-Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian blur
blurred = cv2.GaussianBlur(gray, (5, 5), 0)

# Edge detection
edges = cv2.Canny(blurred, 50, 150)

# Display edges
plt.imshow(edges, cmap='gray')
plt.title("Edge Detection")
plt.show()


# Find contours
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Sort contours by area (largest to smallest)
contours = sorted(contours, key=cv2.contourArea, reverse=True)[:2]  # Top 2 contours

# Draw contours
bottles = image.copy()
cv2.drawContours(bottles, contours, -1, (0, 255, 0), 3)

plt.imshow(cv2.cvtColor(bottles, cv2.COLOR_BGR2RGB))
plt.title("Detected Bottles")
plt.show()

filled_ratios = []

for i, contour in enumerate(contours):
    # Create a mask for the current contour
    mask = cv2.drawContours(cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR), [contour], -1, (255, 255, 255), thickness=cv2.FILLED)
    mask_gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)

    # Get the region of interest (ROI) for the bottle
    x, y, w, h = cv2.boundingRect(contour)
    roi = mask_gray[y:y+h, x:x+w]

    # Calculate the ratio of non-zero pixels (filled portion) to total pixels
    filled_ratio = cv2.countNonZero(roi) / (w * h)
    filled_ratios.append((i, filled_ratio))

    print(f"Bottle {i+1} filled ratio: {filled_ratio:.2f}")

# Determine which bottle is more filled
filled_ratios.sort(key=lambda x: x[1], reverse=True)
most_filled_index = filled_ratios[0][0]
print(f"Bottle {most_filled_index+1} is more filled.")

# Highlight the most filled bottle
highlighted = image.copy()
cv2.drawContours(highlighted, [contours[most_filled_index]], -1, (0, 0, 255), 3)

plt.imshow(cv2.cvtColor(highlighted, cv2.COLOR_BGR2RGB))
plt.title(f"Bottle {most_filled_index+1} is more filled")
plt.show()
