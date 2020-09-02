# 面向对象编程

### 类的四个要素
    类 属性 函数（方法） 对象（实例）
    类，一群有着相同属性和函数的对象的集合。
    
### 抽象类
    from abc import ABCMeta, abstractmethodclass
    
     Entity(metaclass=ABCMeta):
        @abstractmethod
        def get_title(self):
            pass
            
        @abstractmethod
        def set_title(self, title):
            pass

### 属性
* 私有属性
    self.__name 声明在类的构造函数中，派生类特别的访问方式self._A__name
* 保护属性
    self._name 声明在基类的构造函数中，派生类可以在类函数访问
* 公有属性
    self.name 声明在类的构造函数中
* 类的静态成员
    class.STATIC_PROPERTY 声明在类的结构定义中，与类方法同级
    
### 函数
* 构造函数

        def __init__(self, *args, **kwargs):
            pass

* 成员函数

        def function(self, *args, **kwargs):
            pass

* 类函数
        
        @classmethod
        def func(cls, *args, **kwargs):
            pass
            
* 静态函数
        
        @staticmethod
        def func(*args, **kwargs):
            pass

* 抽象函数（参见抽象类）

