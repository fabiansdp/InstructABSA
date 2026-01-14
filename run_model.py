import os
import warnings
warnings.filterwarnings('ignore')
import pandas as pd

import torch
from InstructABSA.data_prep import DatasetLoader
from InstructABSA.utils import T5Generator, T5Classifier
from InstructABSA.config import Config
from instructions_indo import InstructionsHandler

# import wandb
from datetime import datetime

try:
    use_mps = True if torch.has_mps else False
except:
    use_mps = False

# Set Global Values
config = Config()
instruct_handler = InstructionsHandler()
if config.inst_type == 1:
    instruct_handler.load_instruction_set1()
else:
    instruct_handler.load_instruction_set2()

current_time = datetime.now().strftime('%Y%m%d_%H%M%S')
print('Task: ', config.task)

if config.mode == 'train':
    if config.id_tr_data_path is None:
        raise Exception('Please provide training data path for mode=training.')
    
if config.mode == 'eval':
    if config.id_te_data_path is None and config.ood_te_data_path is None:
        raise Exception('Please provide testing data path for mode=eval.')

if config.experiment_name is not None and config.mode == 'train':
    print('Experiment Name: ', config.experiment_name)
    model_checkpoint = config.model_checkpoint
    model_out_path = config.output_dir
    model_out_path = os.path.join(model_out_path, config.task, f"{model_checkpoint.replace('/', '')}-{config.experiment_name}-{current_time}")
else:
    model_checkpoint = config.model_checkpoint
    model_out_path = config.model_checkpoint

print('Mode set to: ', 'training' if config.mode == 'train' else ('inference' if config.mode == 'eval' \
                                                                  else 'Individual sample inference'))

# Load the data
id_tr_data_path = config.id_tr_data_path
id_te_data_path = config.id_te_data_path
id_val_data_path = config.id_val_data_path

ood_tr_data_path = config.ood_tr_data_path
ood_te_data_path = config.ood_te_data_path

if config.mode != 'cli':
    id_tr_df, id_te_df, id_val_df = None, None, None
    ood_tr_df,  ood_te_df = None, None
    if id_tr_data_path is not None:
        id_tr_df = pd.read_csv(id_tr_data_path)
    if id_te_data_path is not None:
        id_te_df = pd.read_csv(id_te_data_path)
    if id_val_data_path is not None:
        id_val_df = pd.read_csv(id_val_data_path)
    if ood_tr_data_path is not None:
        ood_tr_df = pd.read_csv(ood_tr_data_path)
    if ood_te_data_path is not None:
        ood_te_df = pd.read_csv(ood_te_data_path)
    print('Loaded data...')
else:
    print('Running inference on input: ', config.test_input)

# Create T5 model object
print(config.set_instruction_key)
if config.set_instruction_key == 1:
    indomain = 'bos_instruct1'
    outdomain = 'bos_instruct2'
else:
    indomain = 'bos_instruct2'
    outdomain = 'bos_instruct1'

