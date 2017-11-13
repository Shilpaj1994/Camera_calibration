import cv2

cap = cv2.VideoCapture(1)

while True:
    ret, frame = cap.read()
    size = frame.shape[:2]
    print(size)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 2)
    edges = cv2.Canny(frame, 100, 300)

    cv2.imshow('Gray', gray)
    cv2.imshow('Blur', blur)
    cv2.imshow('Edges', edges)
    cv2.imshow('Original', frame)

    if cv2.waitKey(1) == 27:
        break