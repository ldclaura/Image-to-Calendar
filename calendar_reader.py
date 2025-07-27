import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory

# https://stackoverflow.com/questions/3408097/parsing-files-ics-icalendar-using-python
class Calendar_Reader:
    """Reads screenshot of calendar"""
    def __init__(self, image):
        self.image = reader.readtext(image)
    def read(self):
        """Reads self.image\n
        returns text in image as str in tuple"""
        self.list = []
        for _ in range(len(self.image)):
            for x in self.image[_]:
                if type(x) == str:
                    self.list.append(x)
        return tuple(self.list)





# result = reader.readtext('screenshot.png')
# # print(result)
# for _ in range(len(result)):
#     for x in result[_]:
#         # print(x)
#         # print(type(x))
#         if type(x) == str:
#             print(x)
#             if x == "all-day":
#                 print("GAY") #make it so if it has "all-day" it crops it differently


#IMPORTANT
#!!!NOTE
#make it so it saves x into a list???
#then it looks through the list and sees if the list contains all:
#all-day
#10am
#11am
#etc, the sidebar crap,
#to see if you crop it or not










    # print(result[_])
    # print(type(result[_])) #tuple

    #NOTE!!!!!!
    #when installing packages with pip
    #instead of git bash
    #use command prompt 
    # bottom right of vscode, the downward arrow next to +
    # type:
    #.venv/Scipts/activate
    #then it should come up with prefix (.venv)

#it uses CPU instead of GPU
#Neither CUDA nor MPS are available - defaulting to CPU. Note: This module is much faster with a GPU.
# \Lib\site-packages\torch\utils\data\dataloader.py:665: UserWarning: 'pin_memory' argument is set as true but no accelerator is found, then device pinned memory won't be used.
#   warnings.warn(warn_msg)