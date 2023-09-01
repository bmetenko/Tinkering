import numpy as np
from lets_plot import (
    LetsPlot, ggplot, geom_density,
    ggsize, scale_fill_brewer, theme,
    ggsave, aes, geom_text, geom_line,
    facet_wrap, geom_bar, geom_point,
    geom_lollipop
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
    # pass in custom values as well.
    geom_text(
        aes(x=[1, 2, 3], y=[1, 2, 3], label=['a', 'b', 'c']),
        nudge_x=0,
        nudge_y=-0.25,
        check_overlap=True,
        size=24,
    ) +
    geom_line(aes(x=[1, 2, 3], y=[1, 2, 3]), color='red') +
    geom_lollipop(aes(color='cond'), size=0.1, shape=22, fill='black') +
    geom_density(color='dark_green', alpha=.7) +
    scale_fill_brewer(type='seq') +
    theme(panel_grid_major_x='blank') +
    facet_wrap('cond', ncol=2)
)

ggsave(main_plot, filename="test_plot2.png")
