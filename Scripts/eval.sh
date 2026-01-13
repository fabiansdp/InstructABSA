LANGUAGE="$1"
DATASET_TYPE="$2"
TASK="$3"
GPU="$4"
MODEL_PATH="$5"
SEED="$6"

export CUDA_VISIBLE_DEVICES="$GPU"

python run_model.py -mode eval -model_checkpoint "$MODEL_PATH" \
-task "$TASK" -output_path ./Output \
-id_te_data_path "./dataset/${LANGUAGE}/${DATASET_TYPE}/${TASK}/test.csv" \
-seed "$SEED"