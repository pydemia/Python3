class Myclass(object):

    def __init__(self, cls_name):
        self.name = cls_name

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

    def __getattribute__(self, name):
        return name, super().__getattribute__(name)

    # Use Bracket
    def __setitem__(self, name, value):
        super().__setattr__(name, value)

    def __getitem__(self, name):
        return name, super().__getattribute__(name)

if __name__ == '__main__':
    test = Myclass('test_instance')
    
    test['user'] = 'kyongmin'
    test.user
    test['user']

    test.admin = 'kkm'
    test.admin
    test['admin']

