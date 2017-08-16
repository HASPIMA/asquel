INSTALLDIR = /usr/share/asquelito

install :
	sudo mkdir ${INSTALLDIR}
	sudo cp asquel.py ${INSTALLDIR}/asquel.py
	sudo cp icono.png ${INSTALLDIR}/icono.png
	sudo cp run.sh ${INSTALLDIR}/run.sh
	sudo mkdir ${INSTALLDIR}/xolo
	cd xolo
	sudo cp xolo/__init__.py ${INSTALLDIR}/xolo/__init__.py
	cp xo.desktop ~

remove :
	sudo rm -r ${INSTALLDIR}
	rm ~/xo.desktop

