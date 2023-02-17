import cx_Oracle
from fastapi import FastAPI
from dotenv import load_dotenv
import os



load_dotenv()
# DB VAR
ENV_VAR_HOST = os.getenv('HOST')
ENV_VAR_PORT = os.getenv('PORT')
ENV_VAR_SERVICE_NAME = os.getenv('SERVICE_NAME')
ENV_VAR_ORACLE_CLIENT_PATH = os.getenv('ORACLE_CLIENT_PATH')
ENV_VAR_DB_USER = os.getenv('DB_USER')
ENV_VAR_DB_PASSWORD = os.getenv('DB_PASSWORD')

# API CREDENTIALS
user = os.getenv('API_USER')
passw = os.getenv('API_PASSWORD')
ENV_VAR_API_VER_FOLDER = os.getenv('API_VER_FOLDER')
# ==========================================================

# ORACLE CLIENT - LOCAL PATH==========================================
cx_Oracle.init_oracle_client(lib_dir=ENV_VAR_ORACLE_CLIENT_PATH)
# ====================================================================

app = FastAPI(title='centynel',
            description='Web Service MUI',
            version='ALPHA',
            contact={
                "acces_token": "CCT CPU Department",
                "email": "cct-cpu@cct-pa.com"
                })


# ORACLE CONNECTION======================================================================
dsn_tns = cx_Oracle.makedsn(ENV_VAR_HOST,ENV_VAR_PORT,service_name=ENV_VAR_SERVICE_NAME) 
con = cx_Oracle.connect(user=ENV_VAR_DB_USER, password=ENV_VAR_DB_PASSWORD, dsn=dsn_tns) 
cursor = con.cursor()
# ======================================================================================== 


# print("Database version:", con.version)
@app.get('/')
async def index():

    return {"message": "COLON CONTAINER TERMINAL WEB SERVICES"}


# CONTAINER HOLD PROCEDURE
@app.get(ENV_VAR_API_VER_FOLDER+"/employees_query/{EMPLOYEE_ID}")
async def employees_query(EMPLOYEE_ID):
    
    # query = "select employee_id,first_name,last_name,div_dept,dept_sec,position from empmst where employee_id = :var01" 
    

    ref_cursor = cursor.execute("select employee_id,first_name,last_name,div_dept,dept_sec,position from empmst where employee_id = :var01",var01=EMPLOYEE_ID)
    for row in ref_cursor:
            return {"EMPLOYEE_ID": row[0],
                    "FIRST_NAME": row[1],
                    "LAST_NAME": row[2],
                    "DIV_DEPT": row[3],
                    "DEPT_SEC": row[4],
                    "POSITION": row[5]}