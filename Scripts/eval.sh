DATASET_TYPE="$1"
TASK="$2"
GPU="$3"

export CUDA_VISIBLE_DEVICES="$GPU"

MODEL_DIR="models/${TASK}"
MODEL_PATHS="$MODEL_DIR/*"

for MODEL_PATH in $MODEL_PATHS; do
    python run_model.py -mode eval -model_checkpoint "$MODEL_PATH" \
    -task "$TASK" -output_path ./Output \
    -id_te_data_path "./Dataset/${DATASET_TYPE}/${TASK}/test.csv"
done
