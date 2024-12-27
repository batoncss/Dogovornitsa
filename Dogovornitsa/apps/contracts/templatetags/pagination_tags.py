from django import template
from django.http import QueryDict

register = template.Library()


# todo: use constants
ORDER_BY = "order_by"


@register.simple_tag
def sorting_by_query_params(current_params, column_name):
    res = QueryDict(current_params, mutable=True)
    res["order_by"] = column_name
    res["order_direction"] = "desc" if res.get("order_direction") == "asc" else "asc"
    return "?" + res.urlencode()

@register.simple_tag
def changing_number_elements_on_page(current_params, elements_per_page):
    res = QueryDict(current_params, mutable=True)
    res["per_page"] = elements_per_page
    return "?" + res.urlencode()

@register.simple_tag
def switching_page(current_params, page_number):
    res = QueryDict(current_params, mutable=True)
    print(res)
    res["page"] = page_number
    return "?" + res.urlencode()