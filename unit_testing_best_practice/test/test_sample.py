import sys
# Always run from unit_testing_best_practice/test
sys.path += ['../src']

import io


from sample import *


def test_test(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "nospace")
    assert check_username("nospace") == 1

def test_username(monkeypatch):
    
    # Correct usernames
    monkeypatch.setattr('builtins.input', lambda _: "nospace")
    assert check_username("nospace") == 1

    monkeypatch.setattr('builtins.input', lambda _: "45345345")
    assert check_username("45345345") == 1

    monkeypatch.setattr('builtins.input', lambda _: "4234/*-*-/324dfsdfDFSDfsdfds")
    assert check_username("4234/*-*-/324dfsdfDFSDfsdfds") == 1

    # Incorrect usernames
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert check_username("") == 0

    monkeypatch.setattr('builtins.input', lambda _: "with space")
    assert check_username("with space") == 0

def test_password(monkeypatch):
    # Correct password
    monkeypatch.setattr('builtins.input', lambda _: "123qSc%/")
    assert check_password("123qSc%/") == 1

    monkeypatch.setattr('builtins.input', lambda _: "abCD1234%$")
    assert check_password("abCD1234%$") == 1

    monkeypatch.setattr('builtins.input', lambda _: "$*reTR87")
    assert check_password("$*reTR87") == 1

    monkeypatch.setattr('builtins.input', lambda _: "1A$8f9!h")
    assert check_password("1A$8f9!h") == 1

    monkeypatch.setattr('builtins.input', lambda _: "132165165165165165165121651aB*")
    assert check_password("132165165165165165165121651aB*") == 1

    monkeypatch.setattr('builtins.input', lambda _: "*%&$%&$)()()(&$%&BBBBBBBB2t")
    assert check_password("*%&$%&$)()()(&$%&BBBBBBBB2t") == 1

    monkeypatch.setattr('builtins.input', lambda _: "onetwoTHREEfour5!")
    assert check_password("onetwoTHREEfour5!") == 1

    # Incorrect password
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert check_password("") == 0

    monkeypatch.setattr('builtins.input', lambda _: "12345678")
    assert check_password("12345678") == 0

    monkeypatch.setattr('builtins.input', lambda _: "abcdefgh")
    assert check_password("abcdefgh") == 0

    monkeypatch.setattr('builtins.input', lambda _: "!!!!!!!!")
    assert check_password("!!!!!!!!") == 0

    monkeypatch.setattr('builtins.input', lambda _: "withoutSpecialCharacter06")
    assert check_password("withoutSpecialCharacter06") == 0

    monkeypatch.setattr('builtins.input', lambda _: "-1-1-1-1-1")
    assert check_password("-1-1-1-1-1") == 0

    monkeypatch.setattr('builtins.input', lambda _: "QwErTyUi")
    assert check_password("QwErTyUi") == 0

def test_email(monkeypatch):
    # Correct emails
    monkeypatch.setattr('builtins.input', lambda _: "@.")
    assert check_email("@.") == 1

    monkeypatch.setattr('builtins.input', lambda _: "asdasd@adsad@dadsad@.com")
    assert check_email("asdasd@adsad@dadsad@.com") == 1

    monkeypatch.setattr('builtins.input', lambda _: "asdasdsa.dasdsa@")
    assert check_email("asdasdsa.dasdsa@") == 1

    monkeypatch.setattr('builtins.input', lambda _: "ameple@io.com")
    assert check_email("sameple@io.com") == 1

    monkeypatch.setattr('builtins.input', lambda _: "243243@342342.234324")
    assert check_email("243243@342342.234324") == 1

    monkeypatch.setattr('builtins.input', lambda _: "%&$$%@54534.....")
    assert check_email("%&$$%@54534.....") == 1

    # Incorrect emails
    monkeypatch.setattr('builtins.input', lambda _: "")
    assert check_email("") == 0

    monkeypatch.setattr('builtins.input', lambda _: " ")
    assert check_email(" ") == 0

    monkeypatch.setattr('builtins.input', lambda _: "adasodsa@dasdasdcom")
    assert check_email("adasodsa@dasdasdcom") == 0

    monkeypatch.setattr('builtins.input', lambda _: "adijasijdas.com")
    assert check_email("adijasijdas.com") == 0
