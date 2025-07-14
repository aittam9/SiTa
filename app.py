import streamlit as st
from spacy import displacy
from io import StringIO
import spacy

#from streamlit_annotation_tools import text_labeler
from nlp_utils import anonymize, SPACY_SUPPORTED_ENTITIES, convert_pdf
st.set_page_config(layout='wide')
# #"""
# Simple  streamlit web app to anonymize text. Text can be typed, copy-pasted or uploaded in txt or pdf formats.
# There is an entity viewer showing the entities found by the choosen engine and a text previewer in which anonymization are shown.

# Is possible to switch between two engine:
    
#     spacy pipeline (en_core_web_sm): It is the default. The only entity anonymized on a default basis is PERSON. The sidebar allows
#     for the expansion of the possible entities. The selection can be made among the pool of the entities supported by the pipeline.
    
#     GLiNER: Transformer model based on encoder. This allow for 0-shot recognition of entities. Desired Entities can be typed in the
#     sidebar when the GliNER option is chosen in the radio. Default works for Person

#     """
#store spacy supported entities
supp_ents = SPACY_SUPPORTED_ENTITIES
ENTS2REMOVE = []


#sidebar with some options
with st.sidebar:
    #TODO try to call gliner just one time! It seems that the model is being called every time
    "Options"
    #Allow customization of the model used for the entity tagging
    ANNOTATION_ENGINE = st.radio("Choose annotation engine" , ["Spacy NER (default)", "GLiNer"])
    if ANNOTATION_ENGINE == "GLiNer":
        custom_labels = st.text_input("Choose custom labels for Gliner") # type custom entities for gliner
        #ensure that if no custom label is provide "Person" is used as default
        if custom_labels:  
            ENTS2REMOVE = custom_labels.split()
        else:
            ENTS2REMOVE = ["Person"]
        #load a blank spacy pipeline and add gliner as the NER engine    
        nlp = spacy.blank("en")
        nlp.add_pipe("gliner_spacy", config = {"labels": ENTS2REMOVE})         
    else:
        nlp = spacy.load("en_core_web_sm")
        ENTS2REMOVE = ["PERSON"]
        #if st.button("Customize labels"):
        
        multi_sele = st.multiselect("Select entities (optional, default PERSON)", options = supp_ents) #expand the set of entities to replace, default is person
        if multi_sele:
            ENTS2REMOVE.extend(multi_sele)
            
    # TODO  
    # Allow customization of the replacement methods for the entities found
    st.divider()
    if st.radio("Choose replacement method", ["Entity label", "Omissis" ]) == "Omissis": #"Pseudo anonimization (only for person)"
        rep_method = 1
    else:
        rep_method = 0


st.title("Simple Text Anonimizer")
st.html(
    """<p>Hello this is SiTA, a simple text anonymizer that leverage NLP tools to spot and cover textual information that you wish to hide in your documents.
      You can write or copy-paste some text you wish to anonymize inside the box below.
        Alternatively you can upload a file from your local folders.</p>"""
)
st.divider()

# Type some text to be manipulated or upload a file
tab1, tab2 = st.tabs(["Copy-Paste", "Upload File"])
with tab1:
    text = st.text_area("Write or copy-paste some text")

# upload a file
with tab2:
    uploaded_file = st.file_uploader("Upload file from folder", type = [".txt", ".pdf"])
    # check if file is txt otherwise send erro
    if uploaded_file:
        if uploaded_file.name.endswith(".pdf"):
            text = convert_pdf(uploaded_file.name)
        
        elif uploaded_file.name.endswith(".txt"):
            stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
            text = stringio.read()
    

#analyze the text with spacy and get html representation of entities
text =  nlp(text)

#display found entities
ents_html = displacy.render(text, style="ent", jupyter=False)
with st.expander("Entities Preview"):
    if text:
        st.markdown(ents_html, unsafe_allow_html=True)
    else:
        st.write("No input Text provided. Please type or paste some text.")

    
#anonymization step
if st.button("Anonymize"):
    #do some operation on the text
    if text:
        st.divider()
        st.subheader("Text preview")

        anonymized_text = anonymize(text, labels = ENTS2REMOVE, rep_method = rep_method)
        with st.container(border= True, ):
        
        #render the modified text
            st.html(f"<p>{anonymized_text}</p>")
        
        #select a format for il download
        st.divider()
        # select format for download (ideally txt or json?)
        with st.expander("Download the results"):
            st.selectbox(label = "Select a format", options = ["TXT", "JSON"])
    else:
        "Warning: Please type some valid text or upload a supported file"
    
    
    #TODO
    #format the file for the download
    st.download_button("Download", anonymized_text, "anonymized.txt")

#TODO possible addition of component
#1. Integration of annotation component to supplement the annotation missed by the model


# st.divider()
# from streamlit_annotation_tools import text_highlighter

# annotations = text_highlighter(anonymized_text)


st.divider()
st.html("<div>This APP has been made by Mattia Proietti as the final project of CS50 course</div>")


