from .web_driver import WebAutomation

def test_login():
        webdriver = WebAutomation('SPglp2WH020','Bia2023@@')
        login = webdriver.login()
        webdriver.close_browser()
        
        assert login['status'] == 'Login feito com sucesso!'
        