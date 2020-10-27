import cv2 as cv
import numpy as np

area_map = cv.imread(r'C:\Users\Mat\PycharmProjects\OpenCV\Waldo\waldomap1.jpg', cv.IMREAD_UNCHANGED)
waldo_face = cv.imread(r'C:\Users\Mat\PycharmProjects\OpenCV\Waldo\waldoface.png', cv.IMREAD_UNCHANGED)

results = cv.matchTemplate(area_map, waldo_face, cv.TM_CCOEFF_NORMED)

min_val, max_val, min_loc, max_loc = cv.minMaxLoc(results)

print('The best top left position is: %s' % str(max_loc))
print('The best bottom right position is: %s' % str(min_loc))
print("Odds %s" % str(max_val))

threshold = 0.5
if max_val >= threshold:
    print("I found waldo!")

    waldo_face_h = waldo_face.shape[0]
    waldo_face_w = waldo_face.shape[1]
    
    top_left = max_loc
    bottom_right = (top_left[0] + waldo_face_w, top_left[1] + waldo_face_h)
    
    cv.rectangle(area_map, top_left, bottom_right, color=(0, 255, 0), thickness=2, lineType=cv.LINE_4)
    
    cv.imshow("Waldo", area_map)
    cv.waitKey(0)
    
else:
    print("Waldo is not here!")

