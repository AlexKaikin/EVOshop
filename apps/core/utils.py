from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

from apps.core.services.filter_service import get_filter_category_list, get_filter_tag_list


class Filter:
    """ Список фильтров к товарам """
    def get_category(self):
        return get_filter_category_list()

    def get_tag(self):
        return get_filter_tag_list()


def ajax_paginator(self, context):
    paginator = Paginator(context['object_list'], 9)
    page = self.request.GET.get('page')
    try:
        context['object_list'] = paginator.page(page)
    except PageNotAnInteger:
        context['object_list'] = paginator.page(1)
    except EmptyPage:
        context['object_list'] = paginator.page(paginator.num_pages)
