import calendar
from datetime import datetime, timedelta, date


def get_first_day(dt, d_months=0, d_years=0):
    # d_years, d_months are "deltas" to apply to dt
    y, m = dt.year + d_years, dt.month + d_months
    a, m = divmod(m - 1, 12)
    return datetime(y + a, m + 1, 1)


def is_weekend(dt=date.today()):
    int_day_of_week = dt.weekday()
    day_of_week = calendar.day_name[int_day_of_week]
    if day_of_week in ["Saturday", "Sunday"]:
        return True
    else:
        return False


def is_weekday(dt=date.today()):
    int_day_of_week = dt.weekday()
    day_of_week = calendar.day_name[int_day_of_week]
    if day_of_week not in ["Saturday", "Sunday"]:
        return True
    else:
        return False


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def get_first_working_day_of_month(dt=date.today()):
    first_day_of_month = get_first_day(dt) + timedelta(days=1)
    seventh_day_of_month = first_day_of_month + timedelta(days=5)
    for d in date_range(first_day_of_month, seventh_day_of_month):
        if is_weekday(d):
            return d.date()
        else:
            continue


def is_first_working_day_of_month(dt=date.today()):
    if dt == get_first_working_day_of_month(dt):
        return True
    else:
        return False


def get_x_days_ago(current_date, n):
    return current_date - timedelta(days=n)
