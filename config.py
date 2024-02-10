CSS = open("assets/css/styles.css", 'r').read()
CSS2 = {
    "icon": {"colo": "white"},
    "nav-link": {"--hover-colo": "grey"},
    "nav-link-selected": {"background-color": "#232FAC"},
}

IMG_BANNER = "assets/images/banner.png"
IMG_BANNER2 = "assets/images/banner2.png"
IMG_OMDENA = "assets/images/omdena-logo.png"
IMG_LOGO = "assets/images/logo.png"
IMG_ALGERIA = "assets/images/algeria.png"
IMG_BHOPAL = "assets/images/bhopal.png"
IMG_BACKGROUND = "assets/images/background.webp"

ALGERIA_DATASET = "assets/dataset/algeria/GLDAS_GFS_population_Algeria_2015_2023_final.csv"
BHOPAL_DATASET = "assets/dataset/bhopal/Bhopal_CompleteData_Final_Modified.csv"

SIDEBAR_TEXT_1 = """
<center><h1>Omdena Algeria & Bhopal Chapter</h1></center>
"""
SIDEBAR_TEXT_2 = """
<h3 class='sidebar_h1'>Disclaimer</h3>
<h5 class='sidebar_h1'>The predictions provided by this system are for informational purposes only.</h5>
<hr>
"""


PROJECT_BACKGROUND = """
## Project background
The arid climate of several Algerian regions and the water-stressed region of Bhopal, effective water management and forecasting are crucial. This project aims to harness the power of machine learning to address the unique water resource challenges faced by both regions. By creating an open-source solution, we aim to empower Algeria and Bhopal to make informed decisions, optimize resource allocation, and build resilient water infrastructure for a sustainable future. <br><br>
Local Chapter Website : [Visit Site](https://www.omdena.com/chapter-challenges/open-source-water-management-and-forecasting-project-in-algeria-and-bhopal) <br>
Dagshub Repository : [Visit Site](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting) <br>
"""

PROJECT_PROBLEM = f"""
## The Problem
The different water resource challenges faced by both Algeria and Bhopal region in India.
"""

PROJECT_GOALS = """
## Project Goals
##### **1. Develop a Comprehensive Open-Source Water Management and Forecasting System:**
Create a user-friendly platform tailored to the specific needs of Algeria and Bhopal, integrating machine learning algorithms for precise water forecasting and efficient water resource management. 
##### **2. Enhance Water Resource Utilization:**
Improve the sustainable use of water resources in both regions by providing accurate forecasts and real-time monitoring.
##### **3. Capacity Building:**
Empower local stakeholders in Algeria and Bhopal with the knowledge and tools necessary to make well-informed decisions about water management.
##### **4. Community Engagement:**
Foster collaboration among local government agencies, NGOs, and the research community to collectively address water-related challenges in both regions.
"""

PROJECT_TIMELINE = """
## Project Timeline
##### 1. Project Initiation: 
Define project goals and scope. Identify key stakeholders and project team members and teams. Secure resources.
##### 2. Research and Data Collection: 
Gather historical weather and water data specific to Algeria and Bhopal. Collect satellite imagery and remote sensing data. Use open source data.
##### 3. Visualization and Exploration:
Visualize and explore the data and identify relevant machine learning algorithms accordingly.
##### 4. Development of Water Management Platform: 
Design and develop the open-source platform for water management and forecasting. Implement machine learning models for water forecasting, water resources disponibility, quality and risks.
##### 5. Testing and Validation: 
Conduct extensive testing of the platform using historical data. Validate the accuracy of machine learning models. Address any issues or bugs that arise during testing.
##### 6. Deployment and Maintenance: 
Deploy the water management platform for operational use. Monitor and maintain the platform. Provide ongoing support and updates.
##### 7. Data Dissemination:
Refine the github repository of the project and prepare the final demo for presentation on the official platforms of Omdena and the parties involved. Write conference and/or journal papers to publish the presented solutions.
"""


OVERVIEW_PHASE1 = """
## Phase 1: Data Collection & Preprocessing
[Dagshub Directory](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/data)

The first phase is all about collecting data from different sources and merging them into a single dataset. The dataset is then preprocessed and cleaned to remove any missing values and outliers. The final dataset is then used for further analysis and model building.
1. Raw Datasets: [Visit Link](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/data/raw)
2. Preprocessed Datasets: [Visit Link](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/data/processed)

##### 3. Final Datasets:
"""

OVERVIEW_PHASE2 = """
---
## Phase 2: Exploratory Data Analysis (EDA)
[Dagshub Directory](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks)

EDA is involves delving into raw datasets with a curious mindset, employing statistical techniques and visualizations to unravel the underlying patterns, anomalies, and relationships within the data. It's a crucial preliminary step in the data analysis journey, aiming to extract meaningful insights, identify trends, and inform subsequent analytical decisions.
All the jupyter notebooks created by our contributors for EDA can be found below:

##### **A) Population**
1. [EDA_Amir_FARES_Algiers borders and population.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Population/EDA_Amir_FARES_Algiers%20borders%20and%20population.ipynb), by **Amir Fares**
2. [EDA_Bhopal_Population_Michelle_COYLE.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Population/EDA_Bhopal_Population_Michelle_COYLE.ipynb), by **Michelle Coyle**
3. [Population_data_EDA_Meriem_.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Population/Population_data_EDA_Meriem_.ipynb), by Meriem Arab

##### **B) Surface and Ground Water**
1. [GFS_GLDAS_EDA_Weather_MihoRosenberg.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Surface%20&%20Groundwater/GFS_GLDAS_EDA_Weather_MihoRosenberg.ipynb), by **Miho Rosenberg**
2. [EDA_Bhopal_Surface_Water_Michelle_COYLE.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Surface%20&%20Groundwater/EDA_Bhopal_Surface_Water_Michelle_COYLE.ipynb), by **Michelle Coyle**
3. [EDA_GLDAS_Hariprasad_VL.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Surface%20&%20Groundwater/EDA_GLDAS_Hariprasad_VL.ipynb), by **Hariprasad VL**

##### **C) Weather Parameters**
1. [Bhopal_Rainfall_EDA_Hariprasad_VL.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Weather%20Parameters/Bhopal_Rainfall_EDA_Hariprasad_VL.ipynb), by **Hariprasad VL**
2. [EDA_Bhopal_Weather_MihoRosenberg.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Weather%20Parameters/EDA_Bhopal_Weather_MihoRosenberg.ipynb), by **Miho Rosenberg**
3. [EDA_Meriem_Arab.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Weather%20Parameters/EDA_Meriem_Arab.ipynb), by **Meriem Arab**
4. [EDA_Weather_Algeria_Meriem.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Weather%20Parameters/EDA_Weather_Algeria_Meriem.ipynb), by **Meriem Arab**
5. [EDA_weather_Emanuel_AFESSA.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task2_EDA/notebooks/Weather%20Parameters/EDA_weather_Emanuel_AFESSA.ipynb), by **Emanuel Afessa**
"""

