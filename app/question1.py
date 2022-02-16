
class Question1:
    def __init__(self, h, b, w):
        self.h = float(h)
        self.w = float(w)
        self.b = float(b)

    def dropping(self):
        if self.h < 0:
            return -1
        if self.b >= 1 or self.b < 0:
            return -1
        if self.w > self.h:
            return -1

        counter = 1
        curr = self.h
        while True:
            #new height
            curr *= self.b
            if curr < self.w:
                break
            counter += 2
            
        return counter


if __name__ == '__main__':
    print(f"h=3;b=0.66;w=1.5; ans: {Question1(3, 0.66, 1.5).dropping()} times")
    print(f"h=3;b=0.8;w=1.5; ans: {Question1(3, 0.8, 1.5).dropping()} times")
    print(f"h=3;b=1.0;w=1.5; ans: {Question1(3, 1.0, 1.5).dropping()} times")


