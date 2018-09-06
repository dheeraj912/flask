from common.common import *

class School(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('id', type = int, help = "Please provide a valid ID")
        parser.add_argument('schoolName', type = str,required = True, help = "Plaese provide school name")
        args = parser.parse_args()

        try:
            con =MYSQL.connect()
            APP.logger.info("connection to the database"+" "+APP.config['MYSQL_DATABASE_USER']+" " +"established")
            cur = con.cursor()
            sql = '''INSERT INTO school VALUES (%s,%s)'''
            APP.logger.info("query executed"+" "+sql )
            cur.execute(sql,(args['id'],args['schoolName']))
            con.commit()
            APP.logger.info("connection commited")
            con.close()
            APP.logger.info("connection closed from DB:"+" "+APP.config['MYSQL_DATABASE_USER']+" "+ "Query Executed successfully")
        except KeyError as e:
            APP.logger.error("Missing Parameter:"+" "+str(e))
            return {"errors":"Missing parameter"+ str(e)},400
        except Exception as e:
            APP.logger.error(str(e))
            return {"errors": str(e)},400
        return {'response':'success'},201

    def get(self):
        try:
            con =MYSQL.connect()
            APP.logger.info("connection to the database"+" "+APP.config['MYSQL_DATABASE_USER']+" " +"established")
            cur = con.cursor()
            sql = '''SELECT * from school'''
            cur.execute(sql)
            APP.logger.info("query executed"+" "+sql )
            school_data = cur.fetchall()

            con.close()
            APP.logger.info("connection closed from DB:"+" "+APP.config['MYSQL_DATABASE_USER']+" "+ "Query Executed successfully")
            school = []
            for row in school_data:
                school_dict= {}
                school_dict['id']= row[0]
                school_dict['school'] = row[1]
                school.append(school_dict)
            response = {}
            response['school'] = school
        except Exception as e:
            APP.logger.error(str(e))
            return {"errors": str(e)}

        return jsonify(response)
