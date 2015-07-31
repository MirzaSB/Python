import web

urls = (
  '/hello', 'Index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class Index(object):
    def GET(self):
    	return render.hello_form()

    def POST(self):
        form = web.input(name="Nobody", greet="Hello", location="Path", image={})
        greeting = "%s, %s" % (form.greet, form.name)
        filedir = form.location + '/'
        fout = open(filedir +'/'+ form['image'].name + '_from_ex51.jpg', 'w') 
        fout.write(form['image'].file.read())
        fout.close()
        return render.index(greeting = greeting)

if __name__ == "__main__":
    app.run()