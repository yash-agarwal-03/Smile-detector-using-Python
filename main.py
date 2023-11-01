import cv2
import pyttsx3
import datetime

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    _, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.4, 4)
    for x, y, w, h in face:
        #frame can be removed if not wanted in photos. Only present to make the functioning interactive
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 3)
        face_roi = frame[x:x+w, y:y+h]
        gray_roi = gray[x:x+w, y:y+h]
        smile = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        for x1, y1, w1, h1 in smile:
            timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            filename = f'selfie-{timestamp}.png'
            cv2.imwrite(filename, frame)
            speak("Selfie taken")

    cv2.imshow('cam star', frame)
    if cv2.waitKey(10) == 27:
        break
