The project is a system for a clinic containing several doctors, where the system consists of two types of users (admin, patient) and each of them has its own pages, where when the patient logs in, the appointment booking page is entered, and if the appointment that the patient booked is not available A message will be given to him that the appointment you are requesting is booked. Please choose another appointment. Through the patient, you can also enter the list of doctors and their specialties. If you click on the doctor’s name, you will be transferred to the appointment booking page.
When logging in by the admin, the patient’s pages are entered, but there is a difference that in the list of doctors, if you click on the name of the doctor, you will be redirected to the reservations for this doctor, and in addition to that, the admin can add a new doctor and view the list of reservations
perfect  .

## Installation

if you have anaconda open vs in it if not you have to creat virtualenv -> virtualenv project_name , and activation the virtualenv -> project_name\Scripts\activate
download Django -> pip install django
cd project_name
makemigrations-> python manage.py makemigrations
add to data base -> python manage.py migrate
create superuser ->manage.py createsuperuser 
open local server -> python manage.py runserver
http://127.0.0.1:8000/
http://127.0.0.1:8000/admin -> for superuser 




