#reader
import easyocr
reader = easyocr.Reader(['en']) # this needs to run only once to load the model into memory
#writer
from icalendar import Calendar, Event
from datetime import datetime
import pytz, zoneinfo, dateutil.tz #timezone
tz = dateutil.tz.tzstr('Australia/Melbourne')


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


# Monday ('C', 'Mon 28/7', 'am', '10.30am', 'Admin', 'Monday Morning Meeting',
#  'Cain, Ashley (MSGJI78) Available', '10 am', 'TANYA SCHREIBER',
#  '10.45 am-', '1.45 am', 'Doctors', 'Ppointment', 'Ashley',
#  '(MSGI78) Blocking', 'pm', 'JASON NOWELL (6268044007) Untitled',
#  '2,30 pm', 'EMMA LINDSAY (25381170) Untitled', 'Cain,')
# Tuesday ('Tue 29/7',)
# Wednesday ('Wed 30/7', '10,30 am', 'LISA BUCHANAN (6648807709) Untited',
#  '12,30 pm', 'CAMILLE WITHNELL (9972812119)', '2 pm', 'IACKY MACDONALD (5573620) Untitled',
#  '230 pm', 'N! CORY MCHALE (5234510) Untitled DES')
# Thursday ('Thu 31/7',)
# Friday ('Fri 1/8', 'am -', '12 pm', 'Marketing', 'Ashley (MSGi78)', 'Ivailable',
#  '1:45 pm', 'NI CAMILLE SIER (671408509) Untitled DEST', '2.30 pm',
#  'MARGARET MCIVOR (448835709) Untitled', '3.30 pm',
#  'KIRK (648976509) Untidled DES', 'Cain;', 'KAREN E')

class Calendar_Writer:
    """Writes to ics file"""
    def __init__(self, image):
        self.image = image
        #e.g. 
        # Monday ('C', 'Mon 28/7', 'am', '10.30am', 'Admin', 'Monday Morning Meeting',
        #  'Cain, Ashley (MSGJI78) Available', '10 am', 'TANYA SCHREIBER',
        #  '10.45 am-', '1.45 am', 'Doctors', 'Ppointment', 'Ashley',
        #  '(MSGI78) Blocking', 'pm', 'JASON NOWELL (6268044007) Untitled',
        #  '2,30 pm', 'EMMA LINDSAY (25381170) Untitled', 'Cain,')
    def write_to_ics(self):
        cal = Calendar()
        cal.add('prodid', '-//My calendar product//mxm.dk//')
        cal.add('version', '2.0')

        event = Event()
        event.add('summary', 'Python meeting about calendaring')
        event.add('dtstart', datetime(2005,4,4,8,0,0,tzinfo=tz))
        event.add('dtend', datetime(2005,4,4,10,0,0,tzinfo=tz))
        event.add('dtstamp', datetime(2005,4,4,0,10,0,tzinfo=tz))
        event['uid'] = '20050115T101010/27346262376@mxm.dk'
        event.add('priority', 5)

        cal.add_component(event)

        f = open('example.ics', 'wb')
        f.write(cal.to_ical())
        f.close()
    def str_to_time(self):
        for _ in self.image:
            pass


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