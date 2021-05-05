from .Google_Calendar.gcalendar import *
from .Google_Drive.gDrive import *



class GoogleClient(object):

    def __init__(self, auth):
        self.google_drive = Google_Drive(auth)
        self.google_calendar = Google_Calendar(auth)
