class Student:
    """
    单例模式
    """

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)

            return cls.instance

