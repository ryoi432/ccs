---
layout: post
title: ブログつくりました
author: ryoi
date: 2016-12-02 15:37:06 +0900
moddate: 2016-12-03 17:42:37 +0900
---
Jekyll でブログつくりました。  
[GitHub Pages](https://pages.github.com/){:target="_blank"} というのを利用して公開しています。  
適当に書いて `git push -u origin master` するだけで GitHub 側で静的ファイルを生成してくれるので非常に便利です。


なんとなくテーマを1から作ったんですが、Sass 便利ですね。  
変数が使えてネストができるというだけで使う価値があります。  
デザインにはみんな大好き [Bootstrap](http://getbootstrap.com/){:target="_blank"} を fork した [Umi](http://nkmr6194.github.io/Umi/){:target="_blank"} というテーマを使わせていただきました。


[Jekyll::Compose](https://github.com/jekyll/jekyll-compose){:target="_blank"} というプラグインを使っているのですが、なぜか Front-matter に date を生成する機能がないので毎回自分で書かないといけません。さすがに面倒なので CotEditor 用のスクリプトを組んで、とりあえずエディタ側でなんとかするようにしました。


{% highlight perl %}
#!/usr/bin/env perl
# %%%{CotEditorXOutput=ReplaceSelection}%%%

use POSIX qw(strftime);

print "date: ", strftime "%F %T %z", localtime;
{% endhighlight %}


[CCS Advent Calendar 2016](http://www.adventar.org/calendars/1592){:target="_blank"} の記事はここに投稿する予定です。  
それ以外に記事を書くかどうかはわかりませんが、どうぞよろしくお願いします。