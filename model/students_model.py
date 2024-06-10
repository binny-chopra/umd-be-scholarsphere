from constants import app_constants
from utility.common import common
from flask import make_response


class students_model:
    def __init__(self):
        common.conn_setup(self)
        # try:
        #     self.conn = mysql.connector.connect(
        #         host=app_constants.DB_HOST,
        #         user=app_constants.DB_USER,
        #         password=app_constants.DB_PASSWORD,
        #         database=app_constants.DB_NAME,
        #     )
        #     self.conn.autocommit = True
        #     self.cursor = self.conn.cursor(dictionary=True)
        #     print(app_constants.CONN_SUCCESSFUL)
        # except:
        #     print(app_constants.CONN_FAILED)

    def registered_students_list_model(self):
        self.cursor.execute(f"SELECT * FROM {app_constants.REGISTERED_STUDENT_TABLE}")
        result = self.cursor.fetchall()
        if len(result) > 0:
            response = make_response({"payload": result}, 200)
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            return make_response({"message": f"{app_constants.NO_DATA_FOUND}"}, 204)

    def new_student_model(self, data):
        try:
            self.cursor.execute(
                f"INSERT INTO {app_constants.REGISTERED_STUDENT_TABLE}({app_constants.STUDENT_ID}, {app_constants.STUDENT_NAME}, {app_constants.STUDENT_MAJOR}, {app_constants.GRAD_DATE}, {app_constants.STUDENT_EMAIL}, {app_constants.MAJORITY_CLASSES}, {app_constants.STATE}, {app_constants.COUNTY}, {app_constants.GPA}) VALUES ('{data['studentId']}', '{data['studentName']}', '{data['studentMajor']}', '{data['gradDate']}', '{data['studentEmail']}', '{data['majorityClasses']}', '{data['state']}', '{data['county']}', '{data['gpa']}')"
            )
            return make_response(
                {"message": f"{app_constants.NEW_STUDENT_ADDED} {data['studentId']}"},
                201,
            )
        except:
            return make_response({"message": f"{app_constants.NO_NEW_STUDENT_ADDED}"})

    def student_update_model(self, data):
        self.cursor.execute(
            f"UPDATE {app_constants.REGISTERED_STUDENT_TABLE} SET studentName='{data['studentName']}', studentMajor='{data['studentMajor']}', gradDate='{data['gradDate']}', studentEmail='{data['studentEmail']}', majorityClasses='{data['majorityClasses']}', state='{data['state']}', county='{data['county']}', gpa='{data['gpa']}' WHERE studentId={data['studentId']}"
        )
        if self.cursor.rowcount > 0:
            return make_response(
                {
                    "message": f"{app_constants.UPDATED_STUDENT_RECORD} {data['studentId']}"
                },
                201,
            )
        else:
            return make_response({"message": f"{app_constants.NOTHING_TO_UPDATE}"}, 202)

    def student_delete_model(self, studentId):
        self.cursor.execute(
            f"DELETE FROM {app_constants.REGISTERED_STUDENT_TABLE} WHERE {app_constants.STUDENT_ID}={studentId}"
        )
        if self.cursor.rowcount > 0:
            return make_response(
                {"message": f"{app_constants.DELETED_STUDENT_RECORD} {studentId}"}, 200
            )
        else:
            return make_response({"message": f"{app_constants.NOTHING_TO_DELETE}"}, 202)

    def student_patch_model(self, data, studentId):
        patch_query = f"UPDATE {app_constants.REGISTERED_STUDENT_TABLE} SET "
        for key in data:
            patch_query += f"{key}='{data[key]}',"
            patch_query = patch_query[:-1] + f" WHERE studentId={studentId}"
            self.cursor.execute(patch_query)
            if self.cursor.rowcount > 0:
                return make_response(
                    {"message": f"{app_constants.UPDATED_STUDENT_RECORD} {studentId}"},
                    201,
                )
            else:
                return make_response(
                    {"message": f"{app_constants.NOTHING_TO_UPDATE}"}, 202
                )
