![Steam Games Dataset](https://gist.github.com/dventep/fc64df11bc7aeb08ce9c231152970221/raw/a6f29556487e70e6a88eb6033779b8f25bf309b9/banner.png)

## Process
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
