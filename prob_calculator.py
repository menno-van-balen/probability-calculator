import copy
import random


class Hat:
    def __init__(self, **balls):
        self.contents = list()
        for color, value in balls.items():
            for i in range(value):
                self.contents.append(color)

    def draw(self, number):
        if number >= len(self.contents):
            return self.contents
        else:
            copy_contents = copy.copy(self.contents)
            result_draw = list()
            for i in range(number):
                x = random.randint(0, len(copy_contents) - 1)
                result_draw.append(copy_contents[x])
                copy_contents.remove(copy_contents[x])
            return result_draw


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hit_count = 0
    for times in range(num_experiments):
        result_exp = copy.copy(expected_balls)
        result_draw = hat.draw(num_balls_drawn)
        # print('result:', result_draw)
        for ball in result_draw:
            if ball in result_exp:
                result_exp[ball] -= 1
            else:
                result_exp[ball] = -1
        # print(result_exp)
        miss_count = 0
        for value in result_exp.values():
            if value > 0:
                miss_count += 1
        if miss_count < 1:
            hit_count += 1
    probability = hit_count / num_experiments
    print('hit_count:', hit_count, 'probability:', probability)
    return probability


# hat = Hat(yellow=3, green=1, blue=2)
# print(hat.contents)
# print(hat.draw(2))

# experiment(hat, {'green': 1, 'yellow': 1}, 4, 3000)
# experiment(hat=hat, expected_balls={
#            "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=10000)


# THIS VERSION PASSES ALL TESTS (different in when to copy...)
# class Hat:
#     def __init__(self, **balls):
#         self.contents = list()
#         for color, value in balls.items():
#             for i in range(value):
#                 self.contents.append(color)

#     def draw(self, number):
#         if number >= len(self.contents):
#             return self.contents
#         else:
#             result_draw = list()
#             for i in range(number):
#                 x = random.randint(0, len(self.contents) - 1)
#                 result_draw.append(self.contents[x])
#                 self.contents.remove(self.contents[x])
#             return result_draw


# def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
#     hit_count = 0
#     for times in range(num_experiments):
#         copy_hat = copy.deepcopy(hat)
#         result_exp = copy.copy(expected_balls)
#         result_draw = copy_hat.draw(num_balls_drawn)
#         # print('result:', result_draw)
#         for ball in result_draw:
#             if ball in result_exp:
#                 result_exp[ball] -= 1
#             else:
#                 result_exp[ball] = -1
#         # print(result_exp)
#         miss_count = 0
#         for value in result_exp.values():
#             if value > 0:
#                 miss_count += 1
#         if miss_count < 1:
#             hit_count += 1
#     probability = hit_count / num_experiments
#     # print('hit_count:', hit_count, 'probability:', probability)
#     return probability


# hat = Hat(yellow=3, green=1, blue=2)
# print(hat.contents)
# print(hat.draw(2))

# experiment(hat, {'green': 1, 'yellow': 1}, 4, 20)
# experiment(hat=hat, expected_balls={
#            "blue": 2, "green": 1}, num_balls_drawn=4, num_experiments=10000)
