from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'p'
    #默认情况下，每一页显示的条数为2
    page_size = 5

    page_size_query_param = 's'
    #制定前端分页最大显示数量
    max_page_size = 50

