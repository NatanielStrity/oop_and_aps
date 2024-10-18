class Pyramid:

    def __init__(self, max_h):
        self.max_h = max_h
        self.bricks_count = 0
        self.hight = 0


    
    def add_bricks(self, num_bricks):
         if num_bricks > self.max_h - self.height:
             print('ошибка!!!')
             self.bricks_count += num_bricks
        while self.bricks_count >= self.height + 1:
            self.height += 1
            self.bricks_count -= self.height

    def get_height(self, hight):
        



    def is_done(self):
         self.hight
        


class Builder:

    def __init__(self, bricks):
        self.bricks = bricks
        self.my_pyramid = Pyramid(15)

    
    def buy_bricks(self):
        self.bricks = 15


    def build_pyramyd(self):
         self = sum_bricks


    def work_day(self):



