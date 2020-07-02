# General 

* [How to contribute to a git project](https://git-scm.com/book/en/v2/Distributed-Git-Contributing-to-a-Project)
* Learn git in a [visual way](https://learngitbranching.js.org/)

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

## Commit range 

See what is in branchA that is not in master
```
git log master..branchA
```
See what is in master that is not in branchA (keep branch up to date)
```
git log branchA..master
```
if you want to see all commits that are reachable from refA or refB but not from refC
```
$ git log refA refB ^refC
$ git log refA refB --not refC
```

> [full doc](https://git-scm.com/book/en/v2/Git-Tools-Revision-Selection#_commit_ranges)

