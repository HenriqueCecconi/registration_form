from datetime import datetime, timedelta
class RegistrationTime:
    def __init__(self):
        self.registration_time = datetime.today()

    def __str__(self):
        return self.format_date()

    def format_date(self):
        return self.registration_time.strftime('%d/%m/%Y %H:%M')

    def get_month_registration(self):
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'set', 'oct', 'nov', 'dec']
        # registration_time.month goes from  1-12, while index of month goes from 0-11
        return  months[self.registration_time.month - 1]

    def get_week_registration(self):
        weekdays = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        return weekdays[self.registration_time.weekday()]

    def time_since_register(self):
        return datetime.today() - self.registration_time
