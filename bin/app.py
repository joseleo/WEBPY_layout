import web

# web.config.debug = False

urls = (
    '/hello', 'Index'
)

app = web.application(urls, globals())
# app = web.application(urls, locals())
# store = web.session.DiskStore('sessions')
# session = web.session.Session(app, store, initializer={'count': 0})

render = web.template.render('templates/', base="layout")


class Index(object):
    def GET(self):
        # greeting = "webpy"
        return render.hello_form_laid_out()

    def POST(self):
        form = web.input(name="Nadie", greet="Hola")
        greeting = "%s %s" % (form.greet, form.name)
        return render.index_laid_out(greeting=greeting)


# class count:
#    def GET(self):
#        session.count += 1
#        return str(session.count)


# class reset:
#     def GET(self):
#         session.kill()
#        return ""

if __name__ == "__main__":
    app.run()
