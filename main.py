from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


# Base class 
class BaseResource(Resource):
    def get(self):
        return {'message': 'GET request handled by base class'}

    def post(self):
        try:
            credentials = request.json.get('credentials')
            email = credentials.get('email')
            password = credentials.get('password')

            if email == 'bishal@gmail.com' and password == '1234567':
                return {'message': 'POST request handled by base class'}
            else:
                return {'error': 'Invalid credentials'}, 401
        except:
            return {'error': 'Enter valid email and password'}

class HomeResource(BaseResource):
    pass

class TasksResource(BaseResource):
    __name__ = 'TasksResource'  # Set the __name__ attribute

# Class for handling `/blog` route
class BlogResource(BaseResource):
    __name__ = 'BlogResource'  # Set the __name__ attribute
    def get(self, report_type=None):
        if report_type is None:
            return {'message': 'GET request handled by BlogResource'}
        elif report_type == 'abc':
            return self.abc()
        elif report_type == 'def':
            return self.def_()
        else:
            return {'error': 'Invalid report type'}, 404

    def abc(self):
        return {'message': 'Handle by abc'}

    def def_(self):
        return {'message': 'Handle by def'}

    def default(self):
        return {'message': 'default message'}


# Add resources dynamically
resources = {
    # '/': HomeResource(),
    # '/Home/': HomeResource(),
    '/tasks/': TasksResource(),
    '/blog/<string:report_type>': BlogResource(),
}

# Dynamically add resources
for route, resource_cls in resources.items():
    api.add_resource(resource_cls, route)

if __name__ == '__main__':
    app.run(port=5004, debug=True)


    
