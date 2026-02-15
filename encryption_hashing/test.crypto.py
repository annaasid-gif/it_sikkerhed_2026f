from crypto import encrypt_data, decrypt_data, hash_password, verify_password

# GIVEN: vi har en tekst der skal krypteres
def test_encrypt_and_decrypt():
    original = "Anna A, Zealand Næstved"

    # WHEN: vi krypterer og derefter dekrypterer
    encrypted = encrypt_data(original)
    decrypted = decrypt_data(encrypted)

    # THEN: den dekrypterede tekst skal være den samme
    assert decrypted == original  # Risiko: Hvis testen fejler, kan data blive ødelagt

# GIVEN: et password der skal hashes
def test_hash_and_verify_password():
    password = "Test123!"

    # WHEN: vi hasher og validerer password
    hashed = hash_password(password)
    result = verify_password(password, hashed)

    # THEN: passwordet skal godkendes
    assert result is True  # Risiko: Hvis testen fejler, kan brugere ikke logge ind sikkert
