import joblib 
import streamlit as st
import pandas as pd

# page configuration

st.set_page_config(page_title='Public Transport Delay',page_icon='🚌',layout='centered')

st.title(':rainbow[public transport delay prediction]')

#data loading 

try:
    model1 = joblib.load('linear_model.pkl')
    model2 = joblib.load('random_forest_model.pkl')

except Exception as e:
    st.error('error')
    st.write(e)
    st.stop()

st.sidebar.header('select the model')
model_select = st.sidebar.selectbox('select_your_model',['Liner Regression','Random Forest Regression'])



tab1,tab2,tab3,tab4,tab5 = st.tabs([

    'Welcome',
    'About Project',
    'Userinput',
    'Visualization',
    'About Developer'
])

# tab1 WELCOME PAGE
with tab1:
    st.image(r'C:\Users\indur\OneDrive\Desktop\power bi projects\Public_Transport_Delay\app\Gemini_Generated_Image_joezrjjoezrjjoez.png',caption='public transport delay prediction app')

# tab 2 about the project 

with tab2:
    st.subheader('About project')
    st.write(':rainbow[Public Transport Delay Prediction Using Machine Learning]')
    st.write('This project focuses on predicting public transport delays using machine learning. ' \
    'Public transport systems often experience delays due to factors such as traffic congestion, ' \
    'weather conditions, peak travel hours, and public events. The goal of this project is to analyze' \
    'these factors and build a predictive model that estimates the expected delay time of a transport trip.' \
    'The dataset includes information about city, route, weather conditions, traffic levels, events, and vehicle type.' \
    'Data cleaning was performed to handle messy values and missing data. Feature engineering technique' \
    's were applied to create meaningful variables such as rush hour and humidity–temperature ratio.' \
    ' A machine learning pipeline was built using preprocessing techniques and a Random Forest regression model. ' \
    'The model was trained and evaluated using metrics such as Mean Absolute Error (MAE) and R² score.' \
    ' The results help identify the main factors causing delays and improve prediction accuracy. ' \
    'This system can support better planning and decision-making for public transportation management.')

# tab 3 user user input 
with tab3:

    col1, col2 = st.columns(2)

    with col1:
        rainfall_mm = st.number_input('RAINFALL_MM', min_value=0.0)
        temperature = st.number_input('TEMPERATURE', min_value=-50.0)
        humidity = st.number_input('HUMIDITY', min_value=0.0)
        st.write(1:'Hyderabad',2:'Bangalore',3:'Chennai',4:'Mumbai',5:'Delhi')
        city = st.selectbox('CITY', [1,2,3,4,5])
        st.write('1':'Metro','2':'Bus',3:'Train')
        vehicle_type = st.selectbox('VEHICLE_TYPE',[1,2,3])


    with col2:
        wind_speed = st.number_input('WIND_SPEED', min_value=0.0)
        avg_delay_per_traffic_level = st.number_input('AVG_DELAY_PER_TRAFFIC_LEVEL', min_value=0.0)
        humidity_temp_ratio = st.number_input('HUMIDITY_TEMP_RATIO', min_value=0.0)
        st.write(0:'NO',,1:'YEs')
        is_weekend = st.selectbox('IS_WEEKEND',[0,1])



    predict = st.button("Predict")

    if predict:

        input_data = {

            "CITY":city,
            "ROUTE_ID":0,
            'HOUR':12,
            'DAY_OF_WEEK':2,
            'RAINFALL_MM':rainfall_mm,
            'TEMPERATURE':temperature,
            'HUMIDITY': humidity,
            'WIND_SPEED': wind_speed,
            'RUSH_HOUR':0,
            'TRAFFIC_LEVEL':0,
            'EVENT_TODAY':0,
            'EVENT_TYPE':0,
            'IS_WEEKEND':is_weekend,
            'VEHICLE_TYPE':vehicle_type,
            'AVG_DELAY_PER_CITY':city * 5,
            'AVG_DELAY_PER_TRAFFIC_LEVEL': avg_delay_per_traffic_level,
            'HUMIDITY_TEMP_RATIO': humidity_temp_ratio
        }

        feature_df = pd.DataFrame([input_data])
        feature_df = feature_df.astype(float)

        st.write('Input to model:',feature_df)

        if model_select == 'Liner Regression':
            liner_model = model1.predict(feature_df)
            st.write(':rainbow[liner Regression]')
            st.success(f'Transport Delay:{liner_model[0]}')
            st.balloons()
            st.image(r'C:\Users\indur\OneDrive\Desktop\power bi projects\Public_Transport_Delay\app\Gemini_Generated_Image_9i4rke9i4rke9i4r.png',width=200)
        

        elif model_select == 'Random Forest Regression':
            random_model = model2.predict(feature_df)
            st.write(':rainbow[Random Forest Regression]')
            st.success(f'Transport Delay:{random_model[0]}')
            st.balloons()
            st.image(r'C:\Users\indur\OneDrive\Desktop\power bi projects\Public_Transport_Delay\app\Gemini_Generated_Image_9i4rke9i4rke9i4r.png',width=200)
              
#tab4

with tab4:
    st.subheader('Visualization')
    col1,col2 = st.columns(2)


    df = pd.read_csv(r'C:\Users\indur\OneDrive\Desktop\power bi projects\Public_Transport_Delay\feature_engineering.csv')

    st.form("visualization")
    with col1:
        st.write('city for delay minutes(avg)')
        data = df.groupby('CITY')['DELAY_MINUTES'].mean()
        st.area_chart(data)

    with col2:
        st.write('relation ship b/w RAINFALL_MM vs DELAY_MINUTES')
        st.scatter_chart(x = 'DELAY_MINUTES',y='RAINFALL_MM',data=df)

with tab5:
    st.header(':rainbow[ABOUT DEVELOPER]')
    st.form("ABOUT DEVELOPER")
    col1,col2 = st.columns(2)
    with col1:
            st.markdown(
        ''' I am a B.Tech student in Computer Science at Chalapathi Institute of Engineering and Technology
        with a strong interest in Data Science and Machine Learning. 

        I have experience working with Python, MySQL, Power BI, and data analysis tools, and 
        I enjoy building end-to-end data projects. My focus is on data-driven problem solving,
          including machine learning model development, 
        data preprocessing, and building interactive dashboards.

        skills
        -python
        -pandas
        -numpy
        -matplotlib
        -seaborn
        -scikit-learn
        -machine learning
        -power bi
        -mysql
        -ETL
        -statistic
        -streamlit(deploy)
        -ANN and DNN
        
        ''')
    with col2:
        st.header(':rainbow[CONNECT ME]')
        st.write('NAME:INDURI AVINASH REDDY')

        st.write('phone-No:9346739650')
        st.write('Email:induriavinashreddy05@gmail.com')
        st.write('[Avinash_GitHub](https://github.com/avinashreddy0)')

        st.write('[Avinash_linkedin](https://www.linkedin.com/in/avinash-reddy-induri-4662b832a/)')
          
            


    








