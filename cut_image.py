import cv2

# print(img.shape) #height, width, 3??


# print(1287/5)
# print(772/9)





	
# cropped_img = img[0:772, 0:1287]

class Image_Crop:
    """uses cv2 to crop image of calendar"""
    def __init__(self, image):
        self.image = cv2.imread(image)
        self.weekdays_dict = {0: "Monday", 1: "Tuesday", 2: "Wednesday", 3: "Thursday", 4: "Friday"}
    def shape(self):
        return self.image.shape #(772, 1287, 3)
    def crop_full_image(self):
        """creates new image without the sidebar containing all-day, 8am, 9am, 10am etc\n
        use before days function if full image is provided"""
        cv2.imwrite(f"screenshot2.png", self.image[0:self.image.shape[0], 58:self.image.shape[1]])
        return cv2.imread('screenshot2.png')
    def days(self):
        """crops image of calendar into 5 separate column images\n
        by dividing the self.image by 5\n
        images will be named img_{num}_{weekday}.png"""
        x_end = round(self.image.shape[1]/5)
        x_start = 0
        for weekdays in self.weekdays_dict:
            cv2.imwrite(f"img_{weekdays + 1}_{self.weekdays_dict[weekdays]}.png", self.image[0:self.image.shape[0], x_start:x_end])
            x_start = x_end
            x_end = x_end + round(self.image.shape[1]/5)


        #--------------
#this creates too many images
#saves into separate files
# img = cv2.imread('image.png')
# for r in range(0,img.shape[0],30):
#     for c in range(0,img.shape[1],30):
#         cv2.imwrite(f"img{r}_{c}.png",img[r:r+30, c:c+30,:])