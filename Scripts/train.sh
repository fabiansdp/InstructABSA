LANGUAGE="$1"
DATASET_TYPE="$2"
TASK="$3"
GPU="$4"
SEED="$5"

export CUDA_VISIBLE_DEVICES="$GPU"

python run_model.py -mode train -model_checkpoint google/mt5-base \
-experiment_name "${DATASET_TYPE}-${TASK}" -task "$TASK" -output_dir ./models \
-inst_type 1 \
-learning_rate 1e-4 \
-save_strategy epoch \
-id_tr_data_path "./Dataset/${DATASET_TYPE}/${TASK}/train.csv" \
-id_val_data_path "./Dataset/${DATASET_TYPE}/${TASK}/dev.csv" \
-seed "$SEED" \
-per_device_train_batch_size 16 -per_device_eval_batch_size 16 -num_train_epochs 4