from rest_framework.pagination import PageNumberPagination


class PageNumberPaginationManual(PageNumberPagination):
    page_query_param = 'page'
    #默认情况下，每一页显示的条数为2
    page_size = 5

    page_size_query_param = 'size'
    #制定前端分页最大显示数量
    max_page_size = 50

    page_query_description = '第几页'
    page_size_query_description = '每页几条'

    def get_paginated_response(self, data):
        response = super(PageNumberPaginationManual,self).get_paginated_response(data)
        response.data['total_pages'] = self.page.paginator.num_pages
        response.data['current_page_num'] = self.page.number
        return response
