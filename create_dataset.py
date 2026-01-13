import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import os

from InstructABSA.data_prep import DatasetLoader
# from InstructABSA.utils import T5Generator, T5Classifier
from instructions_indo import InstructionsHandler

# Load the data
id_train_file_path = 'instruct_absa/indo/hoasa_hotel/train.csv'
id_test_file_path = 'instruct_absa/indo/hoasa_hotel/test.csv'
id_dev_file_path = 'instruct_absa/indo/hoasa_hotel/dev.csv'
id_tr_df = pd.read_csv(id_train_file_path, converters={"targets": eval})
id_te_df = pd.read_csv(id_test_file_path, converters={"targets": eval})
id_dev_df = pd.read_csv(id_dev_file_path, converters={"targets": eval})

# Get the input text into the required format using Instructions
instruct_handler = InstructionsHandler()

# Set instruction_set1 for InstructABSA-1 and instruction_set2 for InstructABSA-2
instruct_handler.load_instruction_set1()

# Set bos_instruct1 for lapt14 and bos_instruct2 for rest14. For other datasets, modify the insructions.py file.
loader = DatasetLoader(id_tr_df, id_te_df, id_dev_df)
# loader.train_df_id = loader.create_data_in_ate_format(loader.train_df_id, 'term', 'raw_text', 'targets', instruct_handler.ate['bos_instruct1'], instruct_handler.ate['eos_instruct'])
# loader.test_df_id = loader.create_data_in_ate_format(loader.test_df_id, 'term', 'raw_text', 'targets', instruct_handler.ate['bos_instruct1'], instruct_handler.ate['eos_instruct'])
# loader.val_df_id = loader.create_data_in_ate_format(loader.val_df_id, 'term', 'raw_text', 'targets', instruct_handler.ate['bos_instruct1'], instruct_handler.ate['eos_instruct'])

# os.makedirs('Dataset/hoasa_hotel/ate/', exist_ok=True)
# loader.train_df_id.to_csv('Dataset/hoasa_hotel/ate/train.csv', index=False)
# loader.val_df_id.to_csv('Dataset/hoasa_hotel/ate/dev.csv', index=False)
# loader.test_df_id.to_csv('Dataset/hoasa_hotel/ate/test.csv', index=False)

# loader.train_df_id = loader.create_data_in_atsc_format(loader.train_df_id, 'targets', 'term', 'raw_text', 'aspect', instruct_handler.atsc['bos_instruct1'], instruct_handler.atsc['delim_instruct'], instruct_handler.atsc['eos_instruct'])
# loader.test_df_id = loader.create_data_in_atsc_format(loader.test_df_id, 'targets', 'term', 'raw_text', 'aspect', instruct_handler.atsc['bos_instruct1'], instruct_handler.atsc['delim_instruct'], instruct_handler.atsc['eos_instruct'])
# loader.val_df_id = loader.create_data_in_atsc_format(loader.val_df_id, 'targets', 'term', 'raw_text', 'aspect', instruct_handler.atsc['bos_instruct1'], instruct_handler.atsc['delim_instruct'], instruct_handler.atsc['eos_instruct'])

# os.makedirs('Dataset/hoasa_hotel/atsc/', exist_ok=True)
# loader.train_df_id.to_csv('Dataset/hoasa_hotel/atsc/train.csv', index=False)
# loader.val_df_id.to_csv('Dataset/hoasa_hotel/atsc/dev.csv', index=False)
# loader.test_df_id.to_csv('Dataset/hoasa_hotel/atsc/test.csv', index=False)

# loader.train_df_id = loader.create_data_in_aspe_format(loader.train_df_id, 'term', 'polarity', 'raw_text', 'targets', instruct_handler.aspe['bos_instruct1'], instruct_handler.aspe['eos_instruct'])
# loader.val_df_id = loader.create_data_in_aspe_format(loader.val_df_id, 'term', 'polarity', 'raw_text', 'targets', instruct_handler.aspe['bos_instruct1'], instruct_handler.aspe['eos_instruct'])
# loader.test_df_id = loader.create_data_in_aspe_format(loader.test_df_id, 'term', 'polarity', 'raw_text', 'targets', instruct_handler.aspe['bos_instruct1'], instruct_handler.aspe['eos_instruct'])

