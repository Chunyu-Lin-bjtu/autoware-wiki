**You must follow the rules described below when you contribute to Autoware.**
Please read the following carefully before you start coding.
Thank you for your time.

## To Begin With

Please join Autoware Slack at [https://autoware-developer.slack.com/](https://autoware-developer.slack.com/) and say hello to the community. You can also post your message on Autoware Googlegroups at [autoware@googlegroups.com](mailto:autoware@googlegroups.com). To subscribe Autoware Googlegroups, please click the "Apply to Join Group" button at [https://groups.google.com/d/forum/autoware](https://groups.google.com/d/forum/autoware). If you don't have a Google account, please instead send an email to [autoware+subscribe@googlegroups.com](mailto:autoware+subscribe@googlegroups.com). To contribute, apparently, you need to create a GitHub account if you don't have one yet: [[Join GitHub](https://github.com/join)].


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