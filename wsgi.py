from src.webapp.app import app

# def application(env, start_response):
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     return ["Hello!"]

if __name__ == "__main__":
    print("in wsgi main")
    app.run()