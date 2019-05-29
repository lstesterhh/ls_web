

def chigutou(a="狗"):
    print("%s吃骨头"%a)


class DooShi(object):
    def chigutou(self):
        print("吃骨头")

    def luanpao(self):
        print("吓跑")

if __name__ == '__main__':
    dogshili=DooShi()
    dogshili.chigutou()
    chigutou()