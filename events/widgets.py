'''
Created on Jun 17, 2013

@author: taylorak
'''

"""
Extra HTML Widget classes
"""

import time
import datetime

from event_calendar import settings
from django.forms.widgets import MultiWidget,DateInput,TimeInput
from django.forms.extras.widgets import *
from django.forms.widgets import HiddenInput
from django.utils.dates import MONTHS
from django.utils.safestring import mark_safe
from django.utils.formats import get_format


class SelectYrMon(SelectDateWidget):
    def __init__(self, attrs=None, years=None, required=True):
        super(SelectYrMon, self).__init__(attrs, years, required)


    def render(self, name, value, attrs=None):
        try:
            year_val, month_val, day_val = value.year, value.month, value.day
        except AttributeError:
            year_val = month_val = day_val = None
            if isinstance(value, basestring):
                if settings.USE_L10N:
                    try:
                        input_format = get_format('DATE_INPUT_FORMATS')[0]
                        # Python 2.4 compatibility:
                        #     v = datetime.datetime.strptime(value, input_format)
                        # would be clearer, but datetime.strptime was added in 
                        # Python 2.5
                        v = datetime.datetime(*(time.strptime(value, input_format)[0:6]))
                        year_val, month_val, day_val = v.year, v.month, v.day
                    except ValueError:
                        pass
                else:
                    match = RE_DATE.match(value)
                    if match:
                        year_val, month_val, day_val = [int(v) for v in match.groups()]
        choices = [(i, i) for i in self.years]
        year_html = self.create_select(name, self.year_field, value, year_val, choices)
        choices = MONTHS.items()
        month_html = self.create_select(name, self.month_field, value, month_val, choices)
        #choices = [(i, i) for i in range(1, 32)]
        day_html = self.create_hidden(name, self.day_field, value, day_val)

        date_format = get_format('DATE_FORMAT')
        escaped = False
        output = []
        for char in date_format:
            if escaped:
                escaped = False
            elif char == '\\':
                escaped = True
            elif char in 'Yy':
                output.append(year_html)
            elif char in 'bFMmNn':
                output.append(month_html)
            elif char in 'dj':
                output.append(day_html)
        return mark_safe(u'\n'.join(output))
        

    def create_hidden(self, name, field, value, val):
        if 'id' in self.attrs:
            id_ = self.attrs['id']
        else:
            id_ = 'id_%s' % name
        local_attrs = self.build_attrs(id=field % id_)
        h = HiddenInput()
        hidden_html = h.render(field % name, 1, local_attrs)
        return hidden_html


class SplitSelDateTimeWidget(MultiWidget):
    """
    A Widget that splits datetime input into two <input type="text"> boxes.
    """
#  date_format = DateInput.format
#  time_format = TimeInput.format

    def __init__(self, attrs=None, date_format=None, time_format=None):
        widgets = (SelectDateWidget(attrs=attrs), TimeInput(attrs=attrs, format=time_format))
        super(SplitSelDateTimeWidget, self).__init__(widgets, attrs)

    def decompress(self, value):
        if value:
            return [value.date(), value.time().replace(microsecond=0)]
        return [None, None]

