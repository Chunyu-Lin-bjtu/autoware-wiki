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

When you are ready to send a pull request from your branch, please follow:

1. A design article should be posted with a GitHub comment for every feature or bug. 
1. Every feature/bug implementation needs to be thoroughly reviewed (at least two reviewers). You can specify your favorite or appropriate reviewers by @accountname.
1. A sample program for the unit test needs to be submitted so that the reviewers or others can check if the implementation logic is correct.
1. The integration test with the [demo data](https://github.com/CPFL/Autoware/wiki/Demo-Data) needs to be passed.  
1. Coding style enforcement must be applied: e.g., [cpplint](https://github.com/google/styleguide/tree/gh-pages/cpplint).
1. The reviewers would further run static code analysis: e.g., [cppcheck](http://cppcheck.sourceforge.net/).

We introduce [Travis CI](https://travis-ci.org/) to automate the above test and deploy steps.

## Coding Standards

You must have your own preference and fashion in coding, but please respect our coding standards as well. No need to force yourself to change your coding style, though the following standards are preferred in Autoware.

### ROS C++ Coding

First of all, please understand and obey the ROS coding standards, when you add new code to Autoware.

* [ROS Developers Guide](http://wiki.ros.org/DevelopersGuide)

* [ROS C++ Coding Style](http://wiki.ros.org/CppStyleGuide)

You might be interested in using [ROS clang-format](https://github.com/davetcoleman/roscpp_code_format) that helps you to comply with the ROS C++ coding standards automatically in terms of styles, such as indent size and brackets space.

#### How to use clang-format

* Install clang-format. A newer version is better. Ubuntu has a package:
```
sudo apt-get install clang-format-x.x
```
* Locate the .clang-format file at the top directory.
* Apply clang-format to the target source file:
```
clang-format -i filename
```

Be careful that `clang-format -i` will overwrite the file. It is safe to do "git commit" before applying clang-format.
If you want to apply clang-format to the entire system, run the following script:
```sh
for file in $(git ls-files | \grep -E '\.(c|cpp|h|hpp)$' | \grep -v -- '#')
do
    clang-format -i $file
done
```

### ROS Python Coding

In addition to C++, you will often use Python in ROS. There is also a coding style guide for Python recommended in ROS.

* [ROS Python Coding Style](http://wiki.ros.org/PyStyleGuide)

You can use [pep8](https://pypi.python.org/pypi/pep8) as a tool to check PEP8-compliant coding.
Many existing ROS programs use Python 2.5, but Ubuntu 16.04 or later versions will use Python 3 by default.
Considering maintenance of coding in the future, Python 3 is preferred in Autoware.

### Notes for Library Development

* Algorithms should be implemented in libraries. For example, the normal distributions transform (NDT) algorithm is desired to be implemented as something like libndt_xxx. Packaging as a library, this algorithm implementation can also be used for other applications apart from ROS or Autoware. This is a spirit of open source.

* Do not make unnecessary dependencies among libraries. In particular, never make circular dependencies. This jeopardizes the entire build system.

* Do not include header files generated from msg files of other packages.

* Keep every library independent and general. Creating too many libraries is also a bad idea.

* Provide a sample program to test the functions of library. 

### Notes for Design and Implementation

#### Global Variables

We should not use global variables unless they are really needed. Instead, we should use classes or structs to hold variables. Even for libraries, we do not recommend using global variables. In C++, you can use methods. In C, you can use pointers or references for function arguments.

Besides in using global variables, you should take care of thread-safe implementation for multi-threaded programs as global variables may be accessed simultaneously among threads. In ROS, particularly, there are many other threads running in background (e.g., polling threads for subscribing to topics). Thus, you should avoid using global variable as much as possible, though you can use mutual exclusion to ensure thread-safe implementation if you really need global variables.

### ライブラリ関数の引数がない or 戻り値が void型

ライブラリ関数の引数がない or 戻り値が void型ということは副作用のために
関数呼び出しを行うことになる. このような関数はテストしづらく, 理解もしづらい.
ライブラリ関数(not クラスメソッド)については副作用のない関数型スタイルで
あることが望ましい. つまり引数が同一であれば結果が一意になる関数.

### ネーミング

現在のライブラリ関数のネーミングには以下の問題がある
- 名前が単純すぎて理解が難しい
- 名前が単純すぎてシンボル名重複が発生しうる

例えば fusionライブラリには `init`, `destroy`と名前付けされた関数が存在するが,
これだけ見ると何に関する初期化, 終了処理なのかがわからない. また名前が
ありふれているためシンボル名が重複してしまう可能性も高い.

#### 解決案
1. ライブラリの prefixを使う
2. namespaceを使う

##### ライブラリの prefixを使う

上記で挙げた fusionライブラリの場合, `fusion_init`, `fusion_destroy`とする.
こうすることで少なくとも fusionに関する処理ということはわかる.

##### namespaceを使う

全体を `namespace autoware::fusion {}`(もしくは `autoware`)でラップする. 利用するときは
`autoware::fusion::init`, `autoware::fusion_init`等になる. システム全体が namespaceを
使っているのであればこの方法が望ましいと思う(特に Autowareのパッケージを一部だけ
切り出し, 別プロジェクトで使うというケースがある場合).

## export, 非 exportシンボル

exportするシンボルを明確にする. 現在の実装では不必要に多くのシンボルが export
されている. 他パッケージから参照しない関数は exportしないようにする.

C++言語, 無名 namespaceでラップする(ファイルローカルの static指定は非推奨).
class, structであれば privateにする.
C言語では staticを指定し, スコープをファイルローカルにする

## Notes for Timing Constraints 

* Do not publish topics in random periods.

* Basically, topics must be published once updated. That is to say, you should publish topics in callback functions.
The following is a bad example of coding.
```
while(ros::ok()) {
    publisher.publish(xxx);
    loop.sleep();
}
```
* If a node has two or more topics, it has to publish them timely when all of them are ready. For example, if you subscribe to A and B topics, do not publish in the callback function associated with A, where only A is updated. You should wait for both A and B to be updated. The following is sample code:   
```
A_callback(A_msg) {
    if (is_b_callback == true) { // If A was updated 
        publish(xxx); // publish the topic
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_a_callback = true;
}
B_callback(B_msg) {
    if (is_a_callback == true){
        publish(xxx);
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_b_callback = true;
}
```

* Always put a header in the topic, and inherit the time stamp from the preceding topic. Do not update the header's time stamp without inheritance. If a node has two or more topics, you can inherit the time stamp from any of these, because their time stamps are supposed to be synchronized.
 
-  Do not use of the service.  When the service and topic are mixed, real-time estimate becomes difficult.  Basically, it should be carried out in a topic-based.  In non-real-time portion not involved in the recognition, judgment and control of the automated driving operation may utilise the service. 

- Not to topic large data. If unavoidable, use the “nodelet”.  Big data requires few msec to serialize-deserialize, for that reason, large data, such as graphics should utilise the nodelet and invalidate serialize-deserialize. 

- Interdict the use of “MultiThreadSpin”.  When MultiThreadSpin is used, from the point of view of real-time scheduling, it is not preferable because it will become rapidly more complex. You shall not use the MultiThreadSpin in the processing that requires real-time process.

- Interdict the usage for launch file output=”screen”  It is OK for debugging use, however, output=”screen” described file should NEVER be pushed to Git. Other person’s terminal information will be leaked. Basically, do not check rgt, but check  ROS_INFO and ROS_DEBUG from node. 

- Avoid using “tf” as much as possible. For getting location information by using current_pose.  tf library and ROS are separated (not exactly devided, however), it is difficult to secure real-time.  To unify as much as possible to the topic-base, avoid using tf. In addition, tf is very effective when there’s many joints such as arm robot, but not very effective if determined statically coordinate relationship such as automatic driving operation.  

## Notes for Embedded Environments

* Do not use a wide variety of libraries. It will decrease portability of RTOS. For example, use ros::WallTime rather than the chrono library. However, what about the boost library? It remains as an open question...

* For function arguments, use pointers and const calls by reference as much as possible. It is not necessary to use them for int or double arguments, but for vector or array arguments, you should use const calls by reference. It saves memory footprint, and also reduces overhead of the function call.

* Use the reference argument when you return from the function. A direct return value will degrade performance. However, be careful about the scope of pointer and so on. Basically, you may want to use a direct return value just for error numbers or Boolean results.

* Avoid dynamic partitioning, such as malloc and new. malloc and new could cause memory leaks. In addition, they make unclear the amount of used resources.

* If the size of vector is roughly estimated, use reserve. The vector allocates memory regions twice in case of capacity shortage. It will require a large amount of time to allocate memory regions twice, you had better to use reserve so that the required memory regions can be allocated tightly in advance.

* Avoid a monster function that spans more than 50 lines. Basically, any function should be kept around 20-30 lines of code. In addition, bear in mind that the granularity of coding within the function should be well balanced. According to [Effective C++](https://www.amazon.com/Effective-Modern-Specific-Ways-Improve/dp/1491903996/ref=sr_1_2?ie=UTF8&qid=1515426637&sr=8-2&keywords=effective+C%2B%2B), a method or function of sophisticated code has only 14 lines on average.
 
### Bad Example
```
callback() {
    start_time = clock_get_time(); // Not abstracted at all 
    compute_xxx(); // Abstracted too much
}
```
* Use inline effectively. Such a function that has a single line of code, for instance, should be inline. However, inline functions will enlarge footprint. So be careful about using too many inline functions.

* Function naming should correspond to the function code. For example, do not write heavy code in get() or set(), because these functions are supposed to just get or set some values. Function naming should imply what the function is and what is the cost of processing time. If you want to create a time-consuming function, for example, probably function naming such as compute_xxx is suitable. 

## C++ Books

C++ 11/14/17 has introduced many useful capabilities, e.g., type inference.
You may want to review C++ 11 through the popular books: [[Amazon links](https://www.amazon.com/s/ref=nb_sb_noss_2/135-5470609-2801335?url=search-alias%3Daps&field-keywords=C%2B%2B+11)]

[[Home](https://github.com/CPFL/Autoware/wiki/)]
[[Next >>](https://github.com/CPFL/Autoware/wiki/Overview)]