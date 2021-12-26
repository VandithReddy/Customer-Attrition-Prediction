import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
my_dataset="WA_Fn-UseC_-Telco-Customer-Churn.csv"
def explore_data(dataset):
    df=pd.read_csv(dataset)
    return df
data=explore_data(my_dataset)
features=19
st.set_page_config(initial_sidebar_state="collapsed")
html_temp = """
    <div style="background-color:grey;padding:10px">
    <h2 style="color:white;text-align:center;">Customer Attrition Prediction</h2>
    </div>"""
st.markdown(html_temp,unsafe_allow_html=True)

# background
st.markdown(
    """
    <style>
    .reportview-container {
        background: url("https://th.bing.com/th/id/R.856f31d9f475501c7552c97dbe727319?rik=Eq9oehb4QunXVw&riu=http%3a%2f%2fwww.baltana.com%2ffiles%2fwallpapers-5%2fWhite-Background-High-Definition-Wallpaper-16573.jpg&ehk=I38kgsJb2jc3ycTK304df0ig%2flhB3PaaXRrqcPVwDgA%3d&risl=&pid=ImgRaw&r=0")
 }
    </style>
    """,
    unsafe_allow_html=True
)

def main():
    activities=["EDA","Visualize Data","Prediction","Model statistics","About"]
    choice=st.sidebar.selectbox("",activities)
    if choice=="EDA":
        EDA()
    if choice=="Visualize Data":
        DataVisualization()
    if choice=="Prediction":
        prediction()
    if choice=="Model statistics":
        statistics()
    if choice=="About":
        about()
def EDA():
    st.header("Exploratory Data Analysis")
    method_names=["Show dataset","Head","Tail","Shape","Describe","Missing value","Columns Names"]
    method_operation=[data,data.head(),data.tail(),data.shape,data.describe(),data.isnull().sum(),data.columns]

    for i in range(len(method_names)):
        if st.checkbox(method_names[i]):
            st.write(method_operation[i])
    all_columns=list(data.columns)
    if st.checkbox("Select columns to show"):
        selected_columns=st.multiselect("Select column",all_columns)
        new_df=data[selected_columns]
        st.dataframe(new_df)

def DataVisualization():
    st.header("Data Visualization")
    if st.checkbox("Numerical variable"):
        column_name=st.selectbox("",("Select column","MonthlyCharges","SeniorCitizen","TotalCharges","Age"))
        if column_name=="MonthlyCharges":
            plt.figure(figsize=(5,3))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
            st.write(sns.distplot(data[column_name]))
            st.pyplot()
        elif column_name=="SeniorCitizen":
            plt.figure(figsize=(5,3))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
            st.write(sns.distplot(data[column_name]))
            st.pyplot()
        elif column_name=="TotalCharges":
            plt.figure(figsize=(5,3))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
            st.write(sns.distplot(data[column_name]))
            st.pyplot()
    if st.checkbox("Categorical variable"):
        column_name=st.selectbox("",("Select column","Contract","PhoneService","tenure","InternetService"))
        if column_name=="Contract":
            plt.figure(figsize=(5,3))
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
        elif column_name=="PhoneService":
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
        elif column_name=="tenure":
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
        elif column_name=="InternetService":
            st.set_option('deprecation.showPyplotGlobalUse', False)
            st.write(plt.hist(data[column_name],color="skyblue",edgecolor="black"))
            st.pyplot()
