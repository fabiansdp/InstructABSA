export CUDA_VISIBLE_DEVICES="3"

python run_model.py -mode train -model_checkpoint google/mt5-base \
-experiment_name ate_check -task ate -output_dir ./models \
-inst_type 1 \
-learning_rate 1e-4 \
-save_strategy epoch \
-id_tr_data_path ./dataset/indo/hoasa_hotel/ate/train.csv \
-id_val_data_path ./dataset/indo/hoasa_hotel/ate/dev.csv \
-per_device_train_batch_size 16 -per_device_eval_batch_size 16 -num_train_epochs 4