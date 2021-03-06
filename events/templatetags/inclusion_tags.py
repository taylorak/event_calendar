from django import template
from events.models import event,announcement
from django.utils.timezone import utc

register = template.Library()

@register.inclusion_tag('calendars/calendar.html')
def calendar_html(year,month):
    import calendar
    import datetime

    date = datetime.date.today()
    year,month = int(year),int(month)
    calendar.setfirstweekday(6)
    chosen_month = calendar.monthcalendar(year, month)
#    weeks = [[day or '' for day in week] for week in chosen_month]

    weeks = [[]]
    i = 0

    for week in chosen_month:
        for day in week:
            events = announcements = current = False
            if day:
#                check = datetime.date(year,month,day)
#                events = event.objects.filter(start_date==check)
                events = event.objects.filter(start_date__year=year, start_date__month=month, start_date__day=day)
                announcements = announcement.objects.filter(expire_date__gt=datetime.date(year,month,day))
                if year == date.year and month == date.month and day == date.day:
                    current = True
            weeks[i].append((day,events,announcements,current))
        weeks.append([])
        i += 1


    next_month = month+1
    next_year = year
    if next_month == 13: 
        next_month = 1
        next_year = year+1

    prev_month = month-1
    prev_year = year
    if prev_month == 0:
        prev_month = 12
        prev_year = year-1

    return {      
            'month_name': calendar.month_name[month],
            'month': month,
            'year': year,
            'weeks': weeks,
            'daynames': calendar.weekheader(1).split(),#calendar.day_abbr,
            'next_month': next_month,
            'next_year': next_year,
            'prev_month': prev_month,
            'prev_year': prev_year,
            }

