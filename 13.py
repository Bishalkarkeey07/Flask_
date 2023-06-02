#  create a flask app, that can support COMMON GET and POST requests, inheriting from RESOURCE class of library itself. Make three classes for (/ or /home), /tasks & /blog inherits from base class that handles the COMMON task. 
# Also:
# 	- make sure while POST, check the credential (do not do much, simply provide harcoded value from request and match this). Properly throw error.
# 	- single class to be used for / or /home
# 	- make list of classes like in factory methods and add resource dynamically



from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BaseResource(Resource):
    def get(self):
        return {"message": "GET request"}

    def post(self):
         
        # credentials = request.json.get('credentials')
        #print(credentials)
        # return{123:request.json }
        email = request.json['email']

        password = request.json['password']

        if email == 'bishal@gmail.com' and password == '1234567':
            return {'message': 'POST request handled by base class'}
        else:
            return {'error': 'Invalid credentials'}, 401


class HomeResource(BaseResource):
    pass

class TasksResource(BaseResource):
    pass

class BlogResource(BaseResource):
    pass

resources = [
    (['/','/home'], 'HomeResource'),
    (['/tasks'], 'TasksResource'),
    (['/blog'], 'BlogResource')
]

#dynamically Handled
for routes, resource_name in resources:
    resource_class = type(resource_name, (BaseResource,), {})
    # for route in routes:
    api.add_resource(resource_class,*routes)  
# Spread operator in Python

if __name__ == '__main__':
    app.run(debug=True)
