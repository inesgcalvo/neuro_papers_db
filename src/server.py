# Web application with streamlit

''' TERMINAL
cd .\_clase\_FINAL_PROJECT_\neuro_papers_db\src\
conda activate clase
streamlit run server.py
'''

import time
import numpy as np
import pandas as pd
import pylab as plt
import streamlit as st

from support_server import *

import joblib
from support_model import predict_journal


# DataFrame
df_articles = pd.read_csv('../data/neuropapers_db/publications.csv')

# 'pub_id', 'journal_id', 'last_revision', 'volume', 'title', 'pages', 
# 'DOI', 'authors', 'journal', 'abstract', 'abstract_words', 
# 'keywords', 'terms', 'pub_type', 'citation', 'publication_year', 'pub_date'



def intro():
    # sidebar
    np_log_white = '../images/logo_npdb_white.png'
    np_loguin = '../images/loguin.png'
    st.sidebar.image(np_loguin)
    # main
    logo, main_field = st.columns([1, 4])
    with logo:
        st.image(np_log_white)
    with main_field:
        st.markdown('## neuropapers db')
        st.markdown('##### Neurosciences publications database')
        information = '''61945 **publications**  
                         249 **countries**  
                         110 **journals**  
                         228898 **researchers**  
                         133194 **affiliations**'''     
        st.markdown(information)
    # st.divider() 




def universities():
    # DataFrame
    df_universities = pd.read_csv('../data/universities/universities_db.csv', index_col=False)[['Rank_2024', 'Institution_Name', 'Location', 'Academic_Reputation']]
    # sidebar
    QS_logo = '../images/QS_logo.svg'
    st.sidebar.image(QS_logo)
    st.sidebar.markdown('The 20th edition of the QS World University Rankings features 1,500 institutions across 104 locations and is the only ranking of its kind to emphasise employability and sustainability.')
    # main
    st.markdown('#### Top Universities\n QS World University Rankings 2024: Top global universities')
    # folium map
    uni_map_path = '../html/universities_map.html'
    with open(uni_map_path, 'r', encoding='utf-8') as file:
        uni_map = file.read().strip()
    st.components.v1.html(uni_map, width=700, height=400, scrolling=False)
    # Link to tableau
    tableau_url = 'https://public.tableau.com/app/profile/in.s.g.calvo/viz/universities_17014263435230/Universities'
    st.markdown(f'[Interactive visualization in Tableau]({tableau_url})')
    st.divider()  
    # Top Universities Rank
    st.dataframe(df_universities.set_index(df_universities.columns[0]), width=700, height=315)





def countries():
    # DataFrame
    df_countries = pd.read_csv('../data/neuropapers_db/countries.csv')

    # sidebar
    OECD_logo = '../images/logo_OECD.png'
    OECD_iLib_logo = '../images/logo_oecdilibrary.png'
    st.sidebar.image(OECD_logo)
    st.sidebar.markdown("Organisation for Economic Co-operation and Development.")
    st.sidebar.image(OECD_iLib_logo)
    st.sidebar.markdown("OECD iLibrary is OECD’s Online Library for books, papers and statistics and the gateway to OECD's analysis and data.")   

    # main
    st.markdown('#### Countries Research and development (R&D)')

    mln_cols = ['mln_2010', 'mln_2011', 'mln_2012', 'mln_2013', 'mln_2014', 'mln_2015', 'mln_2016', 'mln_2017', 'mln_2018', 'mln_2019', 'mln_2020', 'mln_2021']
    gdp_cols = ['gdp_2010', 'gdp_2011', 'gdp_2012', 'gdp_2013', 'gdp_2014', 'gdp_2015', 'gdp_2016', 'gdp_2017', 'gdp_2018', 'gdp_2019', 'gdp_2020', 'gdp_2021']
    tot_cols = ['tot_2010', 'tot_2011', 'tot_2012', 'tot_2013', 'tot_2014', 'tot_2015', 'tot_2016', 'tot_2017', 'tot_2018', 'tot_2019', 'tot_2020', 'tot_2021']
    wom_cols = ['wom_2010', 'wom_2011', 'wom_2012', 'wom_2013', 'wom_2014', 'wom_2015', 'wom_2016', 'wom_2017', 'wom_2018', 'wom_2019', 'wom_2020', 'wom_2021']

    df_countries['mln'] = df_countries.apply(lambda row: row[mln_cols].tolist(), axis=1)
    df_countries['gdp'] = df_countries.apply(lambda row: row[gdp_cols].tolist(), axis=1)
    df_countries['tot'] = df_countries.apply(lambda row: row[tot_cols].tolist(), axis=1)
    df_countries['wom'] = df_countries.apply(lambda row: row[wom_cols].tolist(), axis=1)

    df = pd.DataFrame({'Country': df_countries['official_state_name'],
                       'Gross domestic spending (%)': df_countries['gdp'],
                       'Million US dollars': df_countries['mln'],
                       'Total Researchers': df_countries['tot'],
                       'Women Researchers': df_countries['wom']})

    # filters
    selection = st.multiselect('Select the index', 
                                ['Gross domestic spending (%)', 'Million US dollars', 'Total Researchers', 'Women Researchers'], 
                                default=['Gross domestic spending (%)', 'Million US dollars'])

    selected_columns = ['Country']
    selected_columns += selection    
    st.dataframe(df[selected_columns],
                 column_config={'Country': 'Country',
                                'Gross domestic spending (%)': st.column_config.LineChartColumn("GDS: [2010 - 2021]", y_min=0),
                                'Million US dollars': st.column_config.LineChartColumn("MLN: [2010 - 2021]", y_min=0),
                                'Total Researchers': st.column_config.LineChartColumn("TOT: [2010 - 2021]", y_min=0),
                                'Women Researchers': st.column_config.LineChartColumn("WOM: [2010 - 2021]", y_min=0),})
    


