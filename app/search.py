def search_sections(sections, course_code=None, department=None, instructor=None):
    """Search course sections by course code, department, and instructor."""
    return [
        section
        for section in sections
        if (course_code is None or section["course_code"] == course_code)
        and (department is None or section["department"] == department)
        and (instructor is None or section["instructor"] == instructor)
    ]