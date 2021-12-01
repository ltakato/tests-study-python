from hello_service import hello_pessoinha


def test_hello_passed_pessoinha():
    pessoinha = 'rennanzera'
    assert hello_pessoinha(pessoinha) == f'hello {pessoinha}'


def test_hello_passed_empty_string():
    pessoinha = ''
    assert hello_pessoinha(pessoinha) == 'hello alguemzinho'
