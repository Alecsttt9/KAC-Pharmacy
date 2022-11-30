def states():
    grid = SQLFORM.grid(db.states)
        return dict(grid=grid)