def prediction():
    st.header("Prediction")
    col_list=[0]*features

    gen_col=["Female","Male"]
    gen_num=list(range(len(gen_col)))
    gen=st.radio("Select gender",gen_num,format_func=lambda x:gen_col[x])
    col_list[0]=gen  

    age_col=[0,1]
    age_num=list(range(len(age_col)))
    age=st.radio("Senior Citizen?",age_num,format_func=lambda x:age_col[x])
    col_list[1]=age_col

    partner_col=["Yes","No"]
    partner_num=list(range(len(partner_col)))
    partner=st.radio("Partner?",partner_num,format_func=lambda x:partner_col[x])
    col_list[2]=partner

    dpdt_col=["Yes","No"]
    dpdt_num=list(range(len(dpdt_col)))
    dpdt=st.radio("Dependant?",dpdt_num,format_func=lambda x:dpdt_col[x])
    col_list[3]=dpdt

    Tenure_col=st.slider("Enter tenure : ",0,72)
    col_list[4]=Tenure_col

    ps_col=["Yes","No"]
    ps_num=list(range(len(ps_col)))
    ps=st.radio("Phone Service?",ps_num,format_func=lambda x:ps_col[x])
    col_list[5]=ps

    ml_col=["Yes","No"]
    ml_num=list(range(len(ml_col)))
    ml=st.radio("Multiple Lines?",ml_num,format_func=lambda x:ml_col[x])
    col_list[6]=ml

    InternetService=["InternetService","Fiber Optic","DSL","No internet service"]
    InternetS_option=st.selectbox("",InternetService)
    if InternetS_option=="Fiber Optic":
        col_list[7]="Fiber Optic"
        # col_list[10]=0
    elif InternetS_option=="DSL":
        col_list[7]="DSL"
        # col_list[10]=1
    elif InternetS_option=="No internet service":
        col_list[7]="No internet service"
        # col_list[10]=0
    
    os_col=["Yes","No"]
    os_num=list(range(len(os_col)))
    os=st.radio("Online Security?",os_num,format_func=lambda x:os_col[x])
    col_list[8]=os

    ob_col=["Yes","No"]
    ob_num=list(range(len(ob_col)))
    ob=st.radio("Online Backup?",ob_num,format_func=lambda x:ob_col[x])
    col_list[9]=ob

    dp_col=["Yes","No"]
    dp_num=list(range(len(dp_col)))
    dp=st.radio("Device Protection?",dp_num,format_func=lambda x:dp_col[x])
    col_list[10]=dp

    ts_col=["Yes","No"]
    ts_num=list(range(len(ts_col)))
    ts=st.radio("Tech Support?",ts_num,format_func=lambda x:ts_col[x])
    col_list[11]=ts

    stv_col=["Yes","No"]
    stv_num=list(range(len(stv_col)))
    stv=st.radio("Streaming TV?",stv_num,format_func=lambda x:stv_col[x])
    col_list[12]=stv

    sm_col=["Yes","No"]
    sm_num=list(range(len(sm_col)))
    sm=st.radio("Streaming Movie?",sm_num,format_func=lambda x:sm_col[x])
    col_list[13]=sm

    Contract=["Contract","One year","month-to-month"]
    Contract_option=st.selectbox("",Contract)
    if Contract_option=="One year":
        col_list[14]="One year"
    elif InternetS_option=="month-to-month":
        col_list[14]="month-to-month"

    pbl_col=["Yes","No"]
    pbl_num=list(range(len(pbl_col)))
    pbl=st.radio("Paper Billing?",pbl_num,format_func=lambda x:sm_col[x])
    col_list[15]=pbl

    paymentmethod=["Payment Method","Electronic check","Mail check","Credit card (automatic)","Bank transfer (automatic)"]
    pm_option=st.selectbox("",paymentmethod)
    if pm_option=="Electronic check":
        col_list[16]="Electronic check"
    elif pm_option=="Mail check":
        col_list[16]="Mail check"
    elif pm_option=="Credit card (automatic)":
        col_list[16]="Credit card (automatic)"
    elif pm_option=="Bank transfer (automatic)":
        col_list[16]="Bank transfer (automatic)"

    Monthlycharges=st.number_input("Enter Monthly charges: ",step=0.01)
    col_list[17]=Monthlycharges

    Totalcharges=st.number_input("Enter Total charges:",step=0.01)
    col_list[18]=Totalcharges



    if st.checkbox("Your entries"):
        d={}
        feature=["gender","SeniorCitizen","Partner","Dependents","tenure","PhoneService","MultipleLines","InternetService","OnlineSecurity","OnlineBackup","DeviceProtection","TechSupport","StreamingTV","StreamingMovies","Contract","PaperlessBilling","PaymentMethod","MonthlyCharges","TotalCharges"]
        for i in range(len(feature)):
            if i<19:
                d[feature[i]]=col_list[i]
            else:
                d[feature[i]]=[col_list[i],col_list[i+1]]
        st.write(d)

    if st.button("Predict"):
        pass
def statistics():
    pass
def about():
    st.write("This is the project that is done by M. Vandith Reddy, KVS. Siddhartha, K Deepak Srinivas")
if __name__=="__main__":
    main() 