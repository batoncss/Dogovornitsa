from django import template
from django.http import QueryDict

register = template.Library()


# todo: use constants
ORDER_BY = "order_by"


@register.simple_tag
def sort_by_query_params(current_params, column_name):
    res = QueryDict(current_params, mutable=True)
    res["order_by"] = column_name
    res["order_direction"] = "desc" if res.get("order_direction") == "asc" else "asc"
    return "?" + res.urlencode()