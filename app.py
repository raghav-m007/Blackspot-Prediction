import streamlit as st
import joblib
import numpy as np
from prediction import get_prediction, ordinal_encoder

model = joblib.load(r'Model/modelfinal.joblib')

st.set_page_config(page_title="Blackspot Accident Severity Prediction App", layout="wide")


st.markdown("<h1 style='text-align: center;'>Accident Severity Prediction App 🚧</h1>", unsafe_allow_html=True)

columns = '''Column 'NO OF FATALITIES' has 3 unique value(s): ['0' '1' '2']
Column 'GRIEVOUSLY INJURED' has 6 unique value(s): ['1' '0' '2' '3' '4' '6']
Column 'MINOR INJURED' has 3 unique value(s): ['0' '1' '2']
Column 'NO OF LANE' has 4 unique value(s): ['1' '2' '0' '4']
Column 'SURFACE CONDITION' has 2 unique value(s): ['0' '1']
Column 'PHYSICAL DRIVER' has 2 unique value(s): ['0' '1']
Column 'ROAD UNDER WORK CONSTRUCTION' has 2 unique value(s): ['0' '1']
Column 'LOAD CONDITION' has 3 unique value(s): ['2' '0' '1']'''

options_surface_condition = ['Paved', 'Un-Paved']
options_physical_driver = ['No', 'Yes']
options_road_under_work_construction = ['No', 'Yes']
options_load_condition = ['Not Loaded', 'Partially Loaded', 'Fully Loaded']


def main():
    with st.form('prediction_form'):
       st.subheader("Enter the input for following features:")
        
       fatalities = st.slider("No of Casualties: ", 0, 2, value=0, format="%d")
       greviously_injured = st.slider("No of Greviously Injured: ", 0, 6, value=0, format="%d")
       minor_injured = st.slider("No of Minor Injured: ", 0, 2, value=0, format="%d")
       no_of_lane = st.slider("No of Lane: ", 1, 4, value=1, format="%d")
       surface_condition = st.selectbox("Surface Condition: ", options=options_surface_condition)
      #  physical_driver = st.selectbox("Physical Driver: ", options=options_physical_driver)
       road_under_work_construction = st.selectbox("Road Under Work Construction: ", options=options_road_under_work_construction)
       load_condition = st.selectbox("Load Condition: ", options=options_load_condition)
       submit = st.form_submit_button("Predict")

    if submit:
           
       print(fatalities, greviously_injured, minor_injured, no_of_lane, surface_condition, road_under_work_construction, load_condition)

       surface_condition = ordinal_encoder(surface_condition, options_surface_condition)
      #  physical_driver = ordinal_encoder(physical_driver, options_physical_driver)
       road_under_work_construction = ordinal_encoder(road_under_work_construction, options_road_under_work_construction)
       load_condition = ordinal_encoder(load_condition, options_load_condition)
       
       data = np.array([fatalities, greviously_injured, minor_injured, no_of_lane, surface_condition, road_under_work_construction, load_condition])
       print(fatalities, greviously_injured, minor_injured, no_of_lane, surface_condition, road_under_work_construction, load_condition)
       pred = get_prediction(data=[data], model=model)
       st.write(f"The predicted severity is:  {pred[0]}")

if __name__ == '__main__':
    main()
