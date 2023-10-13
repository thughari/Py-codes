import cv2

# Open the video file
cap = cv2.VideoCapture('https://github.com/intel-iot-devkit/sample-videos/raw/master/classroom.mp4')

# Create the background subtractor object
fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=True)

# Initialize variables
total_frames = 0
people_count = 0
in_frame = []
out_frame = []

while True:
    # Read a new frame
    ret, frame = cap.read()

    # If the frame is not read correctly or end of video, break the loop
    if not ret:
        break
    
    # Update the total number of frames
    total_frames += 1
    
    # Perform background subtraction
    fgmask = fgbg.apply(frame)

    # Perform morphological operations to remove noise and fill holes
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    closing = cv2.morphologyEx(fgmask, cv2.MORPH_CLOSE, kernel)
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)

    # Find contours in the foreground mask
    contours, hierarchy = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw the contours on the frame (for visualization purposes only)
    frame_contours = frame.copy()
    cv2.drawContours(frame_contours, contours, -1, (0, 255, 0), 2)

    # Loop over the contours to count people
    for contour in contours:
        # Ignore contours that are too small or too large
        if cv2.contourArea(contour) < 1000 or cv2.contourArea(contour) > 20000:
            continue
        
        # Calculate the bounding box of the contour
        (x, y, w, h) = cv2.boundingRect(contour)

        # Draw the bounding box on the frame (for visualization purposes only)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        # Check if the centroid of the contour is already being tracked
        centroid = (int(x+w/2), int(y+h/2))
        if centroid in out_frame:
            out_frame.remove(centroid)
            people_count -= 1
        elif centroid not in in_frame:
            in_frame.append(centroid)
            people_count += 1

    # Display the frame and the count
    cv2.putText(frame, "Total People: {}".format(people_count), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
    cv2.imshow('frame', frame)

    # Exit if 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()

print("Total number of frames:", total_frames)
print("Total number of people:", people_count)
