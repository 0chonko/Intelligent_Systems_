'''FINAL ASSIGNMENT CREATIVE TECHNOLOGY 2020 MOD 6 '''
from Maze.src import Trackbar

'''German Savchenko s2185091'''
'''AI AND PROGRAMMING'''


import cv2
import numpy as np
from Maze.helpers.constants import Constants


class Shapes_Dec:

    def __init__(self):
        self.size = (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT)
        self.cap = cv2.VideoCapture(0 , cv2.CAP_DSHOW)
        Trackbar.init_trackBar("Trackbars")
        self.font = cv2.FONT_HERSHEY_COMPLEX
        self.centroidx = []
        self.centroidy = []
        self.xii = []
        self.yii = []


    def is_empty(self,any_structure):
        if any_structure:
            return False
        else:
            return True

    def generate_contour(self):

        while True:
            #rotate and adapt frame values
            _, frame_ = self.cap.read()
            frame = cv2.rotate(frame_, cv2.ROTATE_90_COUNTERCLOCKWISE, 1.0)
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
            cv2.resize(frame, (Constants.WINDOW_WIDTH, Constants.WINDOW_HEIGHT))

            #clear counter to keep it fresh and limited to amount of current objects
            count_object = 0

            #clear the list before starting to store new values again
            self.centroidx.clear()
            self.centroidy.clear()
            self.xii.clear()
            self.yii.clear()

            low_R , upper_R = Trackbar.updateTrackbar("Trackbars")


            # Generate mask to optimize contours detection
            mask = cv2.inRange(hsv, low_R, upper_R)
            kernel = np.ones((5, 5), np.uint8)
            mask = cv2.erode(mask, kernel)

            # Contours detection
            if int(cv2.__version__[0]) > 3:
                # Opencv 4.x.x
                contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            else:
                # Opencv 3.x.x
                _, contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                M = cv2.moments(cnt)
                if area > 400:
                    approx = cv2.approxPolyDP(cnt, 0.02 * cv2.arcLength(cnt, True), True)

                    if self.is_empty(self.grid_polygon_test(approx)) is False:
                        for i in self.grid_polygon_test(approx):
                            x, y = i
                            self.xii.append(x)
                            self.yii.append(y)


                    #define coordinates for the text along the contour
                    xs = approx.ravel()[0]
                    ys = approx.ravel()[1]

                    #save moments to calculate the center of contours
                    cX = int(M["m10"] / M["m00"])
                    cY = int(M["m01"] / M["m00"])

                    self.centroidx.append(cY)
                    self.centroidy.append(cX)

                    cv2.drawContours(frame, [approx], -1, (80, 80, 0), 1)
                    # snap_x = ndsnap(cX, maze.grid)
                    cv2.circle(frame, (cX, cY), 5, (255, 255, 255), -1)
                    cv2.putText(frame, "centroid", (cX - 25, cY - 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)

                    self.draw_text(approx, frame, xs, ys)

                    for x in range(len(approx)):
                        cv2.ellipse(frame, (approx[x][0][0], approx[x][0][1]), (5, 5), 5, 0, 360, (200, 0, 0), -1)

                    count_object += 1
            cv2.putText(frame, "n Objects", (Constants.WINDOW_WIDTH - 3, 5), self.font, 1, (0, 0, 0))

            return frame


    def draw_text(self, polygon, dest_img, text_x, text_y):
        if len(polygon) == 3:
            cv2.putText(dest_img, "Triangle", (text_x, text_y), self.font, 1, (0, 0, 0))

        elif len(polygon) == 4:
            cv2.putText(dest_img, "Rectangle", (text_x, text_y), self.font, 1, (0, 0, 0))

        elif 7 < len(polygon) < 20:
            cv2.putText(dest_img, "Circle", (text_x, text_y), self.font, 1, (0, 0, 0))



    def get_centroid_x(self):
        cdx = []
        if len(self.centroidx) >0:
            for i in self.centroidx:
                cdx.append((((i) * 40) / Constants.WINDOW_WIDTH))
                return cdx
            cdx.clear()


    def get_centroid_y(self):
        cdy = []
        if len(self.centroidx) >0:
            for i in self.centroidy:
                cdy.append((((i) * 40) / Constants.WINDOW_HEIGHT))
                return cdy
            cdy.clear()


    def get_positive_point_poligons_cords(self):
            return (self.xii, self.yii)



    def grid_polygon_test(self, generated_contour):
        cords = []
        for x in range(0,40):
            #map x and y from grid sizes to screen sizes
            x = (x * Constants.WINDOW_WIDTH) / 40
            for y in range(0,40):
                y = (y * Constants.WINDOW_HEIGHT) / 40

                dist1 = cv2.pointPolygonTest(generated_contour , (x,y), True)
                if dist1 > 0:
                    cords.append([x,y])
                else:
                    pass
        return cords
        cords.clear()
