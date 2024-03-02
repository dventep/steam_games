""" This module is to declarative the SQL classes for the database """

from sqlalchemy import Column, Integer, Date, VARCHAR
from sqlalchemy.orm import declarative_base

BASE = declarative_base()


class RawGames(BASE):
    """This class is to create the table raw_games in the database. This table is to store the raw data from the steam games dataset."""

    __tablename__ = "raw_games"

    id = Column(Integer, primary_key=True)
    name = Column(VARCHAR(200), nullable=True, default=None)
    release_date = Column(VARCHAR(12), nullable=True, default=None)
    estimated_owners = Column(VARCHAR(30), nullable=True, default=None)
    peak_ccu = Column(VARCHAR(20), nullable=True, default=None)
    required_age = Column(VARCHAR(3), nullable=True, default=None)
    price = Column(VARCHAR(20), nullable=True, default=None)
    downloable_content_count = Column(VARCHAR(20), nullable=True, default=None)
    supported_languages = Column(VARCHAR(1500), nullable=True, default=None)
    full_audio_languages = Column(VARCHAR(1500), nullable=True, default=None)
    reviews = Column(VARCHAR(4000), nullable=True, default=None)
    website = Column(VARCHAR(500), nullable=True, default=None)
    support_url = Column(VARCHAR(500), nullable=True, default=None)
    support_email = Column(VARCHAR(500), nullable=True, default=None)
    windows = Column(VARCHAR(20), nullable=True, default=None)
    mac = Column(VARCHAR(20), nullable=True, default=None)
    linux = Column(VARCHAR(20), nullable=True, default=None)
    metacritic_score = Column(VARCHAR(20), nullable=True, default=None)
    metacritic_url = Column(VARCHAR(200), nullable=True, default=None)
    user_score = Column(VARCHAR(20), nullable=True, default=None)
    positive = Column(VARCHAR(20), nullable=True, default=None)
    negative = Column(VARCHAR(20), nullable=True, default=None)
    score_rank = Column(VARCHAR(20), nullable=True, default=None)
    achievements = Column(VARCHAR(20), nullable=True, default=None)
    recommendations = Column(VARCHAR(20), nullable=True, default=None)
    average_playtime_forever_minute = Column(VARCHAR(20), nullable=True, default=None)
    average_playtime_two_weeks_minute = Column(VARCHAR(20), nullable=True, default=None)
    median_playtime_forever_minute = Column(VARCHAR(20), nullable=True, default=None)
    median_playtime_two_weeks_minute = Column(VARCHAR(20), nullable=True, default=None)
    developers = Column(VARCHAR(800), nullable=True, default=None)
    publishers = Column(VARCHAR(800), nullable=True, default=None)
    categories = Column(VARCHAR(500), nullable=True, default=None)
    genres = Column(VARCHAR(500), nullable=True, default=None)
    tags = Column(VARCHAR(500), nullable=True, default=None)

    def __str__(self) -> str:
        return f"Raw {self.name} - {self.release_date}"
