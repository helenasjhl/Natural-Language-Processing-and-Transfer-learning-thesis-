# -*- coding: utf-8 -*-
"""Kódlista Szakdolgozat

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14ASXuBNdUv76EAdeM-u2XfUCk3BmE0lM

4.2
"""

!python --version

from transformers import pipeline
# Elfogultság detektálása egy előre betanított modellen
unmasker = pipeline('fill-mask', model='bert-base-uncased')
result = unmasker("The doctor was a [MASK].")
print(result)

"""6.1"""

import spacy
# SpaCy betöltése
nlp = spacy.load("en_core_web_sm")
# Szöveg elemzése
text = "Apple is looking at buying U.K. startup for $1 billion."
doc = nlp(text)
# Név entitás felismerés
for ent in doc.ents:
 print(ent.text, ent.label_)

"""8.1.3"""

from transformers import BertTokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
text = "Hello, world!"
tokens = tokenizer.tokenize(text)
print(tokens)

"""8.1.4"""

import sentencepiece as spm
# Train SentencePiece model
spm.SentencePieceTrainer.train(input='text.txt', model_prefix='spm', vocab_size=200)
# Load SentencePiece model
sp = spm.SentencePieceProcessor(model_file='spm.model')
# Tokenize text
text = "This is an example sentence."
tokens = sp.encode_as_pieces(text)
print(tokens)

"""8.1.4/2"""

import jieba
text = "我来到北京清华大学"
tokens = jieba.cut(text)
print(list(tokens))

"""8.2.3"""

import re
# Szövegek listája
texts = ["Hello, world!",
    "Natural Language Processing with Python.",
    "Tokenization is a important step in NLP."]
# Tisztítás és normalizálás
def clean_text(text):
    text = text.lower()  # Kisbetűsre alakítás
    text = re.sub(r'\W', ' ', text)  # Nem alfanumerikus karakterek eltávolítása
    text = re.sub(r'\s+', ' ', text)  # Többszörös szóközök eltávolítása
    return text
cleaned_texts = [clean_text(text) for text in texts]
print(cleaned_texts)

"""8.2.4"""

# Telepítsd a Label Studio-t
!pip install label-studio

# Indítsd el a Label Studio-t
!label-studio start

"""10.2

wandb key
**b37cebd790c0188797b1211d340b2f4d48ccddeb**`
"""

import torch
from torch.utils.data import Dataset, DataLoader
from transformers import BertTokenizer, BertForSequenceClassification, Trainer, TrainingArguments

# Definiálj egy Dataset osztályt
class StoryDataset(Dataset):
    def __init__(self, texts, labels, tokenizer, max_length=512):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        text = self.texts[idx]
        label = self.labels[idx]
        encoding = self.tokenizer(
            text,
            truncation=True,
            padding='max_length',
            max_length=self.max_length,
            return_tensors='pt'
        )
        return {
            'input_ids': encoding['input_ids'].flatten(),
            'attention_mask': encoding['attention_mask'].flatten(),
            'labels': torch.tensor(label, dtype=torch.long)
        }

# Adatok betöltése és előkészítése
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
texts = ["Your collection of stories..."]
labels = [0]  # Például, ha több kategóriát is szeretnénk használni

# Hozz létre egy Dataset példányt
dataset = StoryDataset(texts, labels, tokenizer)

# Modell betöltése
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Finomhangolás beállításai
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    warmup_steps=500,
    weight_decay=0.01,
    logging_dir='./logs',
)

# Trainer inicializálása
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    eval_dataset=dataset  # Külön validációs dataset ha lheetséges
)

# Modell betanítása
trainer.train()

"""10.3"""

from transformers import pipeline

# Elfogultság detektálása egy előre betanított modellen
unmasker = pipeline('fill-mask', model='bert-base-uncased')
result = unmasker("The doctor was a [MASK].")
print(result)

"""10.4"""

from transformers import pipeline
classifier = pipeline("zero-shot-classification")
text = "This is a great product."
labels = ["positive", "negative"]
result = classifier(text, candidate_labels=labels)
print(result)

from transformers import MarianMTModel, MarianTokenizer
model_name = 'Helsinki-NLP/opus-mt-en-de'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)
text = "Hello, how are you?"
translated = model.generate(**tokenizer.prepare_seq2seq_batch([text], return_tensors="pt"))
print([tokenizer.decode(t, skip_special_tokens=True) for t in translated])

"""11.2"""



"""11.3"""

from transformers import pipeline
ner = pipeline("ner", model="dbmdz/bert-large-cased-finetuned-conll03-english")
text = "Alice is a hairdresser at Apple."
entities = ner(text)
print(entities)

from transformers import pipeline
summarizer = pipeline("summarization")
text = """
In another moment down went Alice after it,
never once considering how in the world she was to get out again.
The rabbit-hole went straight on like a tunnel for some way, and then dipped suddenly down,
so suddenly that Alice had not a moment to think about stopping herself
before she found herself falling down what seemed to be a very deep well.
"""
summary = summarizer(text, max_length=50, min_length=25, do_sample=False)
print(summary)

"""12.2"""

!pip install transformers torch pandas gradio kaggle

import kagglehub
import pandas as pd
import os


# Adathalmaz letöltése
path = kagglehub.dataset_download("chayanonc/1000-folk-stories-around-the-world")

# A letöltött fájl elérési útjának meghatározása
file_path = os.path.join(path, os.listdir(path)[0])

# Adatok betöltése pandas DataFrame-be
df = pd.read_csv(file_path)

