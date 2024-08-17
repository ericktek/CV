import cv2

# Open a connection to the webcam (0 is typically the default camera)
cap = cv2.VideoCapture(0)

# Check if the webcam opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Capture a single frame
ret, frame = cap.read()

# Check if the frame was captured successfully
if not ret:
    print("Error: Could not read frame.")
    cap.release()
    exit()

# Save the captured image
cv2.imwrite('captured_image.jpg', frame)

# Display the captured image
cv2.imshow('Captured Image', frame)

# Wait for a key press before closing the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# Now release the webcam
cap.release()
