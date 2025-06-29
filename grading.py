from functools import total_ordering

import streamlit as st
st.title('Grading System')

marks = st.number_input('Enter Obtain marks:',min_value=1)
total = st.number_input('Enter total marks:',min_value=1)
p = marks/total * 100
st.subheader(f'Your Percentage: :blue[{p} %]')
if p >= 80:
    st.success('Excelent')
elif p >= 60 and  p < 80:
    st.info('pass')
else:
    st.error('Fail')
