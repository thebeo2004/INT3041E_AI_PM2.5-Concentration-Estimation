jupyter nbconvert --to notebook --execute ./PyCaret_baseline.ipynb --output ./Ouput_PyCaret_baseline.ipynb 
screen -r pycaret_class

jupyter nbconvert --to notebook --execute ./model/Tuning/tuning_RF.ipynb --output ./model/Tuning/RF_output.ipynb


jupyter nbconvert --to notebook --execute ./model/pycaret/notebook/PyCaret_cut.ipynb --output ./model/pycaret/notebook/Ouput_PyCaret_cut.ipynb
screen -r oridinal

screen -r model
jupyter nbconvert --to notebook --execute ./model/pycaret/ordinal/Model.ipynb --output ./model/pycaret/ordinal/Output_Model.ipynb
jupyter nbconvert --to notebook --execute ./model/pycaret/ordinal/Model.ipynb --output Output_Model.ipynb


screen -r rf