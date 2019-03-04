This page describes how to contribute to the development of Autoware.
It contains both guidelines that should be followed and rules that must be followed.

This page is under construction.

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
- 

You will need a GitHub account to contribute to Autoware.
To make a new contribution, you will first need to fork the repository into your own account.
Following that, you can create a new branch in your forked repository for your new feature or bug fix and make a pull request from there once you have finished developing it.
See the sections below for more detail on the steps involved.

## Starting a new feature or bug fix

1. Design your new feature or bug fix.
   Describe in as much detail as possible how you will implement it, and how it will behave.
   If it is a bug fix, describe why you believe the bug will be corrected.
   The more detailed your design, the greater the chance your implementation will be accepted at the pull request review stage.
   If you can, it often helps to have semi-formal or formal models of your intended design's behaviour and structure.
1. Communicate your attentions to the Autoware community (see [[Communication]], above).
1. If you have not done so already (such as for a previous feature or bug fix you developed), [fork the Autoware repository](https://guides.github.com/activities/forking/).
1. In your new fork, create a new branch by clicking the `Branch: master` button at the top left, above the list of source files and entering the name for the new branch to create.
   **Important:** Make sure your branch begins from the `master` branch of Autoware, not another feature or bug fix branch, unless someone from the community directs you to do otherwise.
1. Clone your fork of Autoware to your computer and then check out the branch you have created.
1. Begin developing your feature or bug fix. Make as many commits as you feel necessary during the development. Be sure to [include the DCO sign-off line](https://github.com/probot/dco) in your commit messages.
1. Once your feature or bug fix is complete, make a pull request.
   Consider running [style guide checkers](#codingstyle) checkers and static analysis tools such as [cppcheck](http://cppcheck.sourceforge.net/) before making your pull request to catch common errors in advance.
   These tools will be run automatically on your pull request but fixing errors after making the request will slow down the review process and make others treat your contribution more strictly.


## Making a pull request

1. To make a pull request, first [push your commits](https://guides.github.com/activities/forking/) from your local copy to your fork of the Autoware repository on the GitHub servers.
1. Go to the GitHub page for your Autoware fork and select the branch where your new feature or bug fix has been developed.
1. GitHub will automatically detect the changes and offer to make a pull request.
1. When you make the pull request, fill out the pull request template.
   Provide as much detail about the purpose of the pull request as possible.
   Include all the design documentation to produced before you started to work on the implementation.
   If you are implementing a feature or bug fix for which there is an existing issue on the issue tracker, make sure to [include the issue number in your pull request comments](https://help.github.com/en/articles/closing-issues-using-keywords) using text such as "Fixes #42" or "Resolves #42".
1. If you know of a contributor who is suitable to review your pull request, [request a review from them](https://help.github.com/en/articles/requesting-a-pull-request-review).
   This step is optional.


# Pull request review guidelines

For a pull request to be acceptable to merge, it must receive at least one favourable review from another member of the Autoware community.
It must also not have any negative reviews that have not been resolved through further development or discussion.

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
  - Does the pull request include sufficient tests to achieve maximum coverage of the new code and any existing code that was changed?
    Do these tests cover all known edge and corner cases for using the new and changed code?
  - Do all Continuous Integration pipelines pass for all supported platforms?
    The CI pipelines check not just behaviour but also check things like coding and documentation style and perform static analysis.
  - If appropriate, have simulated or real-world integration tests been performed?
- Other aspects
  - Does the pull request reference any related issues or pull requests?
  - Can the pull request be merged independent of any other pull requests?
    This is not an absolute requirement because sometimes multiple pull requests are needed for a complex feature, but in the majority of cases if your pull request requires other pull requests to be merged first, it will be looked at very intensively and may not be accepted.
    If you are developing a separate feature that requires another feature still in review, consider waiting for that feature to be merged before making your own pull request.
  - Have the [commits been signed](https://github.com/probot/dco)?

In general, we prefer code reviews to be performed by someone who is distant from the new code.
This means not getting someone who helped you develop it to do the review, but rather asking for a review from someone else who has contributed to Autoware before.
If you do not know who to request a review from, then do not request anyone and the [Highfive bot](https://github.com/rust-lang-nursery/highfive) will randomly choose someone to assign from a list of known contributors.
Sometimes the maintainers will ask for reviews from additional contributors.
This is not an indication that the other reviews were bad or that the contribution is bad, but is usually a sign that the feature or bug fix is considered particularly critical.

Once a pull request has passed review, it will be merged into the main Autoware repository by one of the maintainers.
After this is done you are free to delete the branch you used to develop it in your own fork of the Autoware repository.
We recommend you do so to avoid accidentally developing new contributions from that branch rather than from the tip of the Autoware repository.

However, a pull request cannot be merged until at least 24 hours have passed since the pull request was made.
This gives others a chance to comment on the pull request before it gets merged.

Remember, if you want your pull request merged rapidly then you should communicate your intentions to the community before you begin working.
By doing so, you will ensure that everyone interested already knows what is going on when your pull request arrives.


# <a name="codingstyle"></a>Coding style

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