## Tmux summary
1. Installation in osx `brew install osx`.
2. Start `tmux`
3. Split panes into left and right `C-b %`
4. Navigating panes `C-b <arrow key>`. It can be configured to Alt + <arrow key> using the following in .tmux.conf  
	bind -n M-Left select-pane -L
	bind -n M-Right select-pane -R
	bind -n M-Up select-pane -U
	bind -n M-Down select-pane -D
5. Exit a pane `exit`
