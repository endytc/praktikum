import webapp2

class HelloWebapp2(webapp2.RequestHandler):
    def get(self):
        self.response.write('<b>Hello, webapp2!</b>')

app = webapp2.WSGIApplication([
    ('/', HelloWebapp2),
], debug=True)

def main():
    from paste import httpserver
    httpserver.serve(app, host='127.0.0.1', port='8081')

if __name__ == '__main__':
    main()