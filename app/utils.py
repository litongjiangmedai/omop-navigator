import os

def get_db_path():
    """
    Returns the path to the OMOP database.
    - Uses the OMOP_DB_PATH environment variable if set.
    - Otherwise defaults to demo database.
    """
    return os.getenv("OMOP_DB_PATH", "data/synthea_omop_full_demo.sqlite")
