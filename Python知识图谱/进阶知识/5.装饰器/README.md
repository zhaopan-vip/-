# 装饰器
装饰器来源于函数的内部函数，我理解为参数定制的函数模板；
函数本身调用方式由函数名+参数组成，为了让函数附加更多通用的功能，定义一个装饰器包装源函数 - 实质上也是一个函数
我们可以称之为Wrapper函数，负责调用源函数+参数；
装饰器本身呢，也是声明为函数名+参数形式，内部函数是Wrapper调用源函数，这样起到扩展源函数功能实现；
另外由于装饰器本身也允许有参数，这样装饰器能实现一系列的类型功能。

# 示例代码
        from functools import wraps
        import logging
        
        def logged(level, name=None, message=None):
            """
            Add logging to a function. level is the logging
            level, name is the logger name, and message is the
            log message. If name and message aren't specified,
            they default to the function's module and name.
            """
            def decorate(func):
                logname = name if name else func.__module__
                log = logging.getLogger(logname)
                logmsg = message if message else func.__name__
        
                @wraps(func)
                def wrapper(*args, **kwargs):
                    log.log(level, logmsg)
                    return func(*args, **kwargs)
                return wrapper
            return decorate
        
        # Example use
        @logged(logging.DEBUG)
        def add(x, y):
            return x + y
        
        @logged(logging.CRITICAL, 'example')
        def spam():
            print('Spam!')
本质上是 decorate 返回一个可调用对象，它接受一个函数作为参数并包装它

# 参考资料：
<https://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p04_define_decorator_that_takes_arguments.html>