# os.makedirs('Dataset/hoasa_hotel/aspe/', exist_ok=True)
# loader.train_df_id.to_csv('Dataset/hoasa_hotel/aspe/train.csv', index=False)
# loader.val_df_id.to_csv('Dataset/hoasa_hotel/aspe/dev.csv', index=False)
# loader.test_df_id.to_csv('Dataset/hoasa_hotel/aspe/test.csv', index=False)

# loader.train_df_id = loader.create_data_in_aooe_format(loader.train_df_id, aspect_col='targets', opinion_col='targets', key='term', text_col='raw_text', bos_instruction=instruct_handler.aooe['bos_instruct1'], delim_instruction=instruct_handler.aooe['delim_instruct'], eos_instruction=instruct_handler.aooe['eos_instruct'])
# loader.val_df_id = loader.create_data_in_aooe_format(loader.val_df_id, aspect_col='targets', opinion_col='targets', key='term', text_col='raw_text', bos_instruction=instruct_handler.aooe['bos_instruct1'], delim_instruction=instruct_handler.aooe['delim_instruct'], eos_instruction=instruct_handler.aooe['eos_instruct'])
# loader.test_df_id = loader.create_data_in_aooe_format(loader.test_df_id, aspect_col='targets', opinion_col='targets', key='term', text_col='raw_text', bos_instruction=instruct_handler.aooe['bos_instruct1'], delim_instruction=instruct_handler.aooe['delim_instruct'], eos_instruction=instruct_handler.aooe['eos_instruct'])

# os.makedirs('Dataset/hoasa_hotel/aooe/', exist_ok=True)
# loader.train_df_id.to_csv('Dataset/hoasa_hotel/aooe/train.csv', index=False)
# loader.val_df_id.to_csv('Dataset/hoasa_hotel/aooe/dev.csv', index=False)
# loader.test_df_id.to_csv('Dataset/hoasa_hotel/aooe/test.csv', index=False)

# loader.train_df_id = loader.create_data_in_aope_format(loader.train_df_id, text_col='raw_text', target_col='targets', aspect_key='term', opinion_key='opinion', bos_instruction=instruct_handler.aope['bos_instruct1'], eos_instruction=instruct_handler.aope['eos_instruct'])
# loader.val_df_id = loader.create_data_in_aope_format(loader.val_df_id, text_col='raw_text', target_col='targets', aspect_key='term', opinion_key='opinion', bos_instruction=instruct_handler.aope['bos_instruct1'], eos_instruction=instruct_handler.aope['eos_instruct'])
# loader.test_df_id = loader.create_data_in_aope_format(loader.test_df_id, text_col='raw_text', target_col='targets', aspect_key='term', opinion_key='opinion', bos_instruction=instruct_handler.aope['bos_instruct1'], eos_instruction=instruct_handler.aope['eos_instruct'])

# os.makedirs('Dataset/hoasa_hotel/aope/', exist_ok=True)
# loader.train_df_id.to_csv('Dataset/hoasa_hotel/aope/train.csv', index=False)
# loader.val_df_id.to_csv('Dataset/hoasa_hotel/aope/dev.csv', index=False)
# loader.test_df_id.to_csv('Dataset/hoasa_hotel/aope/test.csv', index=False)

loader.train_df_id = loader.create_data_in_aoste_format(loader.train_df_id, target_col='targets', text_col='raw_text', bos_instruction=instruct_handler.aoste['bos_instruct1'], eos_instruction=instruct_handler.aoste['eos_instruct'])
loader.val_df_id = loader.create_data_in_aoste_format(loader.val_df_id, text_col='raw_text', target_col='targets', bos_instruction=instruct_handler.aoste['bos_instruct1'], eos_instruction=instruct_handler.aoste['eos_instruct'])
loader.test_df_id = loader.create_data_in_aoste_format(loader.test_df_id, text_col='raw_text', target_col='targets', bos_instruction=instruct_handler.aoste['bos_instruct1'], eos_instruction=instruct_handler.aoste['eos_instruct'])

os.makedirs('Dataset/hoasa_hotel/aoste/', exist_ok=True)
loader.train_df_id.to_csv('Dataset/hoasa_hotel/aoste/train.csv', index=False)
loader.val_df_id.to_csv('Dataset/hoasa_hotel/aoste/dev.csv', index=False)
loader.test_df_id.to_csv('Dataset/hoasa_hotel/aoste/test.csv', index=False)