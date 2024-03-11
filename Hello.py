import streamlit as st
import pandas as pd
st.set_page_config(layout="wide")

# 데이터 로드
@st.cache_data 
def load_data(filepath):
    data = pd.read_csv(filepath)
    return data
data = load_data('AchievementStandards.csv')

col_a, col_b, col_c = st.columns([33,33,33])

# 교육과정 선택
education_system_options = ['전체'] + list(data['교육과정'].unique())
education_system = col_a.selectbox('교육과정을 선택하세요.', education_system_options)

if education_system == '전체':
    filtered_by_education = data
else:
    filtered_by_education = data[data['교육과정'] == education_system]

# 학년(군) 선택
grade_group_options = ['전체'] + list(filtered_by_education['학년(군)'].unique())
grade_group = col_b.selectbox('학년(군)을 선택하세요.', grade_group_options)

if grade_group == '전체':
    filtered_by_grade = filtered_by_education
else:
    filtered_by_grade = filtered_by_education[filtered_by_education['학년(군)'] == grade_group]

# 과목 선택
subject_options = ['전체'] + list(filtered_by_grade['과목'].unique())
subject = col_c.selectbox('과목을 선택하세요.', subject_options)

if subject == '전체':
    final_filtered = filtered_by_grade
else:
    final_filtered = filtered_by_grade[filtered_by_grade['과목'] == subject]

# 키워드 검색
keyword = st.text_input('성취기준명에서 검색할 키워드를 입력하세요.', '')

# 실행 버튼
if st.button('검색 실행'):
    if keyword:  # 키워드가 입력된 경우에만 필터링
        filtered_by_keyword = final_filtered[final_filtered['성취기준명'].str.contains(keyword, case=False, na=False)]
    else:  # 키워드 입력 없이 버튼을 누른 경우 모든 필터링된 결과를 보여줌
        filtered_by_keyword = final_filtered
    
        st.dataframe(filtered_by_keyword[['교과', '과목', '영역(단원)', '성취기준\n코드', '성취기준명']], width=1600, height=600)

else:
    st.write('검색 결과가 여기에 표시됩니다.')
