#!/usr/bin/env python
import streamlit as st
from great_tables import GT
import pandas as pd
from pprint import pprint
from datetime import datetime

st.write("# Brain Image Library Inventory Status")

@st.cache_data
def get_data():
    st.write('Downloading data from Brain Image Library')
    f = 'https://download.brainimagelibrary.org/inventory/daily/reports/today.json'
    df = pd.read_json(f)
    df = df.drop(columns=['bildirectory', 'consortium', 'bildate', 'genotype', 'md5_coverage', 'sha256_coverage', 'xxh64_coverage', 'taxonomy', 'size', 'samplelocalid', 'json_file', 'temp_file', 'creation_date', 'exists', 'dataset_uuid'])
    df = df.sort_values(by=['number_of_files'])
    df.rename(columns = {'metadata_version':"Version",
        'bildid':"ID",
        'contributor':"Contributor",
        'award_number':"Award Number",
        'affiliation':"Affiliation",
        'project':"Project",
        'generalmodality':'Modality',
        'technique':'Technique',
        'species':'Species',
        'pretty_size':'Size',
        'number_of_files':'Number of Files',
        'score':'Coverage'}, inplace=True)

    return df

df = get_data()
st.data_editor(
    df,
    column_config={
        "Coverage": st.column_config.ProgressColumn(
            "Coverage",
            min_value=0,
            max_value=1,
        ),
    },
    hide_index=True,
)
