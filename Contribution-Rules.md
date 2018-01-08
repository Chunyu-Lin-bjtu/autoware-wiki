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

### ROS Coding

First of all, please understand and obey the ROS coding standards, when you add new code to Autoware.

* [ROS Developers Guide](http://wiki.ros.org/DevelopersGuide)

* [ROS C++ Coding Style](http://wiki.ros.org/CppStyleGuide)

You might be interested in using [ROS clang-format](https://github.com/davetcoleman/roscpp_code_format) that helps you to comply with the ROS C++ coding standards automatically in terms of styles, such as indent size and brackets space.

#### How to use clang-format

* Install clang-format. A newer version is better. Ubuntu has a package:
```
sudo apt-get install clang-format-x.x
```

- プロジェクトのトップディレクトリに .clang-formatファイルを置く
- `clang-format -i filename`とすると .clang-formatに従いフォーマットしてくれる.

`clang-format -i`だとファイルは上書きされるので, 実行前に "git commit"を
しておくと安全である.

システム全体に適用するには以下のようなシェルスクリプトを実行すればよい

```sh
for file in $(git ls-files | \grep -E '\.(c|cpp|h|hpp)$' | \grep -v -- '#')
do
    clang-format -i $file
done
```

### ROS Pythonコーディング規約

- http://wiki.ros.org/PyStyleGuide

PEP8準拠をチェックするツールは [pep8](https://pypi.python.org/pypi/pep8)などで機械的に行えばよい.
現状の ROSは Python2.5をターゲットとしているようだが, Ubuntu 16.04以降では
デフォルトの Pythonのバージョンが 3になるので, 今後の保守を考えると,
Python3準拠で書いておいた方が良いと思う.

## ライブラリ化における注意点
- パッケージ間の依存関係を不必要に増やさない. 循環依存は絶対作らない
- そもそもライブラリ化する必要があるかを検討する
- 他パッケージの msgファイルから生成されたヘッダファイルを includeしない
- テストしやすいように書く

### パッケージ間の依存関係を不必要に増やさない

パッケージ間の依存は少ない方が望ましい. 特に循環参照が発生してしまうと,
ビルドができない状態に陥ってしまう.

### そもそもライブラリ化する必要があるかを検討する

汎用的なもの以外は切り出さない方がいい. パッケージ間の依存を返って高めてしまう可能性がある.
別パッケージにするほど有用かをまず考える. 単に関数の切り出しなら, 同じパッケージ内にライブラリを
作成した方が良い.

### 他パッケージの msgファイルから生成されたヘッダファイルを includeしない

msgファイルから生成されたヘッダファイルを includeすると, ライブラリがその msgを持つ
パッケージに依存してしまう. 結果そのライブラリをリンクするパッケージも, その msgを持つ
パッケージに依存してしまうことになってしまう.

メッセージとして受け取ったデータの処理をライブラリに切り出したい場合は,
メッセージに含まれるデータ型(std::vector<double>等)を渡すようにする.
もしくは別途定義したメッセージの型に依存しない class, structに移し替える.

## 現在のライブラリの実装で気になったところ(2016年 3月 30日現在)

下記のような設計, 実装は推奨されない.

### グローバル変数の多用しすぎている点

ライブラリ側でグローバル変数で状態を保存するのでなく, classや構造体に状態を持たせた
方がよい(errnoのように真に大域的なグローバル変数は例外であるが, そのような変数が
必要になることはほとんどない).

C++であればメソッドとして実装, C言語であれば引数でポインタを渡すように実装すればよい.

またグローバル変数を使う関数の場合は, 複数スレッドを使った場合, 値の取得, 更新に
おいて問題が発生する可能性がある(スレッドセーフ). ROSではユーザの見えないところで
スレッドが使われる可能性もあるため, 極力グローバル変数を使わないことが望ましい.
必要な場合は複数スレッドからのアクセスがあるかを考慮し, その可能性がある場合は
排他制御を行う必要性を検討する.


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

# Coding rules and notes related to Real-Time. 

## INDEX

### ROS specific coding Notes
1. Not to “publish” in random period.
2. Node combining two or more topics, to publish at the stage of uniform two topics. 
3. Always put a header in the topic and time stamp to inherit the value of previous topic. 
4. Do not use of the service.
5. Not to topic large data. If unavoidable, use the “nodelet”. 
6. Interdict the use of “MultiThreadSpin”.
7. Interdict the usage for launch file output=”screen” 
8. Avoid using “tf” as much as possible.

### Notes for general embedded and real-time systems.
1. Do not use wide variety of the library such as the chrono.
2. For a functional argument, deploy the pointer and const reference pointer as much as possible. 
3. Use the reference argument as a result of the function.
4. Avoid dynamic partitioning, such as malloc and new. 
5. If the size of vector is roughly estimable, use reserve. 
6. Avoid monster function that spans more than 50 lines. 
7.  Make effective use of inline.
8.  Naming functions, such as get and set, shall not have processing code described.

### Fine coding conventions
Appreciate if any collaborator can add, as needed.

Must read (at least once) http://qiita.com/shirakawa4756/items/55b509fb56cb1bb0c9a4
If time allows, strongly advised http://www.textdrop.net/google-styleguide-ja/cppguide.xml

Other recommendations for reading 
* Effective C++ (recommend)
* ReadableCode (recommend)
* CODE COMPLETE
* C++ Coding Standards
 
## ROS specific coding Notes

-  Not to “publish” in random period.
-  Basicaly, the topic must publish once updated, In other words, there is a need to publics hin the callback.
Following is bad example of coding.
```
while(ros::ok()) {
    publisher.publish(hogehoge);
    loop.sleep();
}
```
- Node combining two or more topics, to publish at the stage of uniform two topics.
For example, if you subscribe to A,B topic, do not publish in the call back function of A, which is updated only A topic.  Both A,B topic being updated and pair must be made in order to perform publish.   

### SAMPLE CODE 
```
A_callback(A_msg) {
    if (is_b_callback == true){ // When A topic has been updated already 
        publish(hogehoge); // publish the data
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_a_callback = true;
}
B_callback(B_msg) {
    if (is_a_callback == true){
        publish(hogehoge);
        is_a_callback = false;
        is_b_callback = false;
        return;
    }
    is_b_callback = true;
}
```

- Always put a header in the topic and time stamp to inherit the value of previous topic.  Update must not be performed without inheritance of the header’s time stamp. Yet, when combining 2 topic together, either topic’s header time stamp can be inherited. 
*Time stamp of two topics header will be the same by synchronization.
 
-  Do not use of the service.  When the service and topic are mixed, real-time estimate becomes difficult.  Basically, it should be carried out in a topic-based.  In non-real-time portion not involved in the recognition, judgment and control of the automated driving operation may utilise the service. 

- Not to topic large data. If unavoidable, use the “nodelet”.  Big data requires few msec to serialize-deserialize, for that reason, large data, such as graphics should utilise the nodelet and invalidate serialize-deserialize. 

- Interdict the use of “MultiThreadSpin”.  When MultiThreadSpin is used, from the point of view of real-time scheduling, it is not preferable because it will become rapidly more complex. You shall not use the MultiThreadSpin in the processing that requires real-time process.

- Interdict the usage for launch file output=”screen”  It is OK for debugging use, however, output=”screen” described file should NEVER be pushed to Git. Other person’s terminal information will be leaked. Basically, do not check rgt, but check  ROS_INFO and ROS_DEBUG from node. 

- Avoid using “tf” as much as possible. For getting location information by using current_pose.  tf library and ROS are separated (not exactly devided, however), it is difficult to secure real-time.  To unify as much as possible to the topic-base, avoid using tf. In addition, tf is very effective when there’s many joints such as arm robot, but not very effective if determined statically coordinate relationship such as automatic driving operation.  

## Notes for general embedded and real-time systems.
-  Do not use wide variety of the library such as the chrono. It will greatly reduces the portability of the RTOS. Do not use them, such as chrono, but utilise ros::WallTime.

-  For a functional argument, deploy the pointer and const reference pointer as much as possible.  int or double is not necessary to use a const call by reference, but the vector or array should use a const call by reference. It reduces the memory consumption and at the same time, it will reduce overhead of the function call.

-  Use the reference argument as a result of the function.  Pass by return value, the speed is significantly slower.  Therefore, including call by reference and pointer, these return value for passing the result to argument should be used.  Pointer, careful attention has to be paid to the scope of the contents of the data.  Basically, return value may use for the error, such as success or failure.
http://nonbiri-tereka.hatenablog.com/entry/2014/02/18/091945

-  Avoid dynamic partitioning, such as malloc and new. malloc and new will cause memory leak to happen.  In addition, It should be avoided as much as possible in order to prevent it difficult to estimate the use size of the resource.

-  If the size of vector is roughly estimable, use reserve. Capacity shortage in the vector, allocate twice the area.  From the experiences, when shortage occur on a large vector, it requires large amount of time to secure, therefore, it is recommended to use the reserve to allocate area in advance.
http://qiita.com/amayaw9/items/6e55b91c28cdc8d32cf2

-  Avoid monster function that spans more than 50 lines. Basically, any function should be kept around 20-30 lines. In addition, bear in mind the particle size of the processing in the function to align.
*I remember reading in “Effective C++”, sophisticated code method is average of 14 lines.
 
-  Make effective use of inline. Few lines of function maybe expanded to inline.  However, it may lead to the increase of the footprint. Caution!

### Bad Example
```
callback() {
    start_time = clock_get_time(); // Not abstracted at all 
    compute_xxx(); // Abstracted too much
}
```
* Use inline effectively. Such a function that has a single line of code, for instance, should be inline. However, inline functions will enlarge footprint. So be careful about using too many inline functions.

* Naming functions, such as get and set, shall not have processing code described.
Programmer shall not describe time consuming processs to get or set.  Only the acquisition and storage of value should be performed by get and set. Another idea is to be able to provide hint/estimate for processing time by the name and heavy function should use computeXXXX. 
 
* getやsetなどの命名に処理コードを記述しない。getやsetに時間のかかる処理を記述してはいけない。getやsetは値の取得や格納のみを行うべき。名前から処理時間をある程度推定できるようにするべきであり、処理が重たい関数にはcomputeHogeHogeを利用する。 

## 参考文献

C++11(14, 17)には型推論等便利な機能が多く加わっているので, C++11以降の内容が
記載されている本を一読することを推奨する.

- [リーダブルコード](https://www.oreilly.co.jp/books/9784873115658/)
- [プログラミング作法](http://ascii.asciimw.jp/books/books/detail/4-7561-3649-4.shtml)
- [Code Complete上巻](http://ec.nikkeibp.co.jp/item/books/589000.html)
- [Code Complete下巻](http://ec.nikkeibp.co.jp/item/books/589100.html)
- [C++11/14 コア言語](http://asciidwango.jp/post/128762444830/c-1114-コア言語)
- [C++ポケットリファレンス](http://gihyo.jp/book/2015/978-4-7741-7408-2)
- [C++のためのAPIデザイン](http://www.sbcr.jp/products/4797369151.html)
- Effective C++
- C++ Coding Standards
- プログラミング言語C++第4版(C++をもっと知りたくなったあなたに）

[[Home](https://github.com/CPFL/Autoware/wiki/)]
[[Next >>](https://github.com/CPFL/Autoware/wiki/Overview)]