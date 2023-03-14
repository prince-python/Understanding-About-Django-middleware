def simple_middleware(get_response):
    print('simple middleware is running')
    def middleware(request):
        print('some code before actual view')
        response = get_response(request)
        print('some code after actual view')
        return response
    return middleware