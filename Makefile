constancia.pdf: base/constancia-examen.pdf generar.py datos.py
	python3 generar.py

base/constancia-examen.pdf:
	cd base; \
	wget https://www.dc.uba.ar/wp-content/uploads/2018/11/constancia-examen.pdf

# en caso de que se modifique el template con xournalpp y se guarde comprimido:
extract: template.xopp
	mv template.xopp template.xopp.gz
	gunzip template.xopp.gz
