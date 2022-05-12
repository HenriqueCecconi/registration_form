from datetime import datetime
class RegistrationTime:
    def __init__(self):
        self.registration_time = datetime.today()

    def get_month_registration(self):
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'set', 'oct', 'nov', 'dec']
        # registration_time.month goes from  1-12, while index of month goes from 0-11
        return  months[self.registration_time.month - 1]

    def get_week_registration(self):
        weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        return weekdays[self.registration_time.weekday()]
