from functools import total_ordering

import streamlit as st
st.title('Grading System')
marks =st.number_input('Enter Obtain Marks:')
marks = st.number_input('Enter total marks:')
total_ordering()
p = marks/total * 100
st.subheader(f'Your Percentage: :blue[{p} %]')
if p>=80:
    st.success('Excelent')
elif p>= 60 and p<80:
    st.info('Pass')
else:
    st.error('Fail')
