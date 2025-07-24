import cv2
img = cv2.imread('screenshot.png')
print(img.shape) #height, width, 3??


print(1287/5)
print(772/9)





	
cropped_img = img[0:772, 0:1287]
# cv2.imwrite(f"img.png", img[0:772, 0:1287])

all_day = "all-day"

if all_day == "all-day":
    cv2.imwrite(f"screenshot2.png", img[0:772, 58:1287])
    img = cv2.imread('screenshot2.png')
x_end = round(img.shape[1]/5)
x_start = 0
for weekdays in range(0,5):
    print(f"start {x_start} end {x_end}")
    print(x_end-x_start)
    cv2.imwrite(f"img{weekdays}.png", img[0:772, x_start:x_end])
    print(cv2.imread(f'img{weekdays}.png').shape)
    x_start = x_end
    x_end = x_end + round(img.shape[1]/5)


        #--------------
#this creates too many images
#saves into separate files
# img = cv2.imread('image.png')
# for r in range(0,img.shape[0],30):
#     for c in range(0,img.shape[1],30):
#         cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])