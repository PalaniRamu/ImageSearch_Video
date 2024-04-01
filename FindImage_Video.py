import cv2
import numpy as np

def image_search_in_video(video_path, template_path,cnt, threshold=0.7):
    # Read the template image and video
    template = cv2.imread(template_path, cv2.IMREAD_GRAYSCALE)
    h, w = template.shape[:2]

    cap = cv2.VideoCapture(video_path)

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        cnt = cnt + 1
        # Convert the frame to grayscale
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Perform template matching
        result = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
        loc = np.where(result >= threshold)

        for pt in zip(*loc[::-1]):
            # Draw a rectangle around the matched region
            cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 1)
            cv2.imwrite('C:\\Users\\Ajay\\PycharmProjects\\Project311\\output\\Frame_'+str(cnt)+'.jpg', frame)
            cv2.imshow('Matching Frame', frame)

        # Display the result
        #cv2.imshow('Image Search in Video', frame)
        #print('Verified frame Number :'+str(cnt))
        if cv2.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
            break

    cap.release()
    cv2.destroyAllWindows()
    print('Searching process completed')


# Example usage
video_path = 'C:\\Users\\Ajay\Downloads\\KPM_CDM_0216.mp4'
template_path = 'C:\\Users\\Ajay\\Desktop\\Drone\\torus.PNG'
cnt=0
image_search_in_video(video_path, template_path,cnt)
print('Search process completed ...')

