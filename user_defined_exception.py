class EgTypeCdException(Exception):
    def __init__(self, eg):
        super().__init__()
        msg = "EG '{eg_type_cd}' is inappropriate!"
        self.msg = msg.format(eg_type_cd=eg)

    def __str__(self):
        return self.msg
