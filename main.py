from calendar_reader import Calendar_Reader
from cut_image import Image_Crop



#validates whether the image provided is the full calendar image including the sidebar
#determines whether it needs to create a new image not containing the sidebar

img = "screenshot.png"
for x in Calendar_Reader(img).read():
    if x == "all-day":
        Image_Crop(img).crop_full_image()
        img = "screenshot2.png"
        break
Image_Crop(img).days()
print(Calendar_Reader(img).read())

#for item in self.weekdays_dict create a Calendar_Reader class that reads each day of the week.
# objs = [Calendar_Reader(f"img_{Calendar_Reader.weekdays_dict + 1}_{weekdays_dict[weekdays]}.png").read() for i in weekdays_dict]


#e.g
#objs = [Payslip_Data(p.open_file(f"payslips/{payslips[i]}"), payslips[i]) for i in range(len(p.all_payslips_data) + 1)]
# pay = []
# period_ending = []
# for obj in objs:
#   pay.append(obj.net_pay())
#   period_ending.append(obj.period_ending())
# data_dict = {
#     "pay" : pay,
#     "period ending": period_ending
# }