import binascii
from pyramid.config import Configurator
from pyramid_nacl_session.session import EncryptedCookieSessionFactory


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    config = Configurator(settings=settings)
    config.include('pyramid_jinja2')

    hex_key = settings['myproject.session_secret'].strip()
    secret = binascii.unhexlify(hex_key)
    factory = EncryptedCookieSessionFactory(secret)
    config.set_session_factory(factory)

    config.add_static_view('static', 'static', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('home-with-words', '/{words:[a-zA-Z ]+}')
    config.add_route('home-with-digits', '/{digits:[\d+.,]+}')
    config.add_route('home-with-uuid', '/{uuid:[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}}')
    config.scan('.views')
    return config.make_wsgi_app()
