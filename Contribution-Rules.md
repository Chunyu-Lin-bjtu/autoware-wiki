**You must follow the rules described below when you contribute to Autoware.**
Please read the following carefully before you start coding.
Thank you for your time.

## To Begin With

Please join Autoware Slack at [https://autoware-developer.slack.com/](https://autoware-developer.slack.com/) and say hello to the community. You can also post your message on Autoware Googlegroups at [autoware@googlegroups.com](mailto:autoware@googlegroups.com). To subscribe Autoware Googlegroups, please click the "Apply to Join Group" button at [https://groups.google.com/d/forum/autoware](https://groups.google.com/d/forum/autoware). If you don't have a Google account, please instead send an email to [autoware+subscribe@googlegroups.com](mailto:autoware+subscribe@googlegroups.com). To contribute, apparently, you need to create a GitHub account if you don't have one yet: [[Join GitHub](https://github.com/join)].

## Development Workflow

To assure traceablity in our code we follow this development process:
* If you are working on a feature/modify-node, create an issue first
* Create a branch, work on the feature/modify-node, refer in at least one commit to the issue #number
* Open a pull request for the given feature/modify-node and fill out the pull request template. 

This will assure that we know where the feature originated from and the implementation will be linked to the feature request (or bug report). Otherwise there is absolutely no traceability.
Secondly, with the pull request template it will be easier for the reviewer(s) to understand the changes and we can later on convert "Steps to Reproduce" into integration tests.

## Branching Model

In order to keep efficient open-source development of Autoware, we ask all developers to comply with the branching model described below.
On this model, we maily use six branches - master, develop, feature, release, experimental, and hotfix.

### master

This is the latest stable version of Autoware.

### develop and feature

In general, developers should NOT work on the "develop" branch.
When you develop new functions, please check out a new branch, "feature/[branch_name]", from the "develop" branch, and modify the code there.
After the modificaiton, please send a pull request to the "develop" branch.

### release

This situation is true of only the persons in charge of releasing Autoware.
Once we complete some major development, we make a new release.
For the release work, please checkout a new branch, "release/[1.xx.yy], from the "develop" branch, and modify the code there.
After the modification, please send a pull request: "xx" in version of release/[1.xx.yy] is increased when checked out from the "develop" branch, and yy is also increased when bug fixes are done.
Finally, we merge this branch to the master branch, attaching a version tag.

### experimental

If your contribution is not a new feature but is to change one of the existing branches, please checkout a new branch, "experimental/[branch_name]", from the corrensponding branch. Please discuss with other contributions if this change can be merged to the original branch.

### hotfix

If we encounter bugs in the "master" branch after the release, we check out the "hotfix" branch from the "master" branch and fix the bugs there.
This branch is merged to each corresponding branch - master, release, and develop.
After the merge, the version of the master and the release branches is increased.

Reference for the git-flow model
- http://nvie.com/posts/a-successful-git-branching-model/

## Pull Request

1. A design article should be posted for every feature or bug. 
1. Every feature/bug implementation needs to be thoroughly reviewed (at least two reviewers).
1. A unit test program needs to be submitted so that the reviewers or others can check if the implementation logic is correct.
1. an integration test  
4. If applicable we also write a SIL test (with data or simulation) and 
5. HIL test. 
6. For all the tests we also compute coverage (using gcov) so we know which code gets tested and how often. 
7. In addition we use coverity and PClint and cppcheck to run static code analysis. 
8. We also run cpplint for style enforcement. 
9. Now running of all of this is automated through gitlab CI and we have regular Debian and docker release for intel64, qnx and ARM64.

## Branching Model

YYY

## Coding Standards

ZZZ

[[Home](https://github.com/CPFL/Autoware/wiki/)]
[[Next >>](https://github.com/CPFL/Autoware/wiki/Installation)]