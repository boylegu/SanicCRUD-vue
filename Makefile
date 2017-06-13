# author: baoer.gu
# makefile of sunflower __2017-06-13 in Shanghai HongKou District

proj_server := "./sanic_crudvue/app.py"

install:
    pip install  -r requirements.txt

clean:
	find . -name \*.pyc -delete

dev:
    python $(proj_server)