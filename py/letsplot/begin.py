import numpy as np
from lets_plot import (
    LetsPlot, ggplot, geom_density,
    ggsize, scale_fill_brewer, theme,
    ggsave, aes, geom_histogram,
    facet_wrap, geom_bar, geom_point
)

LetsPlot.setup_html()

np.random.seed(555)

data = dict(
    cond=np.repeat(['A', 'B'], 250),
    rating=np.concatenate(
        (
            np.random.normal(0, 1, 250),
            np.random.normal(1, 2, 250)
        )
    ),
    skew=np.concatenate(
        (
            np.random.normal(-1, 1, 250),
            np.random.normal(-1, 1, 250)
        )
    )
)

main_plot = (
    ggplot(
        data, aes(x='rating', y='skew', fill='cond')
    ) +
    ggsize(700, 300) +
    geom_bar() +
    geom_point() +
    geom_density(color='dark_green', alpha=.7) +
    scale_fill_brewer(type='seq') +
    theme(panel_grid_major_x='blank') +
    facet_wrap('cond')
)

ggsave(main_plot, filename="testplot2.png")
