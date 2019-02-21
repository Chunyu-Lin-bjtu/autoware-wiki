![Target Date](https://github.com/CPFL/Autoware/wiki/images_Release-Procedure/target-date.png)

To make a new release of Autoware, two due dates must be met. 

First, all the pull requests are due on the date that is one week before the merge date so that an interval of the review process for them can spend more than one week. This due date for pull requests is a reference. You are encouraged to make your pull requests as early as possible. Always earlier is better. Note that a huge pull request is not recommended and difficult to review. So try to make a moderate pull request at your best.

Second, once the pull requests are merged, a new release branch will be created. All functions must be tested on the release branch. This test process is desired to take several days. After the release branch is sufficiently tested, a new release will be announced.

### Release Schedule
| Version | Pull Request | Merged | Release |
|-----------|------------|------------|------------|
| [v1.11](https://github.com/CPFL/Autoware/issues/1813) | Feb. 28th, 2019 | Mar. 7th, 2019 | Mar. 14th, 2019 |