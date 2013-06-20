from django import template
from itertools import groupby
from events.models import event

register = template.Library()

@register.inclusion_tag('calendars/calendar.html')
def calendar_html(year,month):
    import calendar
    year,month = int(year),int(month)
    chosen_month = calendar.monthcalendar(year, month)
    weeks = [[day or '' for day in week] for week in chosen_month]
    
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
        'daynames': calendar.day_abbr,
        'next_month': next_month,
        'next_year': next_year,
        'prev_month': prev_month,
        'prev_year': prev_year,
    }
    