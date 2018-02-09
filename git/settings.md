# Basic settings for daily work on GIT 

## Alias 
> Don't work in a machine without this minimum aliases configued

```bash
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.st status
git config --global alias.unstage 'reset HEAD --'
git config --global alias.last 'log -1 HEAD'
git config --global alias.visual "!gitk"
```