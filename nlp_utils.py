import spacy 

import re 
from typing import List
import pymupdf as fitz

import warnings
warnings.filterwarnings("ignore")

#supported entities by the en_core_web_sm spacy pipeline
SPACY_SUPPORTED_ENTITIES = ["CARDINAL", "DATE", "EVENT", "FAC", "GPE", "LANGUAGE", "LAW", "LOC", "MONEY", "NORP", "ORDINAL", "ORG",
                             "PERCENT", "PERSON", "PRODUCT", "QUANTITY", "TIME", "WORK_OF_ART","LOC", "MISC", "ORG", "PER"]

ENTS2REMOVE = ["PERSON"]

#take a spacy doc as input
def anonymize(text, labels = ENTS2REMOVE, rep_method = 0):
    """ Replace the substrings to anonimize with the label they are associated with.
    Args: 
        text: spacy doc with ner annotations
        labels: list of entities to replace
    """
    new_text = " ".join([t.text for t in text])
    for ent in text.ents:
        if ent.label_ in labels:
            if rep_method == 0:
                new_text = re.sub(ent.text, ent.label_, new_text)
            elif rep_method == 1:
                new_text = re.sub(ent.text, "OMISSIS", new_text)

    return re.sub(r'\s([?.!",:;-](?:\s|$))', r'\1', new_text)


def convert_pdf(file):
    """
    Convert a pdf file into a txt, stripping consecutively line breaks
    Args:
        file: file name or path of the pdf to convert
    """
    document = fitz.open(file)
    text = ""
    for page in document:
        text += page.get_text()
    return re.sub(r"\n", " ", text)



if __name__ == "__main__":
    # nlp = spacy.blank("en")
    # ENTS2REMOVE = input("labels= ")
    # nlp.add_pipe("gliner_spacy", config = {"labels": ENTS2REMOVE.split()})
    # text  = nlp(input("Text: "))
    # res = anonymize(text, labels= ENTS2REMOVE)
    # print(res)

    # path = "./prova.pdf"

    # text = convert_pdf(path)
    # print(text)
    
    nlp = spacy.load("en_core_web_sm")
    text = "My name is Donald Trump and I come from the US."
    doc = nlp(text)
    

    


   

        