def journals():
    # sidebar
    SJR_logo = '../images/SJR.png'
    st.sidebar.image(SJR_logo, width=250)
    st.sidebar.markdown('The SCImago Journal Rank (SJR) indicator is a measure of the prestige of scholarly journals that accounts for both the number of citations received by a journal and the prestige of the journals where the citations come from.')
    # main
    st.markdown('#### Journals')
    selected_journal = st.selectbox("Select a Journal:", df_articles['journal'].unique())

    A, B = st.columns([1, 5])
    column = 'title'
    with A:
        if st.button("Title"):
            column = 'title'
        if st.button('Abstract'):
            column = 'abstract'
    with B:
        st.pyplot(cloud_for_column(df_articles, column, selected_journal))



def publications():
    # sidebar
    pubmed_logo = '../images/pubmed.svg'
    st.sidebar.image(pubmed_logo, width=250)
    st.sidebar.markdown('PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics.')
    # main
    st.markdown('#### Publications')
    html_powerbi = '<iframe title="neuropapers_db" width="700" height="300" src="https://app.powerbi.com/reportEmbed?reportId=2bc58e54-5ce2-458e-8160-13bb75ca498d&autoAuth=true&ctid=4380e7a1-c525-44fc-b9e4-a02e0dda4d80" frameborder="0" allowFullScreen="true"></iframe>'
    # html_powerbi = '<iframe title="neuropapers_db" width="1140" height="541.25" src="https://app.powerbi.com/reportEmbed?reportId=2bc58e54-5ce2-458e-8160-13bb75ca498d&autoAuth=true&ctid=4380e7a1-c525-44fc-b9e4-a02e0dda4d80" frameborder="0" allowFullScreen="true"></iframe>'
    st.markdown(html_powerbi, unsafe_allow_html=True)
    st.divider() 
    powerbi_url = 'https://app.powerbi.com/groups/me/reports/2bc58e54-5ce2-458e-8160-13bb75ca498d/ReportSection4a4973d3a6499760c280?experience=power-bi'
    st.markdown(f'[Interactive visualization in PowerBI]({powerbi_url})')

    

def model():
    # Load the trained Decision Tree model and Label Encoder
    # dtc_model = joblib.load('your_model_filename.pkl')
    # label_encoder = joblib.load('your_label_encoder_filename.pkl')

    # main
    st.markdown('#### Journal Prediction App')

    # User Input
    title_input = st.text_input("Enter Title:")
    abstract_input = st.text_input("Enter Abstract:")

    # Make Predictions on Button Click
    if st.button("Predict"):
        if title_input and abstract_input:
            predictions = predict_journal(title_input, abstract_input, dtc_model, label_encoder)
            st.write("Predictions:")
            for entry in predictions:
                st.write(f"Journal: {entry['journal']}, Probability: {entry['probability']}")
        else:
            st.warning("Please enter both Title and Abstract for prediction.")



page_names_to_funcs = {'Home': intro,
                       'Top Universities': universities,
                       'Countries R+D': countries,
                       'Journals': journals,
                       'Publications': publications,
                       'Journal Prediction App': model}
    


pages = st.sidebar.selectbox('', page_names_to_funcs.keys())
page_names_to_funcs[pages]()