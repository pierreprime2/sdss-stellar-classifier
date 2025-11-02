run-ui:
	python app.py

predict:
	python predict.py $(ARGS)

freeze:
	pip freeze > requirements.txt

notebook:
	jupyter notebook