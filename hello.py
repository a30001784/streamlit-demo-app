import streamlit as st
import pandas as pd
import numpy as np
from st_files_connection import FilesConnection

st.write("Hello World")
st.write("## This is a H2 Title!")
x = st.text_input("Movie", "Star Wars")

if st.button("Click Me"):
    st.write(f"Your favorite movie is `{x}`")


data = pd.read_csv("movies.csv")
st.write(data)


chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.bar_chart(chart_data)


# Create connection object and retrieve file contents.
# Specify input format is a csv and to cache the result for 600 seconds.
conn = st.connection('s3', type=FilesConnection)
df = conn.read("predawnsuper-serve-s3-bucket-dev/aggregated_stock_performance_tracker/it/RDDT/aggregated_RDDT.csv", input_format="csv", ttl=600)

# Print results.
# for row in df.itertuples():
#     st.write(f"{row.Price}, {row.Volume}:")
st.write(df[['Date', 'Price', 'Volume','P/B']])