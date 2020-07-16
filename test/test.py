class lei():#一类的函数可以分为一类
    def __init__(self, chushihua, chushihua2):
        self.chushihua = chushihua
        self.chushihua2 = chushihua2
    # 可以直接加程序,调用时执行
    lei = "lei"  # 这是一个属性,一个定义了的东西
    none = None  # 这是一个属性,还不确定是啥
    print(lei)
    def xingwei(self):#定义函数，行为,一定要有self(就是调用.前面的类)
        print(1+1)#函数干啥
    def xingwei2(self):
        print(chuanru+1)
        shuchu=0
        return shuchu  # 给一个值


class jichenglei(lei):#继承括号里的类,就是把那的代码复制到这个类
    def xinxingwei():
        print(chushihua)


class j chenglei2(lei):
    def __init__(self,zichushihua):
        super().__init__(chushihua, chushihua2)#加了这行才可以不被jichengleilei里的__init__吃掉父类的__init__
        jichenglie2.zichushihua=zichushihua
    def xinxingwei():
        print(chushihua)
class hunhe(jichenglei,jichenglei2):#把两个类混起来并啥都不做
    #两个父类里都有xinxingwei函数,他会继承写在前面的,就是jichenglei
    def __init__(self,xinzhanwei):
        hunhe.xinzhanwei=xinzhanwei
    pass
# 也可以不定义变量调用
lei(chushihua="shuru",chushihua2="shuru2").xingwei()
duixiang = lei(chushihua="shuru", chushihua2="shuru2")  # 类不能做任何事情，要把它落到实处
jichengduixiang = jichenglei(chushihua="shuru", chushihua2="shuru2")# 也需传入父类需要的参数
# 调用类的函数
duixiang.xingwei()
#改变了属性
lei.lei="gaibian"
lei.none="None"
mix=hunhe(xinzhanwei="new")
