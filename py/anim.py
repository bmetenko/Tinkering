import pandas as pd
import numpy as np
from plotnine import *
from plotnine.animation import PlotnineAnimation
import matplotlib.animation
from matplotlib import rc

rc('animation', html='html5')
n = 200
tightness = 1.05
k_min = 1
k_max = 5
num_frames = 100
theta = np.linspace(-0.85 * np.pi, 0.85 * np.pi, n)


def plot(k):
    # For every plot we change the theta
    _theta = theta*k ** 2

    # Polar Equation of each spiral
    r = tightness*_theta

    df = pd.DataFrame({
        'theta': _theta,
        'r': r,
        'x': r*np.sin(_theta)*r,
        'y': r*np.cos(_theta) ** (1/(np.cos(_theta) + 1))
    })

    p = (
            ggplot(df)
            + geom_path(
                aes('x', 'y', color='theta'),
                size=1,
                show_legend=False
            )
            + lims(
                x=(-50, 50),
                y=(-25, 25),
                color=(-k_max * np.pi, k_max * np.pi)
            )
            + theme_void()
            + theme(
                aspect_ratio=1,
                legend_position=None
            )
    )
    return p

plots = (plot(k) for k in np.linspace(k_min, k_max, num_frames))
ani = PlotnineAnimation(plots, interval=100, repeat_delay=0)
ani.save('test2.gif')
