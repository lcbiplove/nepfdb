from rest_framework.pagination import PageNumberPagination


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 75
    page_size_query_param = 'size'


class MediumResultsSetPagination(PageNumberPagination):
    page_size = 40
    page_size_query_param = 'size'


class SmallResultsSetPagination(PageNumberPagination):
    page_size = 20
    page_size_query_param = 'size'
