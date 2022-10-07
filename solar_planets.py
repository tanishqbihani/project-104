import cv2
import os


img = cv2.imread("solar-system.jpg")


cv2.putText(img,
            "Sun",
            (70,230),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

cv2.putText(img,
            "Mercury",
            (100,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Venus",
            (190,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Earth",
            (280,270),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Mass",
            (380,260),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Jupiter",
            (470,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Saturn",
            (700,110),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Uranus",
            (960,130),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)
cv2.putText(img,
            "Neptune",
            (1100,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,255,255)
)

#print(img)
cv2.imshow("Display Image",img)
cv2.imwrite("solar-system.jpg",img)
cv2.waitKey(0)