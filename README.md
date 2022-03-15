OC - SoftDesk - Bug tracking API
=

<u>Openclassrooms - DA Python - Project 10 :</u><br>

API RESTFul providing a bug tracking system.
<br>
Use of Django Rest Framework + SQLIte database.
## 1. <u>List of endpoints</u> :

1. Sign Up
POST
2. Login
POST
3. Login Refresh
POST
4. Create a project
PUT
5. Update a project
GET
6. Get a specific projet
GET
7. Get list of projects
DEL
8. Delete a project
POST
9. Create a contributor on a project
GET
10. Get all contributors of a project
DEL
11. Delete a contributor of a project
POST
12. Create an issue on a project
PATCH
13. Update issue on project
GET
14. Get issues on project
DEL
15. Delete issue on project
POST
16. Create comment on issue
PATCH
17. Update comment on issue
GET
18. Get comments on an issue
GET
19. Get a specific comment on an issue
DEL
20. Delete comment on issueinscription et connexion au site,

## 2. <u> Documentation</u>

- Initial OC requirements available in the folder [doc](src/doc).
- Full API document available [here](https://documenter.getpostman.com/view/19799080/UVsJxnRD).


## 3. <u> Set Up</u>

```bash
git clone https://github.com/XavierCoulon/OC-P10-SoftDesk.git
cd P10_SoftDesk
python3.9 -m venv .env
source .env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```
API available on http://127.0.0.1:8000/
