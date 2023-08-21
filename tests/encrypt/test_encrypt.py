from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    assert encrypt_message('xablau', 3) == 'bax_ual'
    assert encrypt_message('xablau', 4) == 'ua_lbax'
    assert encrypt_message('xablau', 99) == 'ualbax'
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message('xablau', 'xablau')
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(5, 2)
