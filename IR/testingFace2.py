import os, cv2

training_videos = 'C:/Users/Hari/Videos/training_videos/'

if not os.path.exists('C:/Users/Hari/PycharmProjects/Image Recognition/for_recognizer/'):
    os.mkdir('C:/Users/Hari/PycharmProjects/Image Recognition/for_recognizer/')

for i in os.listdir(training_videos):

    video = cv2.VideoCapture('C:/Users/Hari/Videos/training_videos/' + i)
    fps = video.get(cv2.CAP_PROP_FPS)

    currentFrame = 0

    while video.isOpened():
        # Capture frame-by-frame
        ret, frame = video.read()

        if (video):
            # Write current frame
            name = 'C:/Users/Hari/PycharmProjects/IR/for_recognizer/' + str(currentFrame) + '.png'
            print('Creating...' + name)
            cv2.imwrite(name, frame)

            currentFrame += fps * 0.5
            # Skip to next 0.5 seconds
            video.set(cv2.CAP_PROP_POS_FRAMES, currentFrame)