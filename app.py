from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class BaseResource(Resource):
    def __init__(self):
        self.methods = {}

    def get(self, report_type=None):
            if report_type in self.methods:
                if report_type != 'default':
                    return self.methods[report_type]()
                else:
                    return self.default()
            else:
                return {'massage': 'GET method call'}, 400

    def post(self, report_type=None):
        email = request.json['email']
        password = request.json['password']

        if email == 'bishal@gmail.com' and password == '1234567':
            return self.get(report_type)
        else:
            return {'error': 'Invalid credentials'}, 401

    def default(self):
        return {'message': 'default() called'}


class HomeResource(BaseResource):
    pass

class TasksResource(BaseResource):
    pass

class BlogResource(BaseResource):
    def __init__(self):
        super().__init__()
        self.methods = {
            'abc': self.abc,
            'xyz': self.xyz,
            'default': self.default
        }

    def abc(self):
        return {'message': 'abc() blog called'}

    def xyz(self):
        return {'message': 'xyz() blog called'}

    def default(self):
        return {'message': 'default() blog called'}

resources = [
    (['/', '/home'], HomeResource),
    (['/tasks'], TasksResource),
    (['/blog', '/blog/', '/blog/<string:report_type>'], BlogResource)
]

# Dynamically handle resources
for routes, resource_class in resources:
    api.add_resource(resource_class, *routes)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5004, debug=True)
