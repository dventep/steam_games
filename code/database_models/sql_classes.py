""" This module is to declarative the SQL classes for the database """

from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Date, CheckConstraint

BASE = declarative_base()


class RawApplicant(BASE):
    """This class is to create the table raw_applicant in the database. This table is to store the raw data from the applicants."""

    __tablename__ = "raw_applicant"

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50), nullable=True, default=None)
    last_name = Column(String(50), nullable=True, default=None)
    email = Column(String(60), nullable=True, default=None)
    applicant_date = Column(String(20), nullable=True, default=None)
    country = Column(String(40), nullable=True, default=None)
    experience_year = Column(String(40), nullable=True, default=None)
    seniority = Column(String(40), nullable=True, default=None)
    technology = Column(String(40), nullable=True, default=None)
    code_challenge_score = Column(String(40), nullable=True, default=None)
    technical_interview_score = Column(String(40), nullable=True, default=None)

    def __str__(self) -> str:
        return f"Raw {self.first_name} {self.last_name}"
