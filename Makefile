constancia.pdf: base/constancia-examen.pdf generar.py datos.py
	python3 generar.py

base/constancia-examen.pdf:
	cd base; wget https://www.dc.uba.ar/wp-content/uploads/2018/11/constancia-examen.pdf
