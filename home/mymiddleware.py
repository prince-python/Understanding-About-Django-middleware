class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        print('classbased middleware called')
    def __call__(self, request):
        name=request.POST['name']
        print('class based before code',name)
        response = self.get_response(request)
        print('classbased after code')
        return response