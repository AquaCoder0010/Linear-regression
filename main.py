import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

## global variables
# don't ask me why I put the parameters globally.

p_0 = random.random() * 2;
p_1 = random.random() * 2;        

def cost(y, Y):
    return np.sum(np.pow(y - Y, 2));

def gradient(x, Y):
    # isn't this beautiful? few months in and I will forget how it works, lovely.
    return [ np.sum(2* x *(x * p_1 + p_0 - Y)), np.sum( 2 * (x * p_1 + p_0 - Y) ) ];

def main():
    inputCount = 40;

    # training-data.
    x = np.linspace(0, 5, inputCount);
    Y = 3 * x + 5 + np.random.randn(inputCount) * 0.5;

    # hyper-parameters (in this case there is only one)
    learningRate = 0.001;

    fig, ax = plt.subplots();
    ax.plot(x, Y, 'o');
    line, = ax.plot(x, x*p_1 + p_0);

    print(p_1, p_0);
    
    def update(frames):
        global p_1, p_0;
        p_1 -= learningRate*gradient(x, Y)[0];
        p_0 -= learningRate*gradient(x, Y)[1];
        line.set_ydata((x*p_1 + p_0));
        return line,;
        pass;
    ani = animation.FuncAnimation(fig, update, frames=100, interval=150, blit=False);
    plt.show();
    
    pass;

if __name__ == "__main__":
    main();
