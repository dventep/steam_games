""" This module is to establish connection with PostgreSQL's database """

# Import libraries
import logging
from configparser import ConfigParser
from sqlalchemy import create_engine
from sqlalchemy_utils import create_database
from sqlalchemy_utils import database_exists
from sqlalchemy.orm import sessionmaker
import importlib.util

spec = importlib.util.spec_from_file_location("sql_classes", "../code/models/sql_classes.py")
sql_classes = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sql_classes)

# ? Logger basic settings
logging.basicConfig(
    level=logging.DEBUG,
    filename="../code/log/workshop001.log",
    encoding="utf-8",
    format="%(asctime)s - %(levelname)s - %(message)s",
)


class ConnectionPostgres:
    """Create connection with PostgreSQL"""

    PARSER = ConfigParser()
    # Connection data for PostgreSQL
    CREDENTIALS_FILENAME = "../code/config/credentials.ini"
    DATABASE_SECTION = "postgresql"

    def __init__(self) -> None:
        """Constructor"""

        self.connection_config = False
        self.engine = False
        self.session = False
        self.data_to_connection()
        self.modules = {}

        if self.connection_config:
            self.create_engine()
            self.create_connection()

    def make_tables(self) -> None:
        """Method to create tables in database
            
            Returns: None
        """

        sql_classes.BASE.metadata.drop_all(self.engine)
        sql_classes.BASE.metadata.create_all(self.engine)

    def get_module_records(self, table_name):
        """Method to get records of a table in the database
        
            Parameters:
                table_name: str
                    Name of the table in the database
            Returns: List
                List of dictionaries with records of the specified table.        
        """

        raw_applicant_table = self.get_modules()[table_name]
        records = self.session.query(raw_applicant_table).all()
        return [record.__dict__ for record in records]

    def get_modules(self) -> dict:
        """Method to get classes structure of every table in the database

            Returns: dict
                Dictionary with classes structure of every table in the database
        """

        self.modules = {"RawApplicant": sql_classes.RawApplicant, "Applicant": sql_classes.Applicant}
        return self.modules

    def data_to_connection(self) -> None:
        """Method to get credentials data to connect with database
        
            Returns: None
        """

        self.PARSER.read(self.CREDENTIALS_FILENAME)
        connection_config = {}

        if not self.PARSER.has_section(self.DATABASE_SECTION):
            raise Exception(f"Section {self.DATABASE_SECTION} not found in {self.CREDENTIALS_FILENAME} file.")

        params = self.PARSER.items(self.DATABASE_SECTION)
        for param in params:
            connection_config[param[0]] = param[1]
        self.connection_config = connection_config

    def create_connection(self) -> None:
        """Method to create a connection with database
        
            Returns: None
        """

        Session = sessionmaker(self.engine)
        self.session = Session()
        logging.info(f"Connected with {self.connection_config['database']} - user: {self.connection_config['user']}")

    def close_connection(self) -> None:
        """Method to close connection with database
        
            Returns: None
        """

        if self.session:
            self.session.close()
            logging.info(
                f"Connection with {self.connection_config['database']} - user: {self.connection_config['user']} closed."
            )

    def log(self, text) -> None:
        """Method to create log records
        
            Parameters:
                text: str
                    Text to be logged.
            
            Returns: None
        """

        logging.info(text)

    def create_engine(self) -> None:
        """Method to create a connection with database
        
            Returns: None
        """

        engine_url = f"{self.DATABASE_SECTION}://{self.connection_config['user']}:{self.connection_config['password']}@{self.connection_config['host']}:{self.connection_config['port']}/{self.connection_config['database']}"

        self.engine = create_engine(engine_url)

        if not database_exists(self.engine.url):
            create_database(self.engine.url)
            logging.info(f"Database {self.connection_config['database']} created.")
