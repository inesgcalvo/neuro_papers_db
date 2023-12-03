# Web application with streamlit
# terminal : streamlit run server.py



from enum import auto
from turtle import position, width
import pandas as pd
import streamlit as st

import time
import altair as alt
import numpy as np
import pydeck as pdk
from urllib.error import URLError



# Background
background_image_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pxfuel.com%2Fen%2Fdesktop-wallpaper-acjmz&psig=AOvVaw1T3JZrS09YP9brusk4QOsn&ust=1701353637914000&source=images&cd=vfe&opi=89978449&ved=0CBEQjRxqFwoTCOjd06uy6YIDFQAAAAAdAAAAABAG'
background_image_src = '../images/background.jpg'

background_style = f'''
    <style>
        .stApp {{
            background-image: src("{background_image_src}");
            background-size: cover;
        }}
    </style>
'''
st.markdown(background_style, unsafe_allow_html = True)



# DataFrames
df_journals = pd.read_csv('../data/journals/journal_info.csv')
df_countries = pd.read_csv('../data/countries_db.csv')
df_articles = pd.read_csv('../data/articles_df.csv')
df_universities = pd.read_csv('../data/universities_db.csv', index_col=False)[['Rank_2024', 'Institution_Name', 'Location', 'Academic_Reputation']]



def intro():
    # sidebar
    np_log_white_path = '../images/logo_npdb_white.png'
    st.sidebar.image(np_log_white_path, width=100)
    # main
    logo, main_field = st.columns([1, 3])
    with logo:
        st.image(np_log_white_path)
    with main_field:
        st.write('###### The Neuroscience publications database')
        st.balloons()
        st.snow()
        st.toast('Mr Stay-Puft ')
        st.error('Error message')
        st.warning('Warning message')
        st.info('Info message')
        st.success('Success message')
        st.exception(e)



def universities():
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
    # Top Universities Rank
    # st.dataframe(df_universities.set_index(df_universities.columns[0]), width=700, height=105)
    # Link to tableau
    tableau_url = 'https://public.tableau.com/app/profile/in.s.g.calvo/viz/universities_17014263435230/Universities'
    st.markdown(f'[Interactive visualization in Tableau]({tableau_url})')



def countries():
    # sidebar
    OECD_logo = '../images/logo_OECD.png'
    OECD_iLib_logo = '../images/logo_oecdilibrary.png'
    st.sidebar.image(OECD_logo)
    st.sidebar.markdown("Organisation for Economic Co-operation and Development.")
    st.sidebar.image(OECD_iLib_logo)
    st.sidebar.markdown("OECD iLibrary is OECD’s Online Library for books, papers and statistics and the gateway to OECD's analysis and data.")               
    # main
    st.markdown(f"#### Countries")

    mln_cols = ['mln_2010', 'mln_2011', 'mln_2012', 'mln_2013', 'mln_2014', 'mln_2015', 'mln_2016', 'mln_2017', 'mln_2018', 'mln_2019', 'mln_2020', 'mln_2021', 'mln_2022']
    gdp_cols = ['gdp_2010', 'gdp_2011', 'gdp_2012', 'gdp_2013', 'gdp_2014', 'gdp_2015', 'gdp_2016', 'gdp_2017', 'gdp_2018', 'gdp_2019', 'gdp_2020', 'gdp_2021', 'gdp_2022']
    tot_cols = ['tot_2010', 'tot_2011', 'tot_2012', 'tot_2013', 'tot_2014', 'tot_2015', 'tot_2016', 'tot_2017', 'tot_2018', 'tot_2019', 'tot_2020', 'tot_2021']
    wom_cols = ['wom_2010', 'wom_2011', 'wom_2012', 'wom_2013', 'wom_2014', 'wom_2015', 'wom_2016', 'wom_2017', 'wom_2018', 'wom_2019', 'wom_2020', 'wom_2021']


    st.dataframe(df_countries,
                 column_config={'Alpha_3_code': 'Country',
                                # gdp_cols: st.column_config.LineChartColumn('I+D investment', y_min=0, y_max=5000)
                                },
                                hide_index=True)

    # filters
    A, B = st.columns(2)
    with A:
        cols = ['index', 'Country', 'Official_state_name', 'Sovereignty', 'Alpha_2_code', 'Alpha_3_code']
        columns = df_countries[cols].columns
        selection = st.multiselect('Filter columns', 
                                   columns, 
                                   default=['Official_state_name', 'Alpha_3_code'])
    with B:
        years = [i for i in range(2010, 2022)]
        year = st.multiselect('Filter by Year', years, default=[2020, 2021])
        mln_cols = ['mln_2010', 'mln_2011', 'mln_2012', 'mln_2013', 'mln_2014', 'mln_2015', 'mln_2016', 'mln_2017', 'mln_2018', 'mln_2019', 'mln_2020', 'mln_2021', 'mln_2022']
        gdp_cols = ['gdp_2010', 'gdp_2011', 'gdp_2012', 'gdp_2013', 'gdp_2014', 'gdp_2015', 'gdp_2016', 'gdp_2017', 'gdp_2018', 'gdp_2019', 'gdp_2020', 'gdp_2021', 'gdp_2022']
        tot_cols = ['tot_2010', 'tot_2011', 'tot_2012', 'tot_2013', 'tot_2014', 'tot_2015', 'tot_2016', 'tot_2017', 'tot_2018', 'tot_2019', 'tot_2020', 'tot_2021']
        wom_cols = ['wom_2010', 'wom_2011', 'wom_2012', 'wom_2013', 'wom_2014', 'wom_2015', 'wom_2016', 'wom_2017', 'wom_2018', 'wom_2019', 'wom_2020', 'wom_2021']
        sel_cols = []
        for i in year:
            mln_name = f'mln_{i}'
            gdp_name = f'gdp_{i}'
            tot_name = f'tot_{i}'
            wom_name = f'wom_{i}'
            sel_cols.append(mln_name)
            sel_cols.append(gdp_name)
            sel_cols.append(tot_name)
            sel_cols.append(wom_name)
    # show dataframe
    selected_columns = selection + sel_cols
    st.dataframe(df_countries[selected_columns], width=700, height=200)


