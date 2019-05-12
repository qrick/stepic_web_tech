def wsgi_application(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type','text/plain')]
    params = environ['QUERY_STRING'].split('&')    
    body = "\n".join(params)
    body += "\n"    
    start_response(status, headers)
    return [ str.encode(body) ]
