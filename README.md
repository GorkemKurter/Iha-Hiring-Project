# Iha-Hiring-Project

#Clone or download the repository.
#Open the main folder with VS Code 
#Change the direction iha_kiralama_projesi(open the vs code terminal and use following command:cd iha_kiralama_projesi)
#Then type the following command on the same terminal:docker-compose up

#For the first time tpye following commands on the terminal:
docker-compose exec web python manage.py migrate auth
docker-compose exec web python manage.py migrate

#Open any browser and type the following URL:http://localhost:8000/
#You can connect the webapp anytime with docker desktop app now.

Requirements for project:
DOCKER Desktop app
IDE for Django such as Pycharm,VS Code...
