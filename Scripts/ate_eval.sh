export CUDA_VISIBLE_DEVICES="3"

python run_model.py -mode eval -model_checkpoint ./models/ate/googlemt5-base-ate_check \
-experiment_name ate_check -task ate -output_path ./Output \
-id_te_data_path ./dataset/indo/hoasa_hotel/ate/test.csv \