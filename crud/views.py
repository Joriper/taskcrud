from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.db import connection
from django.shortcuts import render

class UpdateandCreate(APIView):

    def put(self,request,_id):
        task_name = request.data.get("task_name")
        task_description = request.data.get("task_description")
        due_date = request.data.get("due_date")
        status = request.data.get("status")
        print(task_name,task_description,_id)
        with connection.cursor() as cursor:
            cursor.execute(f"UPDATE task set task_name='{task_name}',task_description='{task_description}',status='{status}',due_date='{due_date}' where id='{_id}'")
        return Response({"status":"OK","message":"Successfully Updated the task","id":_id})

    def post(self,request):
        
        task_name = request.data.get("task_name")
        task_description = request.data.get("task_description")
        due_date = request.data.get("due_date")
        status = request.data.get("status")

        print(task_name,task_description)

        with connection.cursor() as cursor:
            cursor.execute(f"INSERT INTO task(task_name,task_description,status,due_date) VALUES('{task_name}','{task_description}','{status}','{due_date}')")
        return Response({"status":"OK","message":"Task Created Successfully"})

@api_view(['GET'])
def list_task(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * from task;")
        raw = cursor.fetchall()
        columns = [col[0] for col in cursor.description]
        data = [dict(zip(columns, row)) for row in raw]

    return Response({"status":"OK","message":"Fetched Successfully","data":data})


@api_view(['DELETE'])
def delete_task(request,_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"DELETE FROM task where id=%s",[_id])
        return Response({"status":"OK","message":"Task Deleted Successfully"})
    except Exception as error:
        print(error)
        return Response({"status":"Failed","message":"Something is wrong with our server"})


@api_view(['GET'])
def get_task(request,_id):
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * from task where id='{_id}';")
            raw = cursor.fetchall()
            columns = [col[0] for col in cursor.description]
            data = [dict(zip(columns, row)) for row in raw] 
        return Response({"status":"OK","message":"Success","data":data})

    except Exception as error:
        return Response({"status":"Failed","message":"Something is wrong with our server"})
        



def index(request):
    result = list_task(request)
    if result.data.get("data"):
        task_list = result.data['data']
    else:
        task_list = []
    return render(request,'index.html',{"data":task_list})
