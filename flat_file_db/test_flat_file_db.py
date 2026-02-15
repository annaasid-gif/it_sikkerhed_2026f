import pytest
from flat_file_db import init_db, add_user, get_user

def setup_function():
    init_db()  # GIVEN: databasen findes

def test_add_user():
    # WHEN: vi tilføjer en bruger
    user = {
        "person_id": 1,
        "first_name": "Anna",
        "last_name": "A",
        "address": "Zealand Næstved",
        "street_number": 12,
        "password": "Test123!",
        "enabled": True
    }

    add_user(user)
    result = get_user(1)

    # THEN: brugeren skal kunne findes
    assert result is not None  # Risiko: Hvis testen fejler, kan brugere ikke gemmes korrekt

def test_user_not_found():
    # WHEN: vi søger efter en bruger der ikke findes
    result = get_user(999)

    # THEN: funktionen skal returnere None
    assert result is None  # Risiko: Systemet kan returnere forkerte brugere
