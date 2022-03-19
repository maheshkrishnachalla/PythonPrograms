from datetime import date, datetime
from dateutil.relativedelta import relativedelta


def find_date_diff(start_dt, end_dt):
    start_dt = datetime.fromisoformat(start_dt)
    end_dt = datetime.fromisoformat(end_dt)

    if end_dt > start_dt:
        diff_dt = relativedelta(end_dt, start_dt)
        return diff_dt.years, diff_dt.months, diff_dt.days
    else:
        raise Exception("{} should be less than or equal to  {}".format(start_dt, end_dt))

