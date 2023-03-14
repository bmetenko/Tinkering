import plotly.graph_objects as go

fig = go.Figure()

tasks = [
    dict(Task="Task 1", Start='2023-01-01', Finish='2023-01-31'),
    dict(Task="Task 2", Start='2023-01-15', Finish='2023-02-28'),
    dict(Task="Task 3", Start='2023-03-01', Finish='2023-03-31')
]

colors = {
    'Task 1': '#12F456', 
    'Task 2': '#F54321', 
    'Task 3': '#1F3054'
    }

for i, task in enumerate(tasks):
    fig.add_trace(
        go.Scatter(
            x=[
                task['Start'], task['Finish']
            ], 
            y=[i, i], 
            mode='lines',
            line=dict(
                    color=colors[task['Task']], 
                    width=20
                ),
            hoverinfo='text', 
            text=task['Task']
        )
    )

fig.update_layout(
    xaxis_title='Date', 
    yaxis_title='Task'
    )

fig.show()
