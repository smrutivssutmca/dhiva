from datetime import datetime, timedelta
from django import template
from django.utils import timezone
from django.utils.timesince import timesince

register = template.Library()

@register.filter
def humanize_timedelta(value):
    now = timezone.now()
    if not isinstance(value, datetime):
        return value

    if value > now:
        return "just now"

    delta = now - value

    if delta < timedelta(minutes=1):
        return "just now"
    elif delta < timedelta(hours=1):
        return f"{int(delta.total_seconds() // 60)} minutes ago"
    elif delta < timedelta(days=1):
        return f"{int(delta.total_seconds() // 3600)} hours ago"
    else:
        return value.strftime("%d %B %Y")
