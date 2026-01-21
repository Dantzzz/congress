# Congressional Data Analysis Pipeline

## Project Overview
This application is designed to fetch, organize, and store data pertaining to the 119th Congress.
Metrics are then displayed on an interactive dashboard, providing insights into the degree of bipartisan support, cosponsor composition, and voting patterns. 

The project demonstrates end-to-end data pipeline proficiency, including REST API integration, relational database design and SQLAlchemy ORM, 
and visualization of KPIs and other metrics.

## Skills Demonstrated
- ETL Pipeline Development
- REST API Integration
- Relational database design and data modeling
- EDA and visualization
- Version control

## Tech Stack
- Python          - Pandas 
- SQL             - SQLAlchemy
- Tableau Public  - Congress.gov API
- Linux           - DBeaver
- Git/GitHub      - PostgreSQL

## Installation & Setup
{placeholder}

## Project Structure
{placeholder}

## Future Enhancements
- Daily updates and caching to avoid redundancy
- Retrieval of data from previous congressional terms
- ML extension to estimate the likelihood of a bill's success.
- Cloud migration

## TODO (PHASE 2)
- Read Congress.gov API documentation
     - Available endpoints
     - Authentication
     - Response formats
     - Rate limits (5000/hr)
- Python script to authenticate with API
- Helper functions to fetch data (bills, voting records, etc)
- Pagination Handling (20 default/max 250)
- Error handling and Rate limiting
- Parse JSON into Python dicts and convert to df's
- Test w/ sample csv export
- Unit tests for API functions
- Create config file for API settings