from textblob import TextBlob
from textblob import download_corpora
import pandas as pd
import streamlit as st
import cleantext

st.header("SENTIMENTAL ANALYSIS")
with st.expander("Analyze Text"):
    text =st.text_input("Text here: ")
    if text:
        # blob = TextBlob(text)
        # st.write("Polarity: ",round(blob.sentiment.polarity,2))
        # st.write("Subjectivity: ",round(blob.sentiment.subjectivity,2))
        
        def score(text):
           
            blob1 = TextBlob(text)
            x = round(blob1.sentiment.polarity,2)
            st.write("Polarity: ",x)
            if x >= 0.5:
                return "Positive"
            elif x <= -0.5:
                 return "Negative"
            else:
                 return "Neutral"
        st.write(score(text))
        # def analyze(x):
        #     if x >= 0.5:
        #         return "Positive"
        #     elif x <= -0.5:
        #          return "Negative"
        #     else:
        #          return "Neutral"
        # st.write(analyze(x))
    
#     pre = st.text_input("Clean Text: ")
#     if pre:
#         st.write(cleantext.clean(pre, clean_all= False,extra_spaces = True,
#                                  stopwords =True, lowercase =True, numbers =True, punct = True))
# with st.expander("Analyze CSV"):
#         upl = st.file_uploader("Upload file")

        
            
#         if upl:
#             df = pd.read_csv(upl)
#             st.write(df.head())
            # df["Score"]=df["tweets"].apply(score)
            # df["analyze"] = df["score"].apply(analyze)
            # st.write(df.head())



