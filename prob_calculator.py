import random
import copy

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    hat = hat
    expected_balls = expected_balls
    num_balls_drawn = num_balls_drawn
    num_experiments = num_experiments
    as_expected_event = 0
    y = copy.copy(num_experiments)
    pick_list = []
    while y > 0:
        picked = hat.draw(num_balls_drawn)
        expected_balls_copy = copy.copy(expected_balls)
        x = 0
        for item in picked:
            if item in expected_balls_copy:
                expected_balls_copy[item] -= 1
        for key in expected_balls_copy:
            x += expected_balls_copy[key]
        if x == 0:
            as_expected_event += 1
        y -= 1
    return as_expected_event/num_experiments


class Hat:
    def __init__(self, **balls):
        self.hat = balls
        self.contents = []
        self.used_balls = []
        for key in self.hat:
            i = self.hat[key]
            while i > 0:
                self.contents.append(key)
                i -= 1

    def draw(self, number):
        num_of_balls = number
        picked_balls = []
        # Drawing event
        while num_of_balls > 0:
            if num_of_balls < len(self.contents):
                random_ball = random.choice(self.contents)
                self.contents.remove(random_ball)
                picked_balls.append(random_ball)
                self.used_balls.append(random_ball)
            elif num_of_balls > len(self.contents):
                for ball in self.used_balls:
                    self.contents.append(ball)
                    self.used_balls.remove(ball)
                break
            num_of_balls -= 1
        return picked_balls
