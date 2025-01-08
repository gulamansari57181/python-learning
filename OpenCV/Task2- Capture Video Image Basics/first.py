import cv2

# Read the image
img = cv2.imread("bottles.jpg")


# Display the image in a window
cv2.imshow("Image", img)


# To get size of the image
print(img.shape)

# To resize the image

# img = cv2.resize(img,(640,420))

# # Display the image in a window
# cv2.imshow("Resize Image", img)

# # To get size of the image
# print(img.shape)


# To convert RGB( In opencv it refer as BGR to graysacle)

gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image", gray)

# Wait for a key press and close the window
cv2.waitKey(0)
cv2.destroyAllWindows()