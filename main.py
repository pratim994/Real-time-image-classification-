import cv2 as cv 

cap = cv.VideoCapture(0)

if not cap.isOpenend():
    print("Can't access camera please turn it on")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error failed to grab a frame ")
        break

    cv.imshow('live camera feed', frame)

    if cv.waitKey(1)&0xFF == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