# Oszlopnevek kiíratása
print(df.columns)

# Szövegek kinyerése a megfelelő oszlopból
stories = df['full_text'].tolist()

print(stories[:1])  # Az első mese kiíratása

from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
import torch
import gradio as gr

# Modell és tokenizer betöltése a Hugging Face Hub segítségével
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token  # A pad token-t az eos token-hez rendeljük

model = GPT2LMHeadModel.from_pretrained('gpt2')

# Adatok tokenizálása
inputs = tokenizer(stories, return_tensors='pt', max_length=512, truncation=True, padding='max_length')

# Dataset létrehozása
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = item['input_ids'].clone()
        return item

    def __len__(self):
        return len(self.encodings['input_ids'])

dataset = CustomDataset(inputs)

# Finomhangolási beállítások
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=2,
    per_device_train_batch_size=1,
    per_device_eval_batch_size=1,
    warmup_steps=200,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
)

# Trainer inicializálása
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Modell betanítása
trainer.train()

"""12.3 TELJES MODELL - wandb key
**b37cebd790c0188797b1211d340b2f4d48ccddeb**
"""

!pip install transformers torch pandas gradio

import pandas as pd
import os
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
import torch
import gradio as gr

# Adathalmaz betöltése a Hugging Face-ről
df = pd.read_csv("hf://datasets/gofilipa/bedtime_stories/stories.csv")

# Ellenőrizzük az oszlopneveket
print(df.columns)

# Szövegek kinyerése a 'stories' oszlopból
stories = df['stories'].tolist()

print(stories[:1])  # Az első mese kiíratása

# Modell és tokenizer betöltése
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
tokenizer.pad_token = tokenizer.eos_token
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Eszközbeállítás
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Adatok tokenizálása
inputs = tokenizer(stories, return_tensors='pt', max_length=512, truncation=True, padding=True)

# Dataset létrehozása
class CustomDataset(torch.utils.data.Dataset):
    def __init__(self, encodings):
        self.encodings = encodings

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = item['input_ids'].clone()
        return item

    def __len__(self):
        return len(self.encodings['input_ids'])

dataset = CustomDataset(inputs)

# Finomhangolási beállítások
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=2,
    warmup_steps=200,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=50,
)

# Trainer inicializálása
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
)

# Modell betanítása
trainer.train()

#1.  Alap promptal

# Történetgeneráló funkció a finomhangolt nyelvezettel és stílusban
def generate_story(protagonist, location, brief_event, paragraphs, words_per_paragraph):
    # Alap prompt a megadott paraméterekkel, a finomhangolt nyelvezet alapján
    initial_prompt = (f"In the {location}, a brave explorer named {protagonist} found themselves on an unusual adventure. "
                      f"One day, {protagonist} discovered {brief_event}. This discovery would lead to wonders and challenges beyond their wildest dreams.")

    story = ""
    prompt = initial_prompt  # Start with the initial prompt for the first paragraph

    for i in range(paragraphs):
        # Generate input_ids with attention mask and set pad token id for reliable generation
        input_ids = tokenizer.encode(prompt, return_tensors='pt').to(device)
        attention_mask = torch.ones(input_ids.shape, device=device)

        output = model.generate(
            input_ids,
            max_length=words_per_paragraph + len(input_ids[0]),
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            temperature=0.7,  # Reduced temperature for more controlled output
            top_k=30,  # Lowered top_k for more focused choices
            top_p=0.9,
            do_sample=True,
            attention_mask=attention_mask,
            pad_token_id=tokenizer.eos_token_id
        )

        paragraph = tokenizer.decode(output[0], skip_special_tokens=True)

        # Add the generated paragraph to the story, removing any repeated prompt text
        story += "\n\n" + paragraph[len(prompt):]

        # Reset the prompt to keep reinforcing the initial setup for each new paragraph
        prompt = (f"As {protagonist} continued their adventure in the {location}, "
                  f"they thought back to the moment they discovered {brief_event}. Each step was filled with new mysteries and friends along the way.")

    return story.strip()

# Teszt mese generálása a megadott paraméterekkel
test_story = generate_story(
    protagonist="Adam",
    location="enchanted forest",
    brief_event="a glowing, magical animal",
    paragraphs=3,
    words_per_paragraph=100
)

print("Generated Test Story:")
print(test_story)

# 0.4 VERZIÓ
import torch
from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Modell és tokenizer betöltése
# tokenizer = GPT2Tokenizer.from_pretrained("your-fine-tuned-model-path")
# model = GPT2LMHeadModel.from_pretrained("your-fine-tuned-model-path")
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

# Minimális paraméterekkel működő történetgeneráló funkció
def test_fine_tuned_model_simple(protagonist="A brave adventurer Adam", max_length=300):
    # Egyszerű, mesés bevezető prompt
    intro_prompt = f"Once upon a time, {protagonist} went on an incredible journey."

    # Prompt tokenizálása és átküldése a modellnek
    input_ids = tokenizer.encode(intro_prompt, return_tensors='pt').to(device)

    # Generálás a modell segítségével
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.6,  # kreatívitás
        top_k=90,         # irányítottabb generálásért
        top_p=0.95,       # összpontosított történetért
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )

    # Kimenet dekódolása és visszaadása
    story = tokenizer.decode(output[0], skip_special_tokens=True)
    return story

# Teszt futtatása egy alapértelmezett főszereplővel
generated_story = test_fine_tuned_model_simple()

print("Generated Story:")
print(generated_story)