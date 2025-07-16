from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination


class WatchListPagination(PageNumberPagination):
    #setting page size for seleted views
    page_size = 3
    
    # old query url - "http://127.0.0.1:8000/watch/list2/?page=2",
    #custom name of query param from default 'page' to any-- like below 'p'
    # page_query_param = 'p' # "http://127.0.0.1:8000/watch/list2/?p=2", <- new query modified url

    #custom page number count
    page_size_query_param = 'size'

    max_page_size = 10

    last_page_strings = 'end' # default - last , can be customized to any by this

class WatchListLOPagination(LimitOffsetPagination):
    default_limit = 5
    max_limit = 10

    limit_query_param = 'limit'
    offset_query_param = 'start'

class WatchListCursor(CursorPagination):
    page_size = 5
    ordering = 'created'