import streamlit as st

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)



def main():
    st.set_page_config(page_title='ML Tasks Overview', layout='wide')
    task = st.sidebar.selectbox('Choose the task', ('Intro','Regression', 'Classification', 'EDA'))


    if task == 'Intro':
        st.title("Automating the Automations")
        st.markdown(
            'This app helps you to easily compare the performance of different machine learning algorithms for both **classification** and **regression** problems. ')

        st.markdown('The app follows a standard data science pipeline:')
        st.markdown('1. **Exploratory Data Analysis (EDA)**: Understanding the dataset and its variables')
        st.markdown(
            '2. **Model building**: Building machine learning models for either classification or regression problems')
        st.markdown('3. **Model evaluation**: Comparing the performance of different models')

        st.markdown(
            'By using this app, you can save a lot of time and effort in building and evaluating different machine learning models, as the app automates these tasks for you. In side bar you choose the task you wanna perform')

    if task == 'Regression':
        st.title('Regression Task')
        st.write(
            'Regression is a technique used to predict a continuous target variable from a set of independent variables')
        st.write(
            'It is mainly used when the target variable is continuous in nature and the relationship between target variable and the independent variables is linear')
        st.write('In this task, you will be able to predict the house prices, employee salaries, stock prices and more')
        st.write("You have selected Regression task.")
        st.markdown("Please follow this link for the Regression task: [Regression Site](https://sj0605-datasci-autoeda-automl-auto-regressionmain-1y4edt.streamlit.app/)")

    if task == 'Classification':
        st.title('Classification Task')
        st.write(
            'Classification is a technique used to predict a categorical target variable from a set of independent variables')
        st.write(
            'It is mainly used when the target variable is categorical in nature and the relationship between target variable and the independent variables is non-linear')
        st.write(
            'In this task, you will be able to predict the type of iris flower, predict whether a customer will churn or not, and more')
        st.write("You have selected Classification task.")
        st.markdown(
            "Please follow this link for the Classification task: [Classification Site](https://sj0605-datasci-autoeda-automl-auto-classificationmain2-enpa5u.streamlit.app/)")

    if task == 'EDA':
        st.title('Exploratory Data Analysis (EDA) Task')
        st.write(
            'Exploratory Data Analysis (EDA) is a technique used to understand the data by summarizing its main characteristics')
        st.write(
            'It helps to understand the distribution of the data, the relationship between variables, and the presence of any outliers or anomalies')
        st.write(
            'In this task, you will be able to understand the relationship between different variables, visualize the data and more')
        st.write("You have selected EDA task.")
        st.markdown(
            "Please follow this link for the EDA task: [EDA Site](https://sj0605-datasci-autoeda-automl-auto-edamain3-uq15zc.streamlit.app/)")


if __name__ == '__main__':
    main()
    local_css("Sj0605-DataSci/AutoEDA-AutoML/style/style.css")
