# 📌 **Saját Nyelvi Modell**

Ez a repository a **Saját Nyelvi Modell** fejlesztésére és alkalmazására szolgál, amely egy GPT-2 alapú mese generáló modell. A cél egy természetes nyelvi feldolgozáson (NLP) alapuló, transzfer tanulással finomhangolt AI létrehozása.

## 📖 **Bevezetés**&#x20;

A természetes nyelvi feldolgozás (NLP) egyik legfontosabb alkalmazási területe a szövegalkotás. Az utóbbi években a nagy nyelvi modellek (LLM) elterjedése lehetővé tette a mesterséges intelligencia számára, hogy koherens, emberi nyelven írt szövegeket generáljon. Ez a projekt egy GPT-2 alapú mese generáló modellt valósít meg, amely gyermekbarát történeteket képes előállítani.

## 📂 **Tartalom**

- **sajat\_model.txt** - A saját fejlesztésű modell teljes kódja
- **szakdolgozat.pdf** - A szakdolgozat, amely bemutatja a modell fejlesztési folyamatát
- **README.md** - Ez a dokumentum
- **kódlista_szakdolgozat** - A szakdolgozatomban lévő összes kódot tartalmazza, nem csak a saját modellt

## 🛠️ **Használt technológiák**

- **Python** (3.x)
- **Hugging Face Transformers** (GPT-2)
- **Torch** (PyTorch)
- **Pandas** (adatkezelés)
- **Gradio** (interaktív bemutató felület)

## 🧠 **Modell felépítése**

A modell egy előre betanított **GPT-2** nyelvi modell finomhangolásán alapul. A finomhangoláshoz a **Hugging Face Datasets** könyvtáron keresztül elérhető **'gofilipa/bedtime\_stories'** datasetet használtam, amely gyermekek számára készült esti meséket tartalmaz. Ennek célja, hogy a generált szövegek természetesebbek és élvezhetőbbek legyenek a fiatalabb közönség számára. Ennek célja, hogy a generált szövegek változatosak és kulturálisan gazdagok legyenek.
A modell egy előre betanított **GPT-2** nyelvi modell finomhangolásán alapul. A finomhangolás során mese adatbázisokat használtunk, hogy a generált szövegek a célközönség számára megfelelő stílusban és tartalommal készüljenek el.

## 📊 **Modell betanítása**

A betanításhoz a **Hugging Face Transformers** és **PyTorch** könyvtárakat használtuk. A finomhangolás folyamata:

1. Adatok előkészítése és tokenizálása
2. Modell finomhangolása előre betanított GPT-2 segítségével
3. Modell teljesítményének értékelése
4. Generált szövegek tesztelése és kiértékelése

A modell újratanításához:

```python
trainer.train()
```

## 🚀 **Hogyan használd?**

### 1. Telepítsd a szükséges csomagokat:

```bash
pip install transformers torch pandas gradio
```

### 2. Futtasd a modellt:

A saját modell betöltéséhez és használatához:

```python
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

# Modell és tokenizer betöltése
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2").to("cuda" if torch.cuda.is_available() else "cpu")

# Teszt generálás
prompt = "Egyszer volt, hol nem volt"
input_ids = tokenizer.encode(prompt, return_tensors='pt')
output = model.generate(input_ids, max_length=100, num_return_sequences=1)
print(tokenizer.decode(output[0], skip_special_tokens=True))
```

## 🔍 **Eredmények és jövőbeli fejlesztések**

A modell sikeresen generál meséket adott kulcsszavak alapján.

## ✅ **Következtetés**

A jelenlegi projekt egy hatékony módszert kínál arra, hogy a mesterséges intelligencia mese generálásra legyen képes. A transzfer tanulás révén elért finomhangolás lehetőséget biztosít a modell továbbfejlesztésére és szélesebb körű alkalmazására. 

