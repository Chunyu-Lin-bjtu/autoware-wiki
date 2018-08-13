![Target Date](https://github.com/CPFL/Autoware/wiki/images_Release-Procedure/target-date.png)

To make a new release of Autoware, two due dates must be met. 

First, all the pull requests are due on the date that is one week before the merge date so that an interval of the review process for them can spend more than one week. This due date for pull requests is a reference. You are encouraged to make your pull requests as early as possible. Always earlier is better. Note that a huge pull request is not recommended and difficult to review. So try to make a moderate pull request at your best.

Second, all the functions provided by the merged pull requests must be tested. This test process is desired to take several days. Once the merged pull requests are sufficiently testedenough, a new release branch will be created. If some pull requests are mandatory for the new release but cannot be merged by itself, they will be cherry-picked after the merge.
