#!/usr/bin/env python
import streamlit as st
from great_tables import GT
import pandas as pd
from pprint import pprint
from datetime import datetime

@st.cache_data
def get_data():
    f = 'https://download.brainimagelibrary.org/inventory/daily/reports/today.json'
    df = pd.read_json(f)
    df = df.drop(columns=['bildirectory', 'bildate', 'genotype', 'md5_coverage', 'sha256_coverage', 'xxh64_coverage', 'taxonomy', 'size', 'samplelocalid', 'json_file', 'temp_file', 'creation_date', 'exists', 'dataset_uuid'])
    return df

df = get_data()

# Create a display table
(
    GT(df)
    .tab_header(title="Brain Image Library", subtitle=f"Inventory status on {datetime.today().strftime('%Y-%m-%d')}")
    .tab_spanner(
        label="Dataset Information",
        columns=["metadata_version", "bildid", 'contributor', 'award_number', 'affiliation', 'project', "consortium", 'pretty_size', 'number_of_files']
    )
    .tab_spanner(
        label="Dataset Metadata",
        columns=["generalmodality", "technique", "species", 'taxonomy']
    )
    .fmt_percent("score", decimals=2)
    .cols_label(
        metadata_version="Version",
        bildid="ID",
        contributor="Contributor",
        award_number="Award Number",
        affiliation="Affiliation",
        project="Project",
        consortium="Consortium",
        generalmodality='Modality',
        technique='Technique',
        species='Species',
        pretty_size='Size',
        number_of_files='Number of Files',
        score='Coverage'
    )
    .tab_source_note(source_note="The Brain Image Library is supported by the National Institutes of Mental Health of the National Institutes of Health under award number R24-MH-114793. The content is solely the responsibility of the authors and does not necessarily represent the official views of the National Institutes of Health.")
)



