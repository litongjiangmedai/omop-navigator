def build_cohort_sql(condition_concept_id):
    sql = f"""
    SELECT person_id, condition_start_date
    FROM condition_occurrence
    WHERE condition_concept_id = {condition_concept_id}
    """
    return sql.strip()
