![Steam Games Dataset](https://gist.githubusercontent.com/dventep/fc64df11bc7aeb08ce9c231152970221/raw/a6f29556487e70e6a88eb6033779b8f25bf309b9/banner.png)

# About the project

The objective of this project is to develop a predictive model to estimate the potential acquisition or popularity of a video game based on various characteristics. These characteristics include features such as user ratings, gameplay hours, genre, platform, release date, developer, and publisher. By analyzing these factors, we aim to create a model that can predict the success of a video game upon its release or even beforehand.

### Exploratory Data Analysis (EDA)

Before building the predictive model, it's crucial to conduct an Exploratory Data Analysis (EDA) to gain insights into the dataset. Here's an outline of the EDA process:

1. **Data Collection**: Gather the dataset containing information about video games, including their features and popularity metrics. (steam_dataset)
   
2. **Data Cleaning and Preprocessing**: 
   - Handle missing values: Check for missing data in any of the features and decide on the appropriate strategy for dealing with them, such as imputation or removal.
   - Data formatting: Ensure consistency in data types and formats across different features.
   - Remove duplicates: Eliminate any duplicate entries in the dataset.
   
3. **Descriptive Statistics**: Calculate summary statistics for numerical features (e.g., mean, median, standard deviation) and categorical features (e.g., frequency distribution, mode).

4. **Data Visualization**: 
   - Histograms: Visualize the distribution of numerical features to understand their spread and identify any outliers.
   - Bar plots: Display the frequency distribution of categorical features, such as genre, platform, developer, and publisher.
   - Correlation matrix: Explore the relationships between different features by calculating and visualizing correlation coefficients.
   - Scatter plots: Investigate potential relationships between variables, such as user ratings and gameplay hours, using scatter plots.

5. **Feature Engineering**:
   - Create new features: Derive additional features from existing ones that might provide valuable information for the predictive model.
   - Transformations: Apply transformations (e.g., log transformation) to numeric variables to improve their distribution.

6. **Outlier Detection and Treatment**: Identify outliers in the dataset and decide whether to remove them or apply appropriate transformations.

By conducting a thorough EDA, we can gain a deeper understanding of the dataset and identify patterns and relationships that will inform the development of the predictive model. This exploratory phase sets the foundation for building a robust and accurate predictive model for estimating the acquisition or popularity of video games.

# Details

In this project, we have a dataset on Steam platform of 83,560 games registered and 39 columns that after processing are now 20 columns including new with last updated on January 12, 2024 and with the oldest release on June 30, 1997 being Carmageddon Max Pack. With this data we want to answer the question Can we build a predictive model to estimate the acquisition or the degree of acquisition of a game based on its features, scores and hours played?

This document outlines the first phase of the process that we carry out:

1. Execution of a request to the Hugging Face API service to bring the dataset into the **parquet** structure.
2. Initial exploratory data analysis for::
    - To know the structure of these.
    - To specify the possibility that with the data we can answer the question.
    - Exclude columns from the process that are discriminated as of no interest and for not saturing data in the database.
3. Initial upload to the database of raw data (unprocessed through a detailed and robust EDA and ETL process).
4. In-depth exploratory data analysis.

## Tools used are:

- [Python 🐍.](https://www.python.org/)
- [Git 📦.](https://git-scm.com/about)
- [Postgres 💽.](https://www.postgresql.org/)
- [PgAdmin 4 📇.](https://www.pgadmin.org/)
- [GitHub 💼.](https://github.com/)
- [Visual Studio Code 📝](https://code.visualstudio.com/)

## Installing

In this part, we will look the process to go from a dataset named [steam-games-dataset] under the Hugging Face hosting to the storage of an initial structure in our database named [steam_games] shown in the diagrams below, to offer the latter to people.

1. Once I have the requirements and the objective to be achieved, flow diagrams are made to have a field visualization of the process to be developed.
- **Metadata of diagrams:** In this part, there are a few explaining of every block and his properties that you will look in the diagrams.
- **Data source block**: There is a **parquet** dataset hosting in Hugging Face with 83.560 rows of videogames data. This starting point dataset is called steam-games-dataset.
- **Data pipeline block**: In this section, there are two jupyter notebooks, which are:
- **load_initial_data**. The process of reading the **parquet** dataset by API and loading of data to **raw_games** table in a PostgreSQL Database called **steam_games**.
- **eda_report**. The process of data collection of **raw_games** table in **steam_games** database to explorate, transform, clean it and establish columns of importance. Then load data to **clean_games** table in the database.
- **Local server block**: There is a database in PostgreSQL called **steam_games** in the local server, this so far will have two tables, **raw_games a**nd **clean_games**.
            (If the database doesn't exist, **load_initial_data** notebook will create it and its structure.)

2. connect_database. To connect the load_initial_data notebook with steam-games-dataset (parquet file hosting in Hugging Face), a class called ConnectionPostgres is created that through the SQLAlchemy library that is highly used by its ORM, that depending on the HOST and PORT configuration credentials file, links to local PostgreSQL. (The file must is locate from root folder in ./code/config/ with name credentials.ini.)

3. **local_initial_data:** Once the connection has been made, the database and its structure is created by the class if it doesn’t exist, including **raw_games a**nd **clean_games** tables. When the proccess is executed, the tables will be reset if they already exists.

## Dasboard
https://app.powerbi.com/view?r=eyJrIjoiYjE0ODZlODctMjBkNy00NzNkLTkyYTQtZTdmNDA0NDM2MTM1IiwidCI6IjY5M2NiZWEwLTRlZjktNDI1NC04OTc3LTc2ZTA1Y2I1ZjU1NiIsImMiOjR9

# Credits
@GersonYF, @dventep and @Davele12
