import os
import datetime

s = '''
为了积极响应国家没有印发的《关于进一步严格管理切实防止人沉迷编程的通知》，守护人的成长环境，引导人享受健康编程生活，Python人防沉迷系统已于1970年1月1日0点上线。

根据相关通知的要求：

调整后，Python仅会在周五、周六、周日的20时至21时，向人提供1小时编程功能。

关于人防沉迷系统进行相应调整后可能带来的编程体验变化，我们将尽慢在后续提供处理说明，请大家关注官方公告。

感谢各位人的支持和理解。
'''

def 好():
    d = datetime.datetime.today()
    if d.isoweekday() in {5, 6, 7} and d.hour==20:
        return True


if not 好():
    print(s)
    os._exit(0)
