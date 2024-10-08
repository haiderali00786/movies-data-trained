# -*- coding: utf-8 -*-
"""gpt movies data trained

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1dJ0lBNcVbGvvpjNtucjp1NfHxkcboHqK
"""

# IMPORTANT: RUN THIS CELL IN ORDER TO IMPORT YOUR KAGGLE DATA SOURCES
# TO THE CORRECT LOCATION (/kaggle/input) IN YOUR NOTEBOOK,
# THEN FEEL FREE TO DELETE THIS CELL.
# NOTE: THIS NOTEBOOK ENVIRONMENT DIFFERS FROM KAGGLE'S PYTHON
# ENVIRONMENT SO THERE MAY BE MISSING LIBRARIES USED BY YOUR
# NOTEBOOK.

import os
import sys
from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from urllib.parse import unquote, urlparse
from urllib.error import HTTPError
from zipfile import ZipFile
import tarfile
import shutil

CHUNK_SIZE = 40960
DATA_SOURCE_MAPPING = 'movies:https%3A%2F%2Fstorage.googleapis.com%2Fkaggle-data-sets%2F5620198%2F9284793%2Fbundle%2Farchive.zip%3FX-Goog-Algorithm%3DGOOG4-RSA-SHA256%26X-Goog-Credential%3Dgcp-kaggle-com%2540kaggle-161607.iam.gserviceaccount.com%252F20240901%252Fauto%252Fstorage%252Fgoog4_request%26X-Goog-Date%3D20240901T135934Z%26X-Goog-Expires%3D259200%26X-Goog-SignedHeaders%3Dhost%26X-Goog-Signature%3D2659bfdc4f29c55d1ce1c627c3d2c396bebb7b9a321da4d9d2145c8130eef93eb166c823cf06e7c0c0a1bbb308b59719f5314fb9d4c3e18264693e47d30b4c052fc606157fbcf910186fc3019c16d35e2c9577f14d7e848b4f547ce24247fa1d770aeca44cd42e95457cbd56370eb9a280183e926e63ca372f17a622a2a99b34e733db5249b6f8ceb9da1ca18f574273024e95418a965a8106cb9283bff191515f881a7752aa59ad012d860a022809aff20624445336af3b565a5b7bb3669045baf76b59036b68d3fce5f9dc6c57ca91d9f86e5f1bd5d117d44a260b75c7b47dddc20ab626c290fd491d60e501e5750b9363534d901e81f06f16374110b64848'

KAGGLE_INPUT_PATH='/kaggle/input'
KAGGLE_WORKING_PATH='/kaggle/working'
KAGGLE_SYMLINK='kaggle'

!umount /kaggle/input/ 2> /dev/null
shutil.rmtree('/kaggle/input', ignore_errors=True)
os.makedirs(KAGGLE_INPUT_PATH, 0o777, exist_ok=True)
os.makedirs(KAGGLE_WORKING_PATH, 0o777, exist_ok=True)

try:
  os.symlink(KAGGLE_INPUT_PATH, os.path.join("..", 'input'), target_is_directory=True)
except FileExistsError:
  pass
try:
  os.symlink(KAGGLE_WORKING_PATH, os.path.join("..", 'working'), target_is_directory=True)
except FileExistsError:
  pass

for data_source_mapping in DATA_SOURCE_MAPPING.split(','):
    directory, download_url_encoded = data_source_mapping.split(':')
    download_url = unquote(download_url_encoded)
    filename = urlparse(download_url).path
    destination_path = os.path.join(KAGGLE_INPUT_PATH, directory)
    try:
        with urlopen(download_url) as fileres, NamedTemporaryFile() as tfile:
            total_length = fileres.headers['content-length']
            print(f'Downloading {directory}, {total_length} bytes compressed')
            dl = 0
            data = fileres.read(CHUNK_SIZE)
            while len(data) > 0:
                dl += len(data)
                tfile.write(data)
                done = int(50 * dl / int(total_length))
                sys.stdout.write(f"\r[{'=' * done}{' ' * (50-done)}] {dl} bytes downloaded")
                sys.stdout.flush()
                data = fileres.read(CHUNK_SIZE)
            if filename.endswith('.zip'):
              with ZipFile(tfile) as zfile:
                zfile.extractall(destination_path)
            else:
              with tarfile.open(tfile.name) as tarfile:
                tarfile.extractall(destination_path)
            print(f'\nDownloaded and uncompressed: {directory}')
    except HTTPError as e:
        print(f'Failed to load (likely expired) {download_url} to path {destination_path}')
        continue
    except OSError as e:
        print(f'Failed to load {download_url} to path {destination_path}')
        continue

print('Data source import complete.')

!pip install numpy==1.26.4