def journals():
    # sidebar
    SJR_logo = '../images/SJR.png'
    st.sidebar.image(SJR_logo, width=250)
    st.sidebar.markdown('The SCImago Journal Rank (SJR) indicator is a measure of the prestige of scholarly journals that accounts for both the number of citations received by a journal and the prestige of the journals where the citations come from.')
    # main
    st.markdown('#### Journals')
    selected_journal = st.selectbox("Select a Journal:", df_journals['journal_name'].unique())
    selected_row = df_journals[df_journals['journal_name'] == selected_journal].iloc[0]
    st.markdown(f"**Journal:** {selected_journal}")
    st.success(f"**Number of Articles:** {selected_row['num_articles']}")



def articles():
    # sidebar
    pubmed_logo = '../images/pubmed.svg'
    st.sidebar.image(pubmed_logo, width=250)
    st.sidebar.markdown('PubMed is a free search engine accessing primarily the MEDLINE database of references and abstracts on life sciences and biomedical topics.')
    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    # main
    st.markdown('#### Articles')
    st.dataframe(df_articles[['Title', 'PMID']])



def mapping_demo():
    st.markdown('#### Map')

    @st.cache_data
    def from_data_file(filename):
        url = (
            "http://raw.githubusercontent.com/streamlit/"
            "example-data/master/hello/v1/%s" % filename
        )
        return pd.read_json(url)

    try:
        ALL_LAYERS = {
            "Bike Rentals": pdk.Layer(
                "HexagonLayer",
                data=from_data_file("bike_rental_stats.json"),
                get_position=["lon", "lat"],
                radius=200,
                elevation_scale=4,
                elevation_range=[0, 1000],
                extruded=True,
            ),
            "Bart Stop Exits": pdk.Layer(
                "ScatterplotLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_color=[200, 30, 0, 160],
                get_radius="[exits]",
                radius_scale=0.05,
            ),
            "Bart Stop Names": pdk.Layer(
                "TextLayer",
                data=from_data_file("bart_stop_stats.json"),
                get_position=["lon", "lat"],
                get_text="name",
                get_color=[0, 0, 0, 200],
                get_size=15,
                get_alignment_baseline="'bottom'",
            ),
            "Outbound Flow": pdk.Layer(
                "ArcLayer",
                data=from_data_file("bart_path_stats.json"),
                get_source_position=["lon", "lat"],
                get_target_position=["lon2", "lat2"],
                get_source_color=[200, 30, 0, 160],
                get_target_color=[200, 30, 0, 160],
                auto_highlight=True,
                width_scale=0.0001,
                get_width="outbound",
                width_min_pixels=3,
                width_max_pixels=30,
            ),
        }
        st.sidebar.markdown("### Map Layers")
        selected_layers = [
            layer
            for layer_name, layer in ALL_LAYERS.items()
            if st.sidebar.checkbox(layer_name, True)
        ]
        if selected_layers:
            st.pydeck_chart(
                pdk.Deck(
                    map_style="mapbox://styles/mapbox/light-v9",
                    initial_view_state={
                        "latitude": 37.76,
                        "longitude": -122.4,
                        "zoom": 11,
                        "pitch": 50,
                    },
                    layers=selected_layers,
                )
            )
        else:
            st.error("Please choose at least one layer above.")
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**
            Connection error: %s
        """
            % e.reason
        )



def plotting_demo():
    st.markdown('#### Plot')

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()

    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()
    st.button("Re-run")



def data_frame_demo():
    st.markdown('#### df')

    @st.cache_data
    def get_UN_data():
        AWS_BUCKET_URL = "http://streamlit-demo-data.s3-us-west-2.amazonaws.com"
        df = pd.read_csv(AWS_BUCKET_URL + "/agri.csv.gz")
        return df.set_index("Region")

    try:
        df = get_UN_data()
        countries = st.multiselect(
            "Choose countries", list(df.index), ["China", "United States of America"]
        )
        if not countries:
            st.error("Please select at least one country.")
        else:
            data = df.loc[countries]
            data /= 1000000.0
            st.write("### Gross Agricultural Production ($B)", data.sort_index())

            data = data.T.reset_index()
            data = pd.melt(data, id_vars=["index"]).rename(
                columns={"index": "year", "value": "Gross Agricultural Product ($B)"}
            )
            chart = (
                alt.Chart(data)
                .mark_area(opacity=0.3)
                .encode(
                    x="year:T",
                    y=alt.Y("Gross Agricultural Product ($B):Q", stack=None),
                    color="Region:N",
                )
            )
            st.altair_chart(chart, use_container_width=True)
    except URLError as e:
        st.error(
            """
            **This demo requires internet access.**

            Connection error: %s
        """
            % e.reason
        )



page_names_to_funcs = {
    'Home': intro,
    'Universities': universities,
    'Countries': countries,
    'Journals': journals,
    'Articles': articles,    
    "Plotting Demo": plotting_demo,
    "Mapping Demo": mapping_demo,
    "DataFrame Demo": data_frame_demo
}



pages = st.sidebar.selectbox('', page_names_to_funcs.keys())
page_names_to_funcs[pages]()