############### Task API CRUD ##############

API ROUTES

1. GET user/api/list_task   [For fetching all the task]
    params: No params
    return JSON response

2. PUT user/api/task/{id}   [For updating a specific task by id and some post paramters]
    params: {id} = id of task
    body:   {"task_name":"","task_description:"","status":"","due_date"}
    return JSON response

3. POST user/api/task       [For creating a task by some post paramters]
    params: No params
    body:   {"task_name":"","task_description:"","status":"","due_date"}
    return JSON response

4. DELETE user/api/delete/{id}   [For deleting a task by specific id]
    params: {id}
    body: no body
    return JSON response

5. GET user/api/get_task/{id}    [For get a specific task by task id]
    params: {id}
    body: no body
    return JSON response

####### How to Setup #########

1. Go to main directory
2. RUN python3 -m venv env
3. RUN source env/bin/activate  [for windows(./env/Scripts/activate.bat),for linux('./env/bin/activate)]
4. RUN pip install -r requirements.txt
5. RUN python manage.py runserver


