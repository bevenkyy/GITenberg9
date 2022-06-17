@ECHO OFF

ECHO. 

echo Upgrading pip command tool...

@ECHO ON

python -m pip install --upgrade pip

@ECHO OFF

ECHO. 

ECHO Start installing Python package...

@ECHO ON

pip3 install numpy-1.17.3+mkl-cp37-cp37m-win_amd64.whl

pip3 install numba-0.46.0-cp37-cp37m-win_amd64.whl

pip3 install numexpr-2.7.0-cp37-cp37m-win_amd64.whl

pip3 install scipy-1.3.1-cp37-cp37m-win_amd64.whl

pip3 install python_dateutil-2.8.0-py2.py3-none-any.whl

pip3 install xlrd-1.2.0-py2.py3-none-any.whl

pip3 install openpyxl-3.0.0-py3-none-any.whl

pip3 install pandas-0.25.2-cp37-cp37m-win_amd64.whl

pip3 install Pillow-6.1.0-cp37-cp37m-win_amd64.whl

pip3 install networkx-2.4-py3-none-any.whl

pip3 install PyWavelets-1.1.1-cp37-cp37m-win_amd64.whl

pip3 install pyparsing-2.4.2-py2.py3-none-any.whl

pip3 install matplotlib-3.1.1-cp37-cp37m-win_amd64.whl

pip3 install scikit_image-0.16.2-cp37-cp37m-win_amd64.whl

pip3 install GDAL-3.0.1-cp37-cp37m-win_amd64.whl

pip3 install rasterio-1.1.0-cp37-cp37m-win_amd64.whl

pip3 install Fiona-1.8.6-cp37-cp37m-win_amd64.whl

pip3 install dbfread-2.0.7-py2.py3-none-any.whl

pip3 install PyMySQL-0.9.3-py2.py3-none-any.whl

pip3 install joblib-0.13.2-py2.py3-none-any.whl

pip3 install psutil-5.6.3-cp37-cp37m-win_amd64.whl

pip3 install scikit_learn-0.21.3-cp37-cp37m-win_amd64.whl

pip3 install PyQt5-5.13.0-5.13.0-cp35.cp36.cp37.cp38-none-win_amd64.whl

pip3 install pyqt5_tools-5.13.0.1.5-cp37-none-win_amd64.whl

pip3 install pylint-2.4.3-py3-none-any.whl

pip3 install ipython-7.8.0-py3-none-any.whl

PAUSE
