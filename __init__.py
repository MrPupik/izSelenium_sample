from Autotest.izSelenium import GetDriver as _get_driver


def GetDriver(name='keep'):
    '''
    global driver for keep projects
    '''
    return _get_driver(name)
