---
layout: post
title: ブログつくりました
author: ryoi
date: 2016-12-02 15:37:06 +0900
---
Jekyll でブログつくりました。  
[GitHub Pages](https://pages.github.com/) というのを利用して公開しています。  
適当に書いて `git push -u origin master` するだけで GitHub 側で静的ファイルを生成してくれるので非常に便利です。


なんとなくテーマを1から作ったんですが、Sass 便利ですね。  
変数が使えてネストができるというだけで使う価値があります。


[Jekyll::Compose](https://github.com/jekyll/jekyll-compose) というプラグインを使っているのですが、なぜか Front-matter に date を生成する機能がないので毎回自分で書かないといけません。さすがに面倒なので CotEditor 用のスクリプトを組んで、とりあえずエディタ側でなんとかするようにしました。


{% highlight perl %}
#!/usr/bin/env perl
# %%%{CotEditorXOutput=ReplaceSelection}%%%

use POSIX qw(strftime);

print "date: ", strftime "%F %T %z", localtime;
{% endhighlight %}


[CCS Advent Calendar 2016](http://www.adventar.org/calendars/1592) の記事はここに投稿する予定です。  
それ以外に記事を書くかどうかはわかりませんが、どうぞよろしくお願いします。