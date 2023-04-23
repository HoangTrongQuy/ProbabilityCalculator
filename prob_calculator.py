import collections
import copy
import random
from itertools import product


class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            for i in range(count):
                self.contents.append(color)

    def draw(self, number_give_ball):
        total_ball = len(self.contents)
        if number_give_ball >= total_ball:
            return self.contents
        else:
            lst_ball = random.shuffle(self.contents)
            lst_ball = random.sample(self.contents, k=number_give_ball)
            for ball in lst_ball:
                self.contents.remove(ball)
            return lst_ball

    def show(self):
        return self.contents

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):

    num_test = 0

    for i in range(num_experiments):

        hat_copy = copy.deepcopy(hat.contents)

        lst_given = hat.draw(num_balls_drawn)

        counts = collections.Counter(lst_given)

        flag = True
        for color, count in expected_balls.items():
            if counts[color] < count:
                flag = False
                break
        if flag:
            num_test += 1

        hat.contents = hat_copy

    probality = num_test/num_experiments

    return probality



# arr = [1, 2, 1, 3, 4, 5]
# arr1 = copy.deepcopy(arr)
# arr.remove(1)
# # print(arr2)
# print(arr1)