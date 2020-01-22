#!/usr/bin/env python3
import iterm2
import os
import subprocess

paths = [
    '~/Projects/Qissa/api-gateway/',
    '~/Projects/Qissa/dataset-handler/',
    '~/Projects/Qissa/qissa-creator/',
    '~/Projects/Qissa/user-control/',
    '~/Projects/Qissa/qissa-ui/',
]


async def tab(connection):
    app = await iterm2.async_get_app(connection)
    window = app.current_terminal_window
    if window is not None:
        await window.async_create_tab()
    else:
        print("No current window")

for x in paths:
    print(x)
    iterm2.run_until_complete(tab)
    os.chdir(x)
