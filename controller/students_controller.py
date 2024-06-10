from app import app
from model.students_model import students_model
from flask import request

obj = students_model()


@app.route("/students")
def registered_students_contoller():
    return obj.registered_students_list_model()

@app.route("/students/new", methods=["POST"])
def new_student_contoller():
    return obj.new_student_model(request.form)

@app.route("/students/update", methods=["PUT"])
def new_student_update_contoller():
    return obj.student_update_model(request.form)

@app.route("/students/delete/<studentId>", methods=["DELETE"])
def student_delete_contoller(studentId):
    return obj.student_delete_model(studentId)

@app.route("/students/patch/<studentId>", methods=["PATCH"])
def student_patch_contoller(studentId):
    return obj.student_patch_model(request.form, studentId)
