# 함수 내부에서 값을 쓰고 싶으면 어떻게 해야하죠?
# 정의할 때 이름을 지어놓고, 호출할 때 값을 넘겨줘요!

class MyClass:
    class_variable = '클래스 변수'

    def __init__(self):
        self.instance_variable = '인스턴스 변수'

    def instance_method(self):
        return self, self.instance_variable

    @classmethod
    def class_method(cls):
        return cls, cls.class_variable

    @staticmethod
    def static_method():
        return ''