# This Python 3 environment comes with many helpful analytics libraries installed
# It is defined by the kaggle/python Docker image: https://github.com/kaggle/docker-python
# For example, here's several helpful packages to load

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Input data files are available in the read-only "../input/" directory
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# You can write up to 20GB to the current directory (/kaggle/working/) that gets preserved as output when you create a version using "Save & Run All"
# You can also write temporary files to /kaggle/temp/, but they won't be saved outside of the current session

pip install pandas

pip install --upgrade transformers huggingface_hub

import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

import nltk
nltk.download('punkt')
import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Assuming you're working in a Kaggle notebook
file_path = "/kaggle/input/movies/aclImdb/test/neg/10000_4.txt"

# Load the file into a DataFrame
data = pd.read_csv(file_path, header=None, names=["review"])

# Extract the review text
review_text = data["review"].iloc[0]

# Tokenize the review text
tokens = word_tokenize(review_text)

print(tokens)

import pandas as pd
import os

folder_path = "/kaggle/input/movies/aclImdb"

import os
import pandas as pd

# Base folder path
folder_path = "/kaggle/input/movies/aclImdb"

# Subfolder paths
subfolders = [
    "test/neg",
    "test/pos",
    "train/neg",
    "train/pos"
]

# List to hold individual DataFrames
dataframes = []

# Iterate through each subfolder
for subfolder in subfolders:
    full_path = os.path.join(folder_path, subfolder)

    if os.path.exists(full_path) and os.path.isdir(full_path):
        print(f"Processing subfolder: {full_path}")

        # Iterate through files in the current subfolder
        for file in os.listdir(full_path):
            file_path = os.path.join(full_path, file)

            # Assuming the files are text files, adjust if necessary
            if file.endswith('.txt'):
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # You might want to label the data based on the folder structure
                    label = 'positive' if 'pos' in subfolder else 'negative'
                    dataframes.append({'review': content, 'sentiment': label})

    else:
        print(f"Subfolder path {full_path} doesn't exist or is not a directory.")

# Create a DataFrame from the collected data
if dataframes:
    df = pd.DataFrame(dataframes)
    print(f"Final DataFrame shape: {df.shape}")
    print(df.head())  # Display the first few rows of the DataFrame
else:
    print("No files found to process.")

import os
import pandas as pd

def load_acl_imdb(data_dir):
    """Loads the ACLIMDB dataset.

    Args:
        data_dir: The directory containing the ACLIMDB dataset.

    Returns:
        A pandas DataFrame with columns 'review' and 'label'.
    """

    reviews = []
    labels = []

    # Loop through the 'train' and 'test' subdirectories
    for subdir in ["train", "test"]:
        subdir_path = os.path.join(data_dir, subdir)

        # Loop through 'pos' and 'neg' subdirectories within each subdir
        for label_dir in ["pos", "neg"]:
            label_dir_path = os.path.join(subdir_path, label_dir)

            # Process each file in the label directory
            for filename in os.listdir(label_dir_path):
                file_path = os.path.join(label_dir_path, filename)

                with open(file_path, "r", encoding="utf-8") as f:
                    review_text = f.read()
                    reviews.append(review_text)
                    labels.append('positive' if label_dir == 'pos' else 'negative')  # Use 'positive' or 'negative'

    # Create a DataFrame from the lists
    data = pd.DataFrame({"review": reviews, "label": labels})
    return data

# Replace with your actual data directory
data_dir = "/kaggle/input/movies/aclImdb"
df = load_acl_imdb(data_dir)

# Display the shape and first few rows of the DataFrame to verify
print(df.shape)
print(df.head())

print(df.shape)  # Output: (50000, 2)

import random

random_index = random.randint(0, len(df))
print(df.iloc[random_index])

!pip show transformers

from transformers import AutoTokenizer, AutoModelForSequenceClassification, Trainer, TrainingArguments

try:
    import transformers
    print("Transformers library is installed.")
except ModuleNotFoundError:
    print("Transformers library is not installed.")

import os
import pandas as pd
from transformers import AutoTokenizer

def load_acl_imdb(data_dir):
    """Loads the ACLIMDB dataset from both train and test subsets and tokenizes the reviews.

    Args:
        data_dir: The directory containing the ACLIMDB dataset.

    Returns:
        A pandas DataFrame with columns 'review', 'label', and 'tokens'.
    """

    reviews = []
    labels = []
    tokenized_reviews = []

    # Initialize the BERT tokenizer
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

    # Loop through the 'train' and 'test' subdirectories
    for subdir in ["train", "test"]:
        subdir_path = os.path.join(data_dir, subdir)

        if not os.path.exists(subdir_path):
            print(f"Warning: {subdir_path} does not exist. Skipping...")
            continue

        # Loop through 'pos' and 'neg' subdirectories within each subset
        for label_dir in ["pos", "neg"]:
            label_dir_path = os.path.join(subdir_path, label_dir)

            if not os.path.exists(label_dir_path):
                print(f"Warning: {label_dir_path} does not exist. Skipping...")
                continue

            # Process each file in the label directory
            for filename in os.listdir(label_dir_path):
                file_path = os.path.join(label_dir_path, filename)

                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        review_text = f.read()
                        reviews.append(review_text)
                        labels.append('positive' if label_dir == 'pos' else 'negative')

                        # Tokenize the review
                        encoded_review = tokenizer(
                            review_text,
                            padding='max_length',
                            truncation=True,
                            max_length=512,
                            return_tensors='pt'
                        )
                        tokenized_reviews.append(encoded_review['input_ids'].squeeze().tolist())

                except Exception as e:
                    print(f"Error processing {file_path}: {e}")

    # Create a DataFrame from the lists
    data = pd.DataFrame({
        "review": reviews,
        "label": labels,
        "tokens": tokenized_reviews
    })

    return data

