import cv2
import time

def capture():
    cam = cv2.VideoCapture(0)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
    #valid width x height values are 160x120, 176x144, 320x240, 352x288, 640x480
    while True:
        ret, frame = cam.read()
        
        if not ret:#boolean to ensure camera is reading
            raise IOError
        cv2.imshow('test', frame)
        #to get continuous live video feed from laptops webcam
        k  = cv2.waitKey(1)
        
        # if the spacebar key is been pressed
        # screenshots will be taken and after one second the camera closes
        if k%256  == 32:
            img_name = 'image.png'
            # saves the image as a png file
            cv2.imwrite(img_name, frame)
            print('screenshot taken')    
            time.sleep(1)
            break
        if k%256  == 27:
            print('exiting without taking photo')    
            break  
    # closes webcam
    cam.release()

    # stops the camera window
    cv2.destroyAllWindows()