OVERVIEW_PHASE3 = """
---
## Phase 3: Preprocessing
[Dagshub Directory](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks)

Data preprocessing involves cleaning and transforming the data to make it suitable for analysis. The goal of data preprocessing is to make the data accurate, consistent, and suitable for analysis. It helps to improve the quality and efficiency of the data mining process. Notebooks developed by our contributors are mentioned below: 

1. [AlgeriaModifiedCalculations_AmirFARES.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks/AlgeriaModifiedCalculations_AmirFARES.ipynb), by **Amir Fares**
2. [Modified_preprocessing_Bhopal_Hariprasad.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks/Modified_preprocessing_Bhopal_Hariprasad.ipynb), by **Hariprasad**
3. [combine_bhopal_GLDAS_GFS_MihoRosenberg.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks/combine_bhopal_GLDAS_GFS_MihoRosenberg.ipynb), by **Miho Rosenberg**
4. [preprocessing_algeria_MihoRosenberg.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks/preprocessing_algeria_MihoRosenberg.ipynb), by **Miho Rosenberg**
5. [preprocessing_bhopal_MihoRosenberg.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task3_Preprocessing/notebooks/preprocessing_bhopal_MihoRosenberg.ipynb), by **Miho Rosenberg**
"""

OVERVIEW_PHASE4 = """
---
## Phase 4: Model Development
[Dagshub Directory](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task4_ModelDevelopment/notebooks)

Model development is the most important part of the project. Model development is the iterative process of creating and refining mathematical or computational representations to understand or predict phenomena. The model is developed using the final preprocessed dataset from the previous phases.

Collaborator Notebooks:

1. [Algeria_Modeling_Amir_FARES.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task4_ModelDevelopment/notebooks/Algeria_Modeling_Amir_FARES.ipynb), by Amir Fares             
2. [CNN-LSTM Model Abhinav Agrawal.ipynb](https://dagshub.com/Omdena/AlgeriaBhopal_WaterManagementandForecasting/src/main/src/Task4_ModelDevelopment/notebooks/CNN-LSTM%20Model%20Abhinav%20Agrawal.ipynb), by Abhinav Agrawal             
"""

OVERVIEW_PHASE5 = """
---
## Phase 5: Model Deployment
[Github Directory](https://github.com/arpy8/Omdena_Algeria_Bhopal_Streamlit_App)

Model development is the iterative process of creating and refining mathematical or computational representations to understand or predict phenomena. The model is developed using the final preprocessed dataset from the previous phases. 

Collaborators who contributed to this phase are mentioned below:
1. [Anastasiia Marchenko](https://www.linkedin.com/in/anastasia-marchenko/)             
2. [Argish Abhangi](https://www.linkedin.com/in/argish/)             
2. [Arpit Sengar](https://www.linkedin.com/in/arpitsengar/)             
"""


LAG_SIZE = 3
TARGET = "daily_water_volume"

ALGERIA_AGG_DATASET = "assets/dataset/algeria/algeria_month_agg.csv"
ALGERIA_POPULATION = "assets/dataset/algeria/Algiers-population-2023-11-22.csv"
ALGERIA_MODEL = "assets/model/RandomForestRegressorAlgeria.joblib"

BHOPAL_AGG_DATASET = "assets/dataset/bhopal/bhopal_month_agg.csv"
BHOPAL_POPULATION = "assets/dataset/bhopal/Bhopal-population-2023-11-22.csv"
BHOPAL_MODEL = "assets/model/RandomForestRegressorBhopal.joblib"


CONTRIBUTORS = """
<h1 style="text-align: center; color:#FFF6F4;">A heartfelt thankyou to all our contributors ❤️</h1><hr>
<div style="text-align:center;">
<table>
<tr>
    <th width="20%" style="font-size: 140%;">Chapter Name</th>    
    <th width="20%" style="font-size: 140%;">Chapter Lead</th>    
</tr>
<tr>
    <td>Omdena Algeria Chapter</td>    
    <td>Kheira Lakhdari</td>    
</tr>
<tr>    
    <td>Omdena Bhopal Chapter</td>    
    <td>Chapter Lead</td>    
</tr>
</table>
<br>
<table>
    <tbody>
        <tr>
            <th width="20%" style="font-size: 140%;" colspan="3">Contributors</th>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
        <tr>
            <td>John Doe</td>
            <td>John Doe</td>
            <td>John Doe</td>
        </tr>
    </tbody>
</table>
</div>
"""