if config.task == 'ate':
    t5_exp = T5Generator(model_checkpoint)
    bos_instruction_id = instruct_handler.ate[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.ate[outdomain]
    eos_instruction = instruct_handler.ate['eos_instruct']
if config.task == 'aspe':
    t5_exp = T5Generator(model_checkpoint)
    bos_instruction_id = instruct_handler.aspe[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.aspe[outdomain]
    eos_instruction = instruct_handler.aspe['eos_instruct']
if config.task == 'aoste':
    t5_exp = T5Generator(model_checkpoint)
    bos_instruction_id = instruct_handler.aoste[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.aoste[outdomain]
    eos_instruction = instruct_handler.aoste['eos_instruct']
if config.task == 'aope':
    t5_exp = T5Generator(model_checkpoint)
    bos_instruction_id = instruct_handler.aope[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.aope[outdomain]
    eos_instruction = instruct_handler.aope['eos_instruct']
if config.task == 'aooe':
    t5_exp = T5Classifier(model_checkpoint)
    bos_instruction_id = instruct_handler.aooe[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.aooe[outdomain]
    delim_instruction = instruct_handler.aooe['delim_instruct']
    eos_instruction = instruct_handler.aooe['eos_instruct']
if config.task == 'atsc':
    t5_exp = T5Classifier(model_checkpoint)
    bos_instruction_id = instruct_handler.atsc[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.atsc[outdomain]
    delim_instruction = instruct_handler.atsc['delim_instruct']
    eos_instruction = instruct_handler.atsc['eos_instruct']
if config.task == 'joint':
    t5_exp = T5Generator(model_checkpoint)
    bos_instruction_id = instruct_handler.joint[indomain]
    if ood_tr_data_path is not None or ood_te_data_path is not None:
        bos_instruction_ood = instruct_handler.joint[outdomain]
    eos_instruction = instruct_handler.joint['eos_instruct']

if config.mode != 'cli':
    # Define function to load datasets and tokenize datasets
    loader = DatasetLoader(train_df_id=id_tr_df, test_df_id=id_te_df, val_df_id=id_val_df, sample_size=config.sample_size)

    # Tokenize dataset
    id_ds, id_tokenized_ds, ood_ds, ood_tokenized_ds = loader.set_data_for_training_semeval(t5_exp.tokenize_function_inputs) 

    if config.mode == 'train':
        # Train model
        print("Using learning rate:", config.learning_rate)
        # Training arguments
        training_args = {
            'output_dir': model_out_path,
            'eval_strategy': config.evaluation_strategy if config.id_te_data_path is not None else 'no',
            'learning_rate': config.learning_rate,
            'per_device_train_batch_size': config.per_device_train_batch_size if config.per_device_train_batch_size is not None else None,
            'per_device_eval_batch_size': config.per_device_eval_batch_size,
            'num_train_epochs': config.num_train_epochs if config.num_train_epochs is not None else None,
            'weight_decay': config.weight_decay,
            'warmup_ratio': config.warmup_ratio,
            'save_strategy': config.save_strategy,
            'load_best_model_at_end': config.load_best_model_at_end,
            'push_to_hub': config.push_to_hub,
            'eval_accumulation_steps': config.eval_accumulation_steps,
            'predict_with_generate': config.predict_with_generate,
            'use_mps_device': use_mps,
            'logging_strategy': 'steps',
            # 'logging_steps': 1,
            # 'report_to': 'wandb',
            # 'run_name': f"instruct_absa_mt5_lr-{config.learning_rate}_samplesize-{config.sample_size if config.sample_size is not None else 'all'}_data-{config.id_tr_data_path.split('/')[3]}_{current_time}",

            'seed': config.seed,
            'data_seed': config.seed
        }
        # os.environ["WANDB_PROJECT"] = "instruct-absa-seq2seq"
        model_trainer = t5_exp.train(id_tokenized_ds, **training_args)
        print('Model saved at: ', model_out_path)
    elif config.mode == 'eval':
        # Get prediction labels
        print('Model loaded from: ', model_checkpoint)
        if id_tokenized_ds.get("train") is not None:
            id_tr_pred_labels = t5_exp.get_labels(tokenized_dataset = id_tokenized_ds, sample_set = 'train', 
                                                  batch_size=config.per_device_eval_batch_size, 
                                                  max_length = config.max_token_length)
            id_tr_df = pd.DataFrame(id_ds['train'])[['text', 'labels']]
            id_tr_df['labels'] = id_tr_df['labels'].apply(lambda x: x.strip())
            id_tr_df['pred_labels'] = id_tr_pred_labels
            id_tr_df.to_csv(os.path.join(config.output_path, f'{config.experiment_name}_id_train.csv'), index=False)
            print('*****Train Metrics*****')
            precision, recall, f1, accuracy = t5_exp.get_metrics(id_tr_df['labels'], id_tr_pred_labels)
            print('Precision: ', precision)
            print('Recall: ', recall)
            print('F1-Score: ', f1)
            if config.task == 'atsc' or config.task == 'aooe':
                print('Accuracy: ', accuracy)


        if id_tokenized_ds.get("test") is not None:
            output_dir = os.path.join(config.output_path, config.task, f"{model_checkpoint.split('/')[-1]}")
            os.makedirs(output_dir, exist_ok=True)
            id_te_pred_labels = t5_exp.get_labels(tokenized_dataset = id_tokenized_ds, sample_set = 'test', 
                                                  batch_size=config.per_device_eval_batch_size, 
                                                  max_length = config.max_token_length)
            id_te_df = pd.DataFrame(id_ds['test'])[['text', 'labels']]
            id_te_df.loc[id_te_df["labels"].isnull()] = "null"
            id_te_df['labels'] = id_te_df['labels'].str.strip()
            id_te_df['pred_labels'] = id_te_pred_labels
            id_te_df.to_csv(os.path.join(output_dir, 'raw_inference_results.csv'), index=False)

            print('*****Test Metrics*****')
            precision, recall, f1, accuracy = t5_exp.get_metrics(id_te_df['labels'], id_te_pred_labels)
            results_metrics = {
                "precision": precision,
                "recall": recall,
                "f1_score": f1,
            }
            print('Precision: ', precision)
            print('Recall: ', recall)
            print('F1-Score: ', f1)
            if config.task == 'atsc' or config.task == 'aooe':
                results_metrics["accuracy"] = accuracy
                print('Accuracy: ', accuracy)

            output_file = os.path.join(output_dir, 'evaluation_results.json')
            with open(output_file, 'w') as f:
                import json
                json.dump(results_metrics, f, indent=4)
            print(f"Saved evaluation results to {output_file}")

        if ood_tokenized_ds.get("train") is not None:
            ood_tr_pred_labels = t5_exp.get_labels(tokenized_dataset = ood_tokenized_ds, sample_set = 'train', 
                                                   batch_size=config.per_device_eval_batch_size, 
                                                   max_length = config.max_token_length)
            ood_tr_df = pd.DataFrame(ood_ds['train'])[['text', 'labels']]
            ood_tr_df['labels'] = ood_tr_df['labels'].apply(lambda x: x.strip())
            ood_tr_df['pred_labels'] = ood_tr_pred_labels
            ood_tr_df.to_csv(os.path.join(config.output_path, f'{config.experiment_name}_ood_train.csv'), index=False)
            print('*****Train Metrics - OOD*****')
            precision, recall, f1, accuracy = t5_exp.get_metrics(ood_tr_df['labels'], ood_tr_pred_labels)
            print('Precision: ', precision)
            print('Recall: ', precision)
            print('F1-Score: ', precision)
            if config.task == 'atsc' or config.task == 'aooe':
                print('Accuracy: ', accuracy)
            
        if ood_tokenized_ds.get("test") is not None:
            ood_te_pred_labels = t5_exp.get_labels(tokenized_dataset = ood_tokenized_ds, sample_set = 'test', 
                                                   batch_size=config.per_device_eval_batch_size, 
                                                   max_length = config.max_token_length)
            ood_te_df = pd.DataFrame(ood_ds['test'])[['text', 'labels']]
            ood_te_df['labels'] = ood_te_df['labels'].apply(lambda x: x.strip())
            ood_te_df['pred_labels'] = ood_te_pred_labels
            ood_te_df.to_csv(os.path.join(config.output_path, f'{config.experiment_name}_ood_test.csv'), index=False)
            print('*****Test Metrics - OOD*****')
            precision, recall, f1, accuracy = t5_exp.get_metrics(ood_te_df['labels'], ood_te_pred_labels)
            print('Precision: ', precision)
            print('Recall: ', precision)
            print('F1-Score: ', precision)
            if config.task == 'atsc' or config.task == 'aooe':
                print('Accuracy: ', accuracy)
else:
    print('Model loaded from: ', model_checkpoint)
    if config.task == 'atsc' or config.task == 'aooe':
        config.test_input, aspect_term = config.test_input.split('|')[0], config.test_input.split('|')[1]
        model_input = bos_instruction_id + config.test_input + f'. The aspect term is: {aspect_term}' + eos_instruction
    else:
        model_input = bos_instruction_id + config.test_input + eos_instruction
    input_ids = t5_exp.tokenizer(model_input, return_tensors="pt").input_ids
    outputs = t5_exp.model.generate(input_ids, max_length = config.max_token_length)
    print('Model output: ', t5_exp.tokenizer.decode(outputs[0], skip_special_tokens=True))
