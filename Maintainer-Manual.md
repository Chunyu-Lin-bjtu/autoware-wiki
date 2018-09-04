
### Merge Pull Request into Develop

![Merge Types](https://github.com/CPFL/Autoware/wiki/images_Maintainer-Rule/merge-types.png)

Using `Squash and merge` is often preferred. `catkin_generate_changelog` puts all commit messages into CHANGELOG. `Squash and merge` wipes away all the history of the pull requests, but this is fine because an individual pull request should  not be associated with multiple topics anyway. If `Create a merge commit` or `Rebase and merge` is applied, CHANGELOG would have a bunch of junk messages.

An exception is that `Create a merge commit` should be applied when merging the release branches into the master or develop branch, in order to keep the history among the master, develop, and release branches.

Another exception is that `Create a merge commit`, `Squash and merge`, or `Rebase and merge` is recommended when multiple contributors work together on a single pull request. For example, you may want to create a pull request for a feature branch.

![Commit Messages on Squash and Merge](https://github.com/CPFL/Autoware/wiki/images_Maintainer-Rule/commit-messages.png)

The second textbox on `Squash and merge`, which initially has all commit messages on the pull request, should be deleted generally.  The strings in the first and second textboxes will be associated with the `Squash and merged` commit message. As a result, the string in the second textbox will be a junk in CHANGELOG.