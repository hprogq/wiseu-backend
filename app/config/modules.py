class ModulesConfig:
    ENABLED_MODULES = {
        "course_schedule": True,
        "grades": True,
        "library_reservations": True,
        "knowledge_base": True,
    }
    UPDATE_INTERVAL = {
        "course_schedule": 3600,  # seconds
        "grades": 86400,
        "library_reservations": 3600,
        "knowledge_base": 604800,
    }
