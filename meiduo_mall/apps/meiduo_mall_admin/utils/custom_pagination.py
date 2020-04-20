from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = 5
    max_page_size = 10
    page_size_query_param = 'pagesize'

    def get_paginated_response(self, data):
        # return Response([
        #     ('counts', self.page.paginator.count),
        #     ('next', self.get_next_link()),
        #     ('previous', self.get_previous_link()),
        #     ('results', data)
        # ])
        return Response({
            'counts': self.page.paginator.count,  # 总数量
            'lists': data,  # 序列化返回的数据列表
            'page': self.page.number,  # 当前页码
            'pagesize': self.page_size,  # 页面容量
            'pages': self.page.paginator.num_pages  # 总页数

        })