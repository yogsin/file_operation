import cv2
import numpy as np

# Create a VideoCapture object and read from input file
# If the input is the camera, pass 0 instead of the video file name
cap = cv2.VideoCapture('E:/face_video/22-35/indoor/P-90/U035_C1.mp4')
def write_file(file_name, name_list):
    f = open(file_name,'w')
    for lines in name_list:
        f.write(lines + '\n')
    f.close()
# Check if camera opened successfully
if (cap.isOpened()== False): 
  print("Error opening video stream or file")

# Read until video is completed
frame_id = 0
#f = open('E:/face_video/jimmy_bill/P0/P0_0.txt','w')
while(cap.isOpened()):
  # Capture frame-by-frame
  ret, frame = cap.read()
  if ret == True:

    # Display the resulting frame
    #cv2.imshow('Frame',frame)
    if frame_id % 20 == 0:
        cv2.imwrite('E:/face_video/22-35/indoor/P-90/U035/' + str(frame_id) + '.jpg', frame)
    #f.write('E:/face_video/jimmy_bill/P0/P0/' + str(frame_id) + '.jpg\n')
    frame_id += 1
    # Press Q on keyboard to  exit
    #if cv2.waitKey(25) & 0xFF == ord('q'):
      #break

  # Break the loop
  else: 
    break
#f.close()
# When everything done, release the video capture object
cap.release()

# Closes all the frames
#cv2.destroyAllWindows()


