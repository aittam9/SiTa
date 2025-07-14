# SiTA: a simple text anonymizer powered by NLP tools
---
#### Video Demo:  <[URL HERE](https://youtu.be/F8QF1_B9tBM)>
#### Description:
**SiTA** is a simple text anonymization tool built in streamlit with the python language. It leverages Natural Language Processing and Deep Learning tools to allow for an easy and flexible anonymization workflow. It allows for entities type customization, replacement method and preferred engine. It also allows to download the results in a txt file at the end of the anonimization.
The user interface allow for copy-paste or file uploading, with the latter supporting both txt and pdf files. Pdf files are converted into txt before running the anonymization process.
Once the text has been pasted or uploaded the user can see a pre-view of the entities found by the engine. All entities found by the engines are shown in the preview but only PERSON are anonymized by default. However, the set of entities can be expanded with custom options in the side bar menu. If *spacy* is chosen as an engine (which is also the default), there is a drop-and-select menu with which the user can select the entities he/she whishes to remove. If the engine is set to be *Gliner*, the user can directly type the entities he/she wants to remove. In this case, if more than one entity is typed, these should be written as a space separated list. 

The user can press the anonymize button and get another preview of the anonymized text. On the sidebar menu, the user can choose between two replacement methods. With the first one, *entity label* the spotted entity is replaced with its label (es. Donald Trump is a billionaire-> PERSON is a billionaire). The second option, *omississ*, will replace the entities with the dummy token *OMISSISS* (es. Donald Trump is a billionaire-> OMISSISS is a billionaire).

A convienent **sidebar menu** allows for some easy customization. Here you can:
- Choose your preferred engine
- Choose the entity you want to remove
- Choose an anomyzation method. You can replace the spotted entities you want to anonymize with their entity label or with a dummy token (OMISSIS)

### Main features:
- **Intuitive UI** built in [streamlit](https://streamlit.io/) where a user can:
    - Copy-Paste some text or upload a document (PDF and TXT supported)
- **Named Entity Recognition module**
    - Two Engines: Spacy (default) and GliNER
- **Custom entities** to anonymize.
    - Select entities among those available in spacy or
    - Type your own entities with GliNER!
---
#### Files
The app is made of two files: nlp_utils.py and app.py.
The first one contains an anonymization function, which takes into account the chosen anonymization engine and return an adapted output following the choices of the users regarding the entities to remove and the replacement method.
The second file, app.py, contains the actual user interface in which the interaction with the user and communication with the anonymization function is orchestrated.


---
#### Zoom-in on the engines
[Spacy](https://spacy.io/) is a famous and widely used NLP library by explosion. SiTA leverages its NER module based on the pre-trained ```en_core_web_sm``` model (which can be found [here](https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/)). 


[GliNER](https://github.com/urchade/GLiNER) is a deep learning transformer models based on an encoder architecture optimized to perform 0-shot entities recognition. It is particularly useful to spot entities which are not present in the spacy standard entity set. You can find the paper [here](https://arxiv.org/abs/2311.08526). The method used by GliNER is conceptually simple, it computes the similarity between the entity typed by the user and possible matches in the text.

---

#### Run the app

To run the app you can follow the simple steps shown below, consisting of:
    - Cloning the repo from github
    - Move into the newly created folder
    - Install the dependencies in the requirements.txt file
    - Run the streamlit command to run app.py
    - Open the browser

```
# optionally create a virtual env
conda create -n sita_env  # with conda or miniconda
python -m venv path/to/sita_env # with python venv module

# clone the repo
git clone https://github.com/aittam9/SiTa
cd SiTa

#install dependencies
pip install -r requirements.txt

#run the app in steamlit
streamlit run app.py
```

----------------------------------------------------
This is a proof of concept made by Mattia Proietti as a final project for the only purpose of completing the Harvard [cs50 2024](https://cs50.harvard.edu/x/2024/) [courework requirements](https://cs50.harvard.edu/x/2024/project/).
