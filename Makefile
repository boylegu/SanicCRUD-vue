# author: baoer.gu
# makefile of sanic_crud_vue __2017-06-13 in Shanghai HongKou District

proj_server := "app.py"
proj_path := $(shell pwd)

install:
		pip install  -r requirements.txt

clean:
		find . -name \*.pyc -delete

dev:
		cd $(proj_path)/sanic_crudvue && \
		python $(proj_server)

test:
		cd $(proj_path)/sanic_crudvue && \
		py.test -q ../tests/test-view.py
