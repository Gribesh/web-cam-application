import cv2

imgCapture = cv2.VideoCapture(0)
result = True

while(result):
    ret, frame = imgCapture.read()
    cv2.imwrite("photo.jpg", frame)
    result = False
    print("Image Captured")

imgCapture.release()
