def search_sections(sections, course_code=None, department=None):
    """Search course sections by course code and department."""
    return [
        section
        for section in sections
        if (course_code is None or section["course_code"] == course_code)
        and (department is None or section["department"] == department)
    ]