# Replace with your actual data directory
data_dir = "/kaggle/input/movies/aclImdb"

# Load all data from both 'train' and 'test' subsets
df = load_acl_imdb(data_dir)

# Display the shape and first few rows of the DataFrame to verify
print(df.shape)  # Expected output: (50000, 3)
print(df.head())

from transformers import AutoTokenizer

try:
    tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
    print("Tokenizer loaded successfully!")
    print("Example Tokenized Output:", tokenizer("Hello, world!"))
except Exception as e:
    print(f"An error occurred: {e}")

import pandas as pd
from transformers import AutoTokenizer

# Load tokenizer
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')

# Define tokenize function
def tokenize_function(review):
    return tokenizer(review, padding="max_length", truncation=True, return_tensors='pt')

# Sample DataFrame
df = pd.DataFrame({
    'review': [
        "This is a positive review.",
        "This is a negative review."
    ]
})

# Apply tokenize function to each review in the DataFrame
tokenized_datasets = df['review'].apply(tokenize_function)

# Convert to list or other desired format if needed
tokenized_datasets = tokenized_datasets.tolist()

# Example output
for example in tokenized_datasets:
    print(example)

!pip install datasets  # Install the 'datasets' library

pip install --upgrade datasets transformers

!pip install --force-reinstall pyarrow

from datasets import Dataset

# Create a simple DataFrame
import pandas as pd
data = {'review': ["I love this!", "I hate this!"]}
df = pd.DataFrame(data)

# Convert DataFrame to Dataset
dataset = Dataset.from_pandas(df)
print(dataset)



from datasets import Dataset

dataset = Dataset.from_pandas(df)

def tokenize_function(examples):
    return tokenizer(examples['review'], padding="max_length", truncation=True) # Access the 'review' column within examples

tokenized_dataset = dataset.map(tokenize_function, batched=True)

train_test = tokenized_dataset.train_test_split(test_size=0.2)
train_dataset = train_test['train']
test_dataset = train_test['test']

model = AutoModelForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=16,
    per_device_eval_batch_size=64,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

from datasets import load_metric
from sklearn.metrics import accuracy_score, f1_score

# Ensure your model is set up for sequence classification and that labels are passed correctly during training.
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
)

# Add a compute_metrics function
def compute_metrics(pred):
  labels = pred.label_ids
  preds = pred.predictions.argmax(-1)
  f1 = f1_score(labels, preds, average="weighted")
  acc = accuracy_score(labels, preds)
  return {"accuracy": acc, "f1": f1}

# Pass the compute_metrics function to the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)

from transformers import TrainingArguments

training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,  # Log every 10 steps
    eval_strategy='epoch',  # Updated to eval_strategy
    save_strategy='epoch',  # Save checkpoints at the end of each epoch
    load_best_model_at_end=True  # Load the best model when finished training
)

from datasets import load_metric
from sklearn.metrics import accuracy_score, f1_score
from transformers import TrainingArguments, Trainer

# Define training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,  # Log every 10 steps
    eval_strategy='epoch',  # Updated to eval_strategy
    save_strategy='epoch',  # Save checkpoints at the end of each epoch
    load_best_model_at_end=True  # Load the best model when finished training
)

# Define compute_metrics function
def compute_metrics(pred):
  labels = pred.label_ids
  preds = pred.predictions.argmax(-1)
  f1 = f1_score(labels, preds, average="weighted")
  acc = accuracy_score(labels, preds)
  return {"accuracy": acc, "f1": f1}

# Create Trainer object with compute_metrics
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset,
    compute_metrics=compute_metrics,
)

# Evaluate the model and get the metrics
eval_results = trainer.evaluate()

# Print the evaluation results with metrics
print(eval_results)

model.save_pretrained('./model')
tokenizer.save_pretrained('./model')

!apt-get install git

!git clone https://github.com/haiderali00786/movies-data-trained.git

# Commented out IPython magic to ensure Python compatibility.
# %cd movies-data-trained



# Save the model using save_pretrained
model.save_pretrained('/content/drive/My Drive/your_model')

!zip -r /content/drive/My\ Drive/your_model.zip /content/drive/My\ Drive/your_model
from google.colab import files
files.download('/content/drive/My Drive/your_model.zip')