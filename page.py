import os
 
import jinja2
import webapp2

from rot13 import rot13


template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape = True)


class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)


class MainPage(Handler):
    def get(self):
        self.render('rot13.html')

    def post(self):
        text = self.request.get('text')
        text_rot13 = ''
        if text:
            text_rot13 = rot13(text)

        self.render('rot13.html', text = text_rot13)