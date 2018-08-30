
### Merge Pull Request into Develop

![Merge Types](https://github.com/CPFL/Autoware/wiki/images_Maintainer-Rule/merge-types.png)

Using `Squash and merge` is generally preferable. `catkin_generate_changelog` puts all commit messages into CHANGELOG. Though `Squash and merge` wipes away all history on the pull request, it should be fine because a pull request should have only one matter. If `Create a merge commit` or `Rebase and merge` is selected, CHANGELOG will have a lot of junk messages.

A exception is that `Create a merge commit` should be selected for merging release branches into master or develop branch to keep the history among master, develop, and release branches.

Another exception is that `Create a merge commit`, `Squash and merge`, or `Rebase and merge` may be useful when some people are collaborating for one pull request. A example is to create a pull request for a feature branch.

![Commit Messages on Squash and Merge](https://github.com/CPFL/Autoware/wiki/images_Maintainer-Rule/commit-messages.png)

The second text box on `Squash and merge` that initially has all commit messages on the pull request should be deleted generally.  The strings in the first and second text boxes will be connected on the `Squash and merged` commit message. As a result, the string in the second text box will be junk in CHANGELOG.