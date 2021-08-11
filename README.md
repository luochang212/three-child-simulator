# three-child-simulator

三孩模拟器：一款简单的文字冒险游戏，运用 Python 协程编写

PS: 好吧，其实是 n 孩模拟器

## 输出样例

```bash
Event(time=5, ident=0, name='上官家豪', gender='boy', action='出生')
Event(time=6, ident=0, name='上官家豪', gender='boy', action='嗷嗷待哺')
Event(time=7, ident=0, name='上官家豪', gender='boy', action='上托儿所')
    Event(time=7, ident=1, name='上官美玲', gender='girl', action='出生')
    Event(time=8, ident=1, name='上官美玲', gender='girl', action='嗷嗷待哺')
Event(time=9, ident=0, name='上官家豪', gender='boy', action='上幼儿园')
    Event(time=9, ident=1, name='上官美玲', gender='girl', action='上托儿所')
    Event(time=11, ident=1, name='上官美玲', gender='girl', action='上幼儿园')
Event(time=12, ident=0, name='上官家豪', gender='boy', action='上小学')
    Event(time=14, ident=1, name='上官美玲', gender='girl', action='上小学')
        Event(time=14, ident=2, name='上官依诺', gender='girl', action='出生')
Event(time=15, ident=0, name='上官家豪', gender='boy', action='上初中')
        Event(time=15, ident=2, name='上官依诺', gender='girl', action='嗷嗷待哺')
        Event(time=16, ident=2, name='上官依诺', gender='girl', action='上托儿所')
    Event(time=17, ident=1, name='上官美玲', gender='girl', action='上初中')
Event(time=18, ident=0, name='上官家豪', gender='boy', action='上高中')
        Event(time=18, ident=2, name='上官依诺', gender='girl', action='上幼儿园')
    Event(time=20, ident=1, name='上官美玲', gender='girl', action='上高中')
Event(time=20.9, ident=0, name='上官家豪', gender='boy', action='高考')
Event(time=21.0, ident=0, name='上官家豪', gender='boy', action='上大学')
Event(time=5, ident=0, name='上官家豪', gender='boy', action='上大学')
        Event(time=21, ident=2, name='上官依诺', gender='girl', action='上小学')
    Event(time=22.9, ident=1, name='上官美玲', gender='girl', action='高考')
    Event(time=23.0, ident=1, name='上官美玲', gender='girl', action='上大学')
    Event(time=7, ident=1, name='上官美玲', gender='girl', action='上大学')
        Event(time=24, ident=2, name='上官依诺', gender='girl', action='上初中')
        Event(time=27, ident=2, name='上官依诺', gender='girl', action='上高中')
        Event(time=29.9, ident=2, name='上官依诺', gender='girl', action='高考')
        Event(time=30.0, ident=2, name='上官依诺', gender='girl', action='上大学')
*** end of simulation time: 1 event(s) pending ***
```

## 注意

Python version >= 3.7

## 声明

灵感来自：微博@小可妮Cony

![](/img/weibo_screenshot.jpeg)
