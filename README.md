# VIRA
## Vegan Information Retrieval Assistant
VIRA is a bot designed to accurately answer veganism questions!

![VIRA Screenshot]('./vegan_faq/static/VIRA_screenshot.png' "VIRA Screenshot")


Click [here](http://134.209.190.239:8501/) to try her out!

## **About**

### What is VIRA?
**VIRA** ('Vegan Information Retrieval Assistant') is a bot that tries to answer your
*veganism related* questions!


### How does VIRA work?
VIRA tries to match your question to its stored knowledge bank - and then return
the most relevant response.
VIRA is a 'closed domain' QA bot, and thus if the answer is not found in one of
VIRA's corpora, she will have a hard time answering the question!


### Tell me more about VIRA's knowledge bank
VIRA's knowledge bank was curated from various sources such as: reddit, wikipedia,
bbc news, & vegan related websites.
The set of questions & answers is quality controlled to ensure the responses
accurately represent veganism!

Currently VIRA's knowledge bank is small, and thus she won't always be able to
assist. It is however being continually updated!

### Tell me more about VIRA's information retrieval algorithm
VIRA utilises a 'Universal Sentence Encoder' algorithm. This approach was publicised
by google in [this](https://arxiv.org/abs/1803.11175) paper. Compared to traditional
methods such as word2vec or glove - which create word embeddings, Universal Sentence
Encoder creates 512 dimensional embeddings at the sentence level. VIRA will compare
the embeddings of your question, with those of the questions in her knowledge
bank - and then if there is a close enough match - retrive the answer!

Stay tuned for a full article on this approach, including what could be improved,
and why this algorithm was used over others!


### What is VIRA built on?
- The model is implemented in **TensorFlow2**
- The web application is implemented in **Streamlit**
- The website is hosted on a **Digital Ocean** droplet

---
### **Steps to run VIRA locally**

If you want to modify / enhance / improve VIRA, follow the below steps.

1. Clone the repository
```
git clone https://www.github.com/ME-64/VIRA
```

2. Navigate to directory
```
cd VIRA
```

3. Create a virtual environment (not required, but reccomended)
```
python -m venv .env 
```

4. Activate the virtual environment and install requirements
```
source .env/bin/activate

pip install -r requirements.txt
```

5. Download the model from TensorFlow Hub and save it in a directory called 'model'
```python
import tensorflow as tf
import tensorflow_hub as hub

model = hub.load('https://tfhub.dev/google/universal-sentence-encoder/4')

tf.saved_model.save(model, output_dir = 'vegan_faq/model')

```

6. Run the streamlit app!
```
streamlit run vegan_faq/VIRA.py
```

7. View the app in your browser of choice at `localhost:8501`

