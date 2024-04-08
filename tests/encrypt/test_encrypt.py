from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Test case 1: 3 different returns with valid entries
    assert encrypt_message("Chiquinha", 10) == "ahniuqihC"
    assert encrypt_message("Pitty", 3) == "tiP_yt"
    assert encrypt_message("Polly", 2) == "yll_oP"

    # Test case 2: encrypt_message with invalid key
    with pytest.raises(TypeError) as exc_info_key:
        encrypt_message("Nega do Suéter", "4")
    assert str(exc_info_key.value) == "tipo inválido para key"

    # Test case 3: encrypt_message with invalid message
    with pytest.raises(TypeError) as exc_info_message:
        encrypt_message(1990, 4)
    assert str(exc_info_message.value) == "tipo inválido para message"
