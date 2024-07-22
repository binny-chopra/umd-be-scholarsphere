from constants import app_constants
from utility.common import common
from flask import make_response


class sponsors_model:
    def __init__(self):
        common.conn_setup(self)

    def sponsors_list_model(self):
        self.cursor.execute(f"SELECT * FROM {app_constants.REGISTERED_SPONSORS_TABLE}")
        result = self.cursor.fetchall()

        if len(result) > 0:
            payload = []
            for row in result:
                student = {
                    "scholarshipId": row["scholarshipId"],
                    "scholarshipName": row["scholarshipName"],
                    "totalAmount": row["totalAmount"],
                    "awardedAmount": row["awardedAmount"],
                    "renewable": row["renewable"],
                    "timeline": row["timeline"],
                    "criteria": {
                        "level": row["level"],
                        "major": row["major"],
                        "needOrMerit": row["needOrMerit"],
                        "state": row["state"],
                        "county": row["county"],
                        "gpa": row["gpa"],
                    },
                }
                payload.append(student)

            response = make_response({"payload": payload}, 200)
            response.headers["Access-Control-Allow-Origin"] = "*"
            return response
        else:
            return make_response({"message": app_constants.NO_DATA_FOUND}, 204)

    def new_sponsor_model(self, data):
        try:
            scholarshipId = data.get("scholarshipId", "")
            scholarshipName = data.get("scholarshipName", "")
            totalAmount = data.get("totalAmount", 0)
            awardedAmount = data.get("awardedAmount", 0)
            renewable = data.get("renewable", "")
            timeline = data.get("timeline", "")
            
            criteria = data.get("criteria", {})
            level = ','.join(criteria.get("level", []))
            major = ','.join(criteria.get("major", []))
            gpa = float(criteria.get("gpa", 0))
            needOrMerit = criteria.get("needOrMerit", "")
            state = criteria.get("state", "")
            county = ','.join(criteria.get("county", []))
            
            query = f"""
                INSERT INTO {app_constants.REGISTERED_SPONSORS_TABLE} (
                    {app_constants.SCHOLARSHIP_ID}, 
                    {app_constants.SCHOLARSHIP_NAME}, 
                    {app_constants.TOTAL_AMT}, 
                    {app_constants.AWARDED_AMT}, 
                    {app_constants.RENEWABLE}, 
                    {app_constants.TIMELINE}, 
                    {app_constants.LEVEL}, 
                    {app_constants.MAJOR}, 
                    {app_constants.NEED_OR_MERIT}, 
                    {app_constants.STATE}, 
                    {app_constants.COUNTY}, 
                    {app_constants.GPA}
                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (
                scholarshipId,
                scholarshipName,
                totalAmount,
                awardedAmount,
                renewable,
                timeline,
                level,
                major,
                needOrMerit,
                state,
                county,
                gpa,
            )
            self.cursor.execute(query, values)
            return make_response(
                {
                    "message": f"{app_constants.NEW_SPONSOR_ADDED} {data['scholarshipId']}"
                },
                201,
            )
        except Exception as e:
            print(f"Error adding new sponsor: {e}")
            return make_response(
                {"message": f"{app_constants.NO_NEW_SPONSOR_ADDED, e}"}, 500
            )