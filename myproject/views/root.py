from pyramid.view import view_config


@view_config(route_name='home', renderer='myproject:templates/mytemplate.jinja2')
@view_config(route_name='home-with-words', renderer='myproject:templates/mytemplate.jinja2')
@view_config(route_name='home-with-digits', renderer='myproject:templates/mytemplate.jinja2')
@view_config(route_name='home-with-uuid', renderer='myproject:templates/mytemplate.jinja2')
def index(request):
    return {'project': 'myproject'}

