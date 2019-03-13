This page describes how to contribute to the development of Autoware.
It contains both guidelines that should be followed and rules that must be followed.

# Communication

Before starting a new contribution, it is important to let the community know what you plan on doing.
This serves several purposes.

1. It lets everyone know that you are going to start work on a feature or bug fix so that no one else does the same and duplicates your effort.
1. It lets anyone who may already be working on the feature or bug fix know you intend to work on it, so they can tell you and you don't duplicate their effort.
1. It gives others a chance to provide more information about what the feature or bug fix might need or how it may need to be implemented.

Join the [Autoware Discourse](https://discourse.ros.org/c/autoware) and start a new topic introducing yourself and explaining what you want to work on.

If you are so inclined, join the [Autoware Slack chat server](https://autoware.herokuapp.com/).
This provides a place to have a quick chat to other Autoware users or developers.


# Development workflow

The Autoware development workflow is based on these principles:

- Everyone owns the code.
  No one person is responsible for maintaining a part of the code, nor does any one person have absolute control over how a part of the code is implemented and managed.
  These sorts of decisions are arrived at by discussion amongst the community and consensus.
- Everyone works on everything at some point.
  If there is a feature or bug fix issue waiting to be developed, take it on.
  Trying to implement in parts of your code outside of your comfort zone will expand your experience and make you an increasingly valuable contributor, as well as give you the knowledge to help others who run into problems.
- Be open about problems and be open to suggestions.
  When you run into a hurdle implementing a new feature or a bug fix, showing your code as it currently is and asking for help will get you advice that will get you over that problem faster than worrying about it yourself.
  Use Discourse, file an issue, or ask in the Autoware Slack chat.
  Similarly, when you receive a suggestion on how to better implement something, take that suggestion on board.
  This is especially important during pull request reviews.
  Everyone is on the same side and thinking about the quality of the final code.

You will need a GitHub account to contribute to Autoware.
To make a new contribution, you will first need to fork the repository into your own account.
Following that, you can create a new branch in your forked repository for your new feature or bug fix and make a pull request from there once you have finished developing it.
See the sections below for more detail on the steps involved.

If you are not familiar with Git or any of its more complex features such as rebasing commits and merging branches, then read the relevant chapters from the [Pro Git SCM book](https://git-scm.com/book/en/).


## Starting a new feature or bug fix

1. Design your new feature or bug fix.
   Describe in as much detail as possible how you will implement it, and how it will behave.
   If it is a bug fix, describe why you believe the bug will be corrected.
   The more detailed your design, the greater the chance your implementation will be accepted at the pull request review stage.
   If you can, it often helps to have semi-formal or formal models of your intended design's behaviour and structure.
1. Communicate your attentions to the Autoware community (see [[#communication]], above).
1. If you have not done so already (such as for a previous feature or bug fix you developed), [fork the Autoware repository](https://guides.github.com/activities/forking/).
1. In your new fork, create a new branch by clicking the `Branch: master` button at the top left, above the list of source files and entering the name for the new branch to create.
   **Important:** Make sure your branch begins from the `master` branch of Autoware, not another feature or bug fix branch, unless someone from the community directs you to do otherwise.
1. Clone your fork of Autoware to your computer and then check out the branch you have created.
1. Begin developing your feature or bug fix. Make as many commits as you feel necessary during the development.
   Be sure to include the [Developer Certificate of Origin](https://developercertificate.org/) [sign-off line](https://github.com/probot/dco) in your commit messages.
   - If you are committing from the command line, pass the `-s` or `--signoff` option to `git commit` to have the sign-off line automatically added to your commit message.
     Be aware that this implies your agreement with it.
   - You can add the sign-off manually by adding the following line to your commit message: `Signed-off-by: Your Name <your.email@example.com>`
1. While working, always build with all tests enabled and run the tests locally before considering your work complete.
1. Once your feature or bug fix is complete, make a pull request.
   Consider running [style guide checkers](#coding-style) checkers and static analysis tools such as [cppcheck](http://cppcheck.sourceforge.net/) before making your pull request to catch common errors in advance.
   These tools will be run automatically on your pull request but fixing errors after making the request will slow down the review process and make others treat your contribution more strictly.


## Making a pull request

1. Before making a pull request, make sure to read the pull request review guidelines to understand what conditions your pull request must meet to be acceptable.
1. Before making a pull request, run the tests locally to ensure your additions are not going to break anything.
1. To make a pull request, first [push your commits](https://guides.github.com/activities/forking/) from your local copy to your fork of the Autoware repository on the GitHub servers.
1. Go to the GitHub page for your Autoware fork and select the branch where your new feature or bug fix has been developed.
1. GitHub will automatically detect the changes and offer to make a pull request.
1. When you make the pull request, fill out the pull request template.
   Provide as much detail about the purpose of the pull request as possible.
   Include all the design documentation to produced before you started to work on the implementation.
   If you are implementing a feature or bug fix for which there is an existing issue on the issue tracker, make sure to [include the issue number in your pull request comments](https://help.github.com/en/articles/closing-issues-using-keywords) using text such as "Fixes #42" or "Resolves #42".
   When giving your pull request a title, do not start the name with tags such as `[Feature]` or `Fix/`. Use [issue labels](#issue-labels) instead to indicate what type of pull request it is.
1. If you know of a contributor who is suitable to review your pull request, [request a review from them](https://help.github.com/en/articles/requesting-a-pull-request-review).
   This step is optional.


## Pull request review guidelines

For a pull request to be acceptable to merge, it must receive at least one favourable review from another member of the Autoware community.
It must also not have any negative reviews that have not been resolved through further development or discussion.

Anyone is welcome to perform a pull request review and all comments from all reviews must be considered and answered appropriately to be considered resolved.

A pull request review will look at all aspects of the pull request.

- Documentation
  - Does the pull request include user guide documentation describing how to use the feature (for new features)?
  - Does the pull request include API documentation for all functions, especially public functions, and for any other public-facing parts of the API such as classes, structures, etc.?
  - Has the design been verified in some way?
- Source code
  - Does new code and changed code comply with the style guide?
  - Are any new or changed APIs well-designed and do they match the style of the surrounding API?
  - Is the code easy to read and understand, and is it easy to maintain?
    Fancy coding may impress your friends but it gets pull requests rejected.
  - Is any new source code, including file system layout, well-structured and following best practices?
- Tests
  - Does the pull request include sufficient tests to achieve maximum practical coverage of the new code and any existing code that was changed?
    Is this proven by a coverage report from the CI pipeline?
  - Do the tests cover all known edge and corner cases for using the new and changed code?
  - Do all Continuous Integration pipelines pass for all supported platforms?
    The CI pipelines check not just behaviour but also check things like coding and documentation style and perform static analysis.
  - If appropriate, have simulated or real-world integration tests been performed?
- Other aspects
  - Each pull request should focus only on one change.
    That change should be as small as practical to make accurate reviews easier.
    Other developers are more likely to perform short reviews of simple pull requests that they can understand from reading the changes, than to spend hours reviewing a pull request that changes dozens of files in significant ways.
  - Does the pull request make more changes than necessary to satisfy the feature or bug fix it targets?
  - Does the pull request reference any related issues or pull requests?
  - Can the pull request be merged independent of any other pull requests?
    This is not an absolute requirement because sometimes multiple pull requests are needed for a complex feature, but in the majority of cases if your pull request requires other pull requests to be merged first, it will be looked at very intensively and may not be accepted.
    If you are developing a separate feature that requires another feature still in review, consider waiting for that feature to be merged before making your own pull request.
  - Have all comments on the pull request been addressed satisfactorily?
  - Have the commits been signed for the [Developer Certificate of Origin](https://developercertificate.org/)?

While performing the review, feel free to suggest changes to the code and documentation.
If you are the person requesting the review, [enable edits from upstream contributors](https://github.blog/2016-09-07-improving-collaboration-with-forks/) to speed up the review and improvement process.
If you are a particularly dedicated reviewer, fork the repository that the pull request came from and make more substantial changes.
Mention the original pull request in your commit message to get your changes added automatically, or if they are changes that require discussion, open a pull request against the original pull request.

In general, we prefer code reviews to be performed by someone who is distant from the new code.
This means not getting someone who helped you develop it to do the review, but rather asking for a review from someone else who has contributed to Autoware before.
If you do not know who to request a review from, then do not request anyone and the [Highfive bot](https://github.com/rust-lang-nursery/highfive) will randomly choose someone to assign from a list of known contributors.

Sometimes the maintainers will ask for reviews from additional contributors.
This is not an indication that the other reviews were bad or that the contribution is bad, but is usually a sign that the feature or bug fix is considered particularly critical.

Once a pull request has passed review, it will be merged into the main Autoware repository by one of the maintainers.
After this is done you are free to delete the branch you used to develop it in your own fork of the Autoware repository.
We recommend you do so to avoid accidentally developing new contributions from that branch rather than from the tip of the Autoware repository.

However, a pull request cannot be merged until at least 48 hours have passed since the pull request was made.
This gives others a chance to comment on the pull request before it gets merged.
Similarly we prefer that a pull request not be merged until some time has elapsed since the last review was made.
This is to give others time to respond to a review with potentially opposing opinions.
24 hours since the last review is the current guideline.

Remember, if you want your pull request merged rapidly then you should communicate your intentions to the community before you begin working.
By doing so, you will ensure that everyone interested already knows what is going on when your pull request arrives.


## Merging guidelines

If you are a maintainer, you are responsible for merging accepted pull requests into the master branch.
In general there is not much involved in this work.
When merging a pull request, make sure to follow these guidelines.

- Read over the pull request's description and discussion, and ensure that there are no outstanding issues with the request.
- Look over the reviews to ensure they comply with the pull request review guidelines.
  In particular, keep an eye out for major problems such as unrelated changes included in the pull request, or a missing DCO sign-off line, or incomplete CI runs.
- If the pull request comes from outside the Autoware organisation, then a maintainer is responsible for running the CI jobs necessary to check if the pull request can be merged.
  CI must be run on all officially supported platforms.
- Don't merge pull requests until at least 48 hours have elapsed since the request was made, 24 hours have elapsed since the last review was made, and all comments have been addressed satisfactorily.
- When performing the merge, squash the commits into as small a number of commits as reasonable.
  This is done to keep the repository history clean.
- If the pull request came from a branch on the Autoware repository, rather than from a fork, delete the branch once it has been merged.


# Coding style

For contributions to Autoware.AI, choose the style guide appropriate to your contribution.
In many cases, there are tools available that can check your code and documentation.

- For code that is using ROS 1:
  - For C++ code, follow the [ROS C++ style guide]().
    You can use [this configuration](https://github.com/davetcoleman/roscpp_code_format) for the [clang-format tool](https://clang.llvm.org/docs/ClangFormat.html) to automatically format your code correctly.
    Consider also using tools such as [cpplint](https://github.com/cpplint/cpplint) to identify additional potential problems.
  - For Python code, follow the [ROS Python style guide](http://wiki.ros.org/PyStyleGuide).
    Use the [flake8 tool](http://flake8.pycqa.org/en/latest/) to check your code before making a pull request.
    Additionally, all Python code for ROS 1 should be usable in both Python 2.7 and Python 3.
- For code that is using ROS 2, or does not use ROS, follow the [appropriate ROS 2 style](https://index.ros.org/doc/ros2/Contributing/Developer-Guide/#language-versions-and-code-format) for the language your code is written in.


# Documentation style

All contributions should come with complete documentation.
Poor documentation is just as likely to get a pull request rejected as poor code.
All documentation must comply with the appropriate style guide.

For user guide documentation, we use [ReadTheDocs](https://readthedocs.org/), which means using Sphinx to write the documentation.
Consult the [Sphinx documentation](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html) for how to write documentation using this tool.
In general, follow the Markdown format and provide detailed documentation.

For documenting C++ code, we do not currently have a style guide.
Follow the style of the existing code surrounding your contribution.

For documenting Python code, follow [PEP 257](https://www.python.org/dev/peps/pep-0257/).
Use the [pep257](https://pypi.org/project/pep257/) tool to confirm your documentation complies.


# Development management


## Repository guidelines

The Autoware.AI repository is structured around a single master branch.
It follows the [OneFlow branching model](https://www.endoflineblog.com/oneflow-a-git-branching-model-and-workflow).
However, for merging branches into the master branch we use a rebase-and-squash approach.
This allows features to be developed using a large number of commits in a separate branch or fork, while still allowing the final result to be presented in one or a small number of commits in the history of the master branch.

The master branch must always compile without warnings and all tests must always pass.
It must always be in a usable state.
This implies that any pull request must do the same before it can be merged, and that features must be completed before they are merged.

If a branch is created in the main Autoware repository, then it should be deleted once merged unless there is a good reason for keeping it around, and that reason is discussed and agreed upon by other contributors.
We recommend that you treat branches in your own fork in the same way, however this is not required nor enforced in any way.

When releases are made, the head of the release branch is tagged and the branch is deleted.
This reduces the number of branches while still providing a known point (the tag) to start version-specific bug-fix branches from.
Major releases, minor releases and hot-fix releases are all treated in this way.


## Milestones

Autoware.AI uses [GitHub milestones](https://github.com/CPFL/Autoware/milestones) to manage the roadmap and the features targeted for each release.
Each issue is either targetted at an upcoming milestone, which means it is due to be included in that release, or it is not assigned to any milestone, which means that it is not currently on the roadmap for release.

If you feel that a feature or bug fix should be included in an upcoming release, make a comment on the relevant issue stating which release you think it should be in and why.
Stating why you feel this way is important; requests for an issue to be included in a release without any justification are likely to be ignored.
If you feel particularly strongly about a feature being released soon and have the development skills, implementing the feature and making a pull request may get it included in the upcoming release, or the one after if the upcoming release is too close.


## Issue labels

Issues and pull requests are [tagged with labels](https://github.com/CPFL/Autoware/labels) that describe their current step in the development process, as well as additional aspects such as needing more information from the original reporter.
See the [labels page](https://github.com/CPFL/Autoware/labels) for a list of labels used and their meaning.

If you are new to Autoware and looking for a feature or bug-fix to implement, look for those that have the [Good first issue](https://github.com/CPFL/Autoware/labels/Good%20first%20issue) label.

If you are filing a new issue or making a pull request, use either the `Bug` label, for bug reports and bug fixes, or the `Enhancement` label, for new or improved features and feature requests. Do not add any labels that are identified in their description as being a Kanban column. The maintainers will add these as appropriate when initially processing the issue.


## Task (Kanban) board

Autoware.AI uses a [Kanban-style task board](https://github.com/orgs/CPFL/projects/1) to visually manage issues.
The board has the following columns.

- Backlog: Features and bug reports not currently assigned to a release.
  These may be done in a future release, or they may not, depending on need and available development resources.
- Do for next release: Contains the tasks that are queued up for the next release milestone.
  This means that the issues are ready to begin development.
  To make it to this column, a feature request or bug report cannot be waiting for more information or for another feature that is not queued up for the same or an earlier milestone.
  If you are looking for features or bug fixes to implement, start in this column.
- In progress: The feature or bug fix is being worked on by someone.
  Trying to do this yourself now would be duplicating effort.
- In review: A pull request for the feature has been received and it is going through the review process.
  This may include making major changes.
- Done: The task associated with the card is complete.
  For feature requests and bug reports, the feature or bug fix has been merged.