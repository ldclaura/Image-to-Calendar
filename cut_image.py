import cv2
img = cv2.imread('screenshot.png')
print(img.shape) #height, width, 3??


print(1287/5)
print(772/9)





	
cropped_img = img[0:772, 0:1287]

class Image_Crop:
    def __init__(self, image):
        self.image = cv2.imread(image)
    def shape(self):
        return self.image.shape #(772, 1287, 3)
    def crop_full_image(self):
        cv2.imwrite(f"screenshot2.png", self.image[0:self.image.shape[0], 58:self.image.shape[1]])
        return cv2.imread('screenshot2.png')
    def days(self):
        x_end = round(self.image.shape[1]/5)
        x_start = 0
        for weekdays in range(0,5):
            print(f"start {x_start} end {x_end}")
            print(x_end-x_start)
            cv2.imwrite(f"img{weekdays}.png", self.image[0:self.image.shape[0], x_start:x_end])
            print(cv2.imread(f'img{weekdays}.png').shape)
            x_start = x_end
            x_end = x_end + round(img.shape[1]/5)
Image_Crop("screenshot.png").crop_full_image()
Image_Crop("screenshot2.png").days()

        #--------------
#this creates too many images
#saves into separate files
# img = cv2.imread('image.png')
# for r in range(0,img.shape[0],30):
#     for c in range(0,img.shape[1],30):
#         cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])