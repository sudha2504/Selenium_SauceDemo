

class Config:
    def __init__(self, env):

        SUPPORTED_ENV = ['dev','qa']

        # if env is None :
        #     env = "qa"

        self.base_url = {
            'dev' : 'http://localhost:8000',
             'qa' : 'https://www.saucedemo.com/'
        }[env]