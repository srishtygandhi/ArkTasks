import cv2
import numpy as np
# f = open("level1.2.txt","w")
img = cv2.imread("Level1.png",0)
print(img)

img_list = np.array(img).tolist()

for sublist in img_list:
    for item in sublist:
        print(chr(item),end='')
        # f.write(chr(item))
# f.close

# was just trying something dont know if correct or not


# import cv2
# import numpy as np

# imglvl1 = cv2.imread("Level1.png")

# print(imglvl1.shape)

# img_lvl2 = np.zeros((250,150,3), np.uint8)
# flag = 0
# for sublist in imglvl1:
#     for item in sublist:
#         # print(chr(item[0]),end='')
#         if(chr(item[0]) == ':'): 
#             print(item)
#             flag = 1
#             break
#     if(flag == 1):
#         break
#         # if(flag):
#         #     cv2.imwrite("img_lvl2.png",item)

# cv2.imshow("img",img_lvl2)
# cv2.waitKey(1000)


