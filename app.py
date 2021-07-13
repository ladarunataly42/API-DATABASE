import os
from flask import Flask, request
from flask_restful import Resource, Api

from Actions import Actions

app = Flask(__name__)
api = Api(app)


class Upload(Resource):
    def post(self):
        file = request.files['file']
        filename = file.filename
        file.save("UPLOAD_FOLDER" + "/" + filename)
        my_file = open(filename, "r")
        text = my_file.read()
        session = Actions()
        if session.upload_database(filename, text):
            return "Uploaded on Database", 200
        else:
            return "Problem on upload - DB", 404


class Delete(Resource):
    def delete(self):
        session = Actions()
        id = request.form.get('id')
        if session.delete_by_id(id):
            return "Deleted", 200
        else:
            return f"Problem on delete the id: {id}", 404


class Update(Resource):
    def patch(self):
        session = Actions()
        id = request.form.get('id')
        text = request.form.get('text')
        if session.update_from_id(id, text):
            return "Updated", 200
        else:
            return "Problem on update", 404


api.add_resource(Upload, '/upload-file')
api.add_resource(Delete, '/delete')
api.add_resource(Update, '/update-file-text')

if __name__ == '__main__':
    app.run()
