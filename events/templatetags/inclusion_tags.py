from django import template

register = template.Library()

@register.inclusion_tag('calendars/calendar.html')
def calendar_html():
    import calendar
    import datetime
    
    date = datetime.date.today()
    month = calendar.monthcalendar(date.year, date.month)
    weeks = [[day or '' for day in week] for week in month]
    
    
    return {      
        'month': calendar.month_name[date.month],
        'year': date.year,
        'weeks': weeks,
        'daynames': calendar.day_abbr,
    }
    