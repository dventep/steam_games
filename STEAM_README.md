---
license: cc-by-4.0
language:
  - en
tags:
- games
- steam
- video games
- gamedev
task_categories:
- text-generation
- text2text-generation
configs:
- config_name: default
  data_files:
  - split: train
    path: "data/train-00000-of-00001-e2ed184370a06932.parquet"
pretty_name: Steam Games Dataset
size_categories:
- 10K<n<100K
---
<p align="center"><img src="images/banner.png"/></p>

# Overview

Information of **more than 85,000 games** published on Steam. Maintained by **[Fronkon Games](https://github.com/FronkonGames)**.

This dataset has been created with **[this code (MIT)](https://github.com/FronkonGames/Steam-Games-Scraper)** and use the API provided by _Steam_, the largest gaming platform on PC. Data is also collected from _Steam Spy_.

Only published games, _no DLCs, episodes, music, videos, etc_.

Here is a simple example of how to parse json information:

```
# Simple parse of the 'games.json' file.
import os
import json

dataset = {}
if os.path.exists('games.json'):
  with open('games.json', 'r', encoding='utf-8') as fin:
    text = fin.read()
    if len(text) > 0:
      dataset = json.loads(text)

for app in dataset:
  appID = app                                         # AppID, unique identifier for each app (string).
  game = dataset[app]             

  name = game['name']                                 # Game name (string).
  releaseDate = game['release_date']                  # Release date (string).
  estimatedOwners = game['estimated_owners']          # Estimated owners (string, e.g.: "0 - 20000").
  peakCCU = game['peak_ccu']                          # Number of concurrent users, yesterday (int).
  required_age = game['required_age']                 # Age required to play, 0 if it is for all audiences (int).
  price = game['price']                               # Price in USD, 0.0 if its free (float).
  dlcCount = game['dlc_count']                        # Number of DLCs, 0 if you have none (int).
  longDesc = game['detailed_description']             # Detailed description of the game (string).
  shortDesc = game['short_description']               # Brief description of the game,
                                                      # does not contain HTML tags (string).
  languages = game['supported_languages']             # Comma-separated enumeration of supporting languages.
  fullAudioLanguages = game['full_audio_languages']   # Comma-separated enumeration of languages with audio support.
  reviews = game['reviews']                           #
  headerImage = game['header_image']                  # Header image URL in the store (string).
  website = game['website']                           # Game website (string).
  supportWeb = game['support_url']                    # Game support URL (string).
  supportEmail = game['support_email']                # Game support email (string).
  supportWindows = game['windows']                    # Does it support Windows? (bool).
  supportMac = game['mac']                            # Does it support Mac? (bool).
  supportLinux = game['linux']                        # Does it support Linux? (bool).
  metacriticScore = game['metacritic_score']          # Metacritic score, 0 if it has none (int).
  metacriticURL = game['metacritic_url']              # Metacritic review URL (string).
  userScore = game['user_score']                      # Users score, 0 if it has none (int).
  positive = game['positive']                         # Positive votes (int).
  negative = game['negative']                         # Negative votes (int).
  scoreRank = game['score_rank']                      # Score rank of the game based on user reviews (string).
  achievements = game['achievements']                 # Number of achievements, 0 if it has none (int).
  recommens = game['recommendations']                 # User recommendations, 0 if it has none (int).
  notes = game['notes']                               # Extra information about the game content (string).
  averagePlaytime = game['average_playtime_forever']  # Average playtime since March 2009, in minutes (int).
  averageplaytime2W = game['average_playtime_2weeks'] # Average playtime in the last two weeks, in minutes (int).
  medianPlaytime = game['median_playtime_forever']    # Median playtime since March 2009, in minutes (int).
  medianPlaytime2W = game['median_playtime_2weeks']   # Median playtime in the last two weeks, in minutes (int).

  packages = game['packages']                         # Available packages.
  for pack in packages:           
    title = pack['title']                             # Package title (string).
    packDesc = pack['description']                    # Package description (string).

    subs = pack['subs']                               # Subpackages.
    for sub in subs:            
      text = sub['text']                              # Subpackage title (string).
      subDesc = sub['description']                    # Subpackage description (string).
      subPrice = sub['price']                         # Subpackage price in USD (float).

  developers = game['developers']                     # Game developers.
  for developer in developers:            
    developerName = developer                         # Developer name (string).

  publishers = game['publishers']                     # Game publishers.
  for publisher in publishers:            
    publisherName = publisher                         # Publisher name (string).

  categories = game['categories']                     # Game categories.
  for category in categories:           
    categoryName = category                           # Category name (string).

  genres = game['genres']                             # Game genres.
  for gender in genres:           
    genderName = gender                               # Gender name (string).

  screenshots = game['scrennshots']                   # Game screenshots.
  for screenshot in screenshots:            
    scrennshotsURL = screenshot                       # Game screenshot URL (string).

  movies = game['movies']                             # Game movies.
  for movie in movies:            
    movieURL = movie                                  # Game movie URL (string).

  tags = game['tags']                                 # Tags.
  for tag in tags:           
    tagKey = tag                                      # Tag key (string, int).
```

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

## Step by step

In this part, we will look the process to go from a dataset named [steam-games-dataset] under the Hugging Face hosting to the storage of an initial structure in our database named [steam_games] shown in the diagrams below, to offer the latter to people.

1. Once I have the requirements and the objective to be achieved, flow diagrams are made to have a field visualization of the process to be developed.
- **Metadata of diagrams:** In this part, there are a few explaining of every block and his properties that you will look in the diagrams.
- **Data source block**: There is a **parquet** dataset hosting in Hugging Face with 83.560 rows of videogames data. This starting point dataset is called steam-games-dataset.
- **Data pipeline block**: In this section, there are two jupyter notebooks, which are:
- **load_initial_data**. The process of reading the **parquet** dataset by API and loading of data to **raw_games** table in a PostgreSQL Database called **steam_games**.
- **eda_report**. The process of data collection of **raw_games** table in **steam_games** database to explorate, transform, clean it and establish columns of importance. Then load data to **clean_games** table in the database.
- **Local server block**: There is a database in PostgreSQL called **steam_games** in the local server, this so far will have two tables, **raw_games a**nd **clean_games**.
            (If the database doesn't exist, **load_initial_data** notebook will create it and its structure.)

2. connect_database. To connect the load_initial_data notebook with steam-games-dataset (parquet file hosting in Hugging Face), a class called ConnectionPostgres is created that through the SQLAlchemy library that is highly used by its ORM, that depending on the HOST and PORT configuration credentials, links to local PostgreSQL.

3. **local_initial_data:** Once the connection has been made, the database and its structure is created by the class if it doesn’t exist, including **raw_games a**nd **clean_games** tables. When the proccess is executed, the tables will be reset if they already exists.


# Credits
