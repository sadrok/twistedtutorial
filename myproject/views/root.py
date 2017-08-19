from pyramid.view import view_config, notfound_view_config, view_defaults
import math
import uuid

@notfound_view_config(renderer='myproject:templates/404.jinja2')
def not_found(request):
    return {'error': "OH NOES! COULDN'T FIND IT 😭"}


@view_defaults(renderer='myproject:templates/mytemplate.jinja2')
class HomeView():

    def __init__(self, request):
        self.request = request

    @view_config(route_name='home')
    @view_config(route_name='home-with-words')
    @view_config(route_name='home-with-digits')
    @view_config(route_name='home-with-uuid', permission='view_uuid')
    def index(self):
        counter = self.request.session.get('counter', 0) + 1
        self.request.session['counter'] = counter
        return {'project': 'myproject',
                'routename': self.request.matched_route.name,
                'matchdict': self.request.matchdict,
                'math': math,
                'uuid': uuid.uuid4(),
                'counter': counter}

