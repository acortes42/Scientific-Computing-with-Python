import random
import copy

class Hat:

    def __init__(self, **balls):

        self.contents = []
        for x, y in balls.items():
            self.contents += [x] * y
        
    def draw(self, num):

        x = 0
        arr = []

        random.seed(a=None, version=2)

        if(num > len(self.contents)):
            return self.contents
        for i in range(num):
            x = random.randrange(len(self.contents))
            arr.append(self.contents[x])
            self.contents.pop(x)
        return arr

def experiment (hat, expected_balls, num_balls_drawn, num_experiments):

    expected_failture = 0

    for i in range(num_experiments):
        cp_hat = copy.deepcopy(hat)
        draw_list = cp_hat.draw(num_balls_drawn)
        for x, y in expected_balls.items():
            if draw_list.count(x) < y :
                expected_failture += 1  
                break
    return 1 - expected_failture / num_experiments


        

def main():

    my_hat = Hat(blue=3,red=2,green=6)
    print(experiment(hat=my_hat, expected_balls={"blue":2, "green":1}, num_balls_drawn=4, num_experiments=100000))

    hat2 = Hat(yellow=5, red=1, green=3, blue=9, test=1)
    print(experiment(hat = hat2, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn = 20, num_experiments = 100))
    return (1)

if __name__ == "__main__":
    main()

    
