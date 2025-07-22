import cv2
img = cv2.imread('screenshot.png')
print(img.shape) #height, width, 3??


print(1287/5)
print(772/9)





img = cv2.imread('screenshot.png')
for r in range(0,img.shape[0],30):
    for c in range(0,img.shape[1],30):
        print(img.shape[0])
        print(img.shape[1])
        # print(img[r:r+30, c:c+30,:])
        # cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])


        #--------------
#this creates too many images
#saves into separate files
# img = cv2.imread('image.png')
# for r in range(0,img.shape[0],30):
#     for c in range(0,img.shape[1],30):
#         cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])