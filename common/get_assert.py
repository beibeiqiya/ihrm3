def get_assert(status_code, success, code, message, response1):
    assert status_code == response1.status_code
    assert success == response1.json().get("success")
    assert code == response1.json().get("code")
    assert message == response1.json().get("message")