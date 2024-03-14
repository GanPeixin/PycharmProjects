import inspect
import asynciotest

async def async_fuc():
    pass
def regular_fuc():
    pass

print(inspect.iscoroutinefunction(async_fuc))   #判断是否支持异步
print(inspect.iscoroutinefunction(regular_fuc))