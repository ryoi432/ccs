---
layout: post
title: DTVに最適なコンテナフォーマット
author: ryoi
date: 2016-12-19 22:40:11 +0900
moddate: 2016-12-20 17:30:55 +0900
---
この記事は [DTV Advent Calendar 2016](http://www.adventar.org/calendars/1429){:target="_blank"} 19日目の記事です。
{:.well}

日本の地上デジタル放送や BS/CS デジタル放送は、基本的に MPEG-2 TS と呼ばれるコンテナフォーマットで多重化されたデータを放送しています。
MPEG-2 TS はストリーミングに最適化されており、ノンリニアに編集したり、保存して視聴するには適さないフォーマットです。
この記事では、そんな MPEG-2 TS をどのようなフォーマットに変換すれば便利に扱えるかを考えようというお話をします。

### なぜ TS のままだとダメなのか

- 取り扱いがだるい
そのまま変換しようとすると、ほぼ確実に映像と音声がズレます。
- 再生がつらい
最近は減りましたが、正しく再生できないプレイヤーがありました。
特に iOS/Android 上のプレイヤーに多かった印象があります。
- 機能が足りない
個人的にはこれが一番大きいです。
MPEG-2 TS には、チャプターを挿入する機能がありません。
放送にチャプターもクソもないので、ついていないのは当たり前といえば当たり前なんですが。

### いいコンテナフォーマットを探す

前述の問題を解決するために、いろいろなフォーマットを調べてどれがいいのか比べてみました。

### MPEG-2 PS

ほぼ TS と同じなので、変換に手間取ることはありません。PS に変換すると、TS 特有の番組表や有料放送用のデータが落ちるため、ファイルサイズが小さくなります。DVD 等にも用いられている MPEG-2 PS ですが、チャプターを挿入する機能がありません。個人的にはこれだけで比較対象から外れるのですが、何か理由があるのでしょうか。

ちなみに BonTsDemux で エンコード方式を `MPEG2PS` にして変換すると、ffmpeg により音声が再エンコードされてしまうので、demux してからなんらかの muxer を用いて mux するといいと思います。

### Matroska

[Matroska](https://www.matroska.org/index.html){:target="_blank"} とは公式サイトによると、

> *Matroska* the extensible, open source, open standard Multimedia container.

だそうです。

最近はサブセットの WebM が有名ですが、本体の方はいまいち流行ってません。入れられるコーデックは、[Codec Specs](https://www.matroska.org/technical/specs/codecid/index.html){:target="_blank"} に書かれており、主要なものは一通り揃っています。機能的にも問題はなさそうです。

### MP4

安定の MPEG4 です。みんな大好き H.264 も同じ MPEG-4 の Part 10 として標準化されています。機能は多く、H.264 と合わせて現在最も利用されているフォーマットだと思います。
H.264 と一緒に使われることが多い MP4 ですが、実は MPEG-2 を入れることもできます。したがって、TS から再エンコードすることなく MP4 を利用することもできてしまうのです。

MP4 で mux するには [MP4Box](https://gpac.wp.mines-telecom.fr/mp4box/){:target="_blank"} を利用します。BonTsDemux で demux したあと、MP4Box で mux するという流れになるのですが、BonTsDemux から出力された音声ファイルはズレているため、補正する必要があります。BonTsDemux で出力した音声ファイルのファイル名に付加される`DELAY *ms`が遅延時間となります。経験則では、音声が数百ms早いことが多いようで、`DELAY -100ms`というように出力されます。この情報を MP4Box に渡してあげる必要があるのですが、そのまま音声を早めるように処理させると頭に無音で真っ暗な部分が生じてしまいます。この挙動が仕様と実装のどちらによるものなのかは分かりませんが、映像のみで音声がないことは許され、音声のみで映像がないことは許されないようです。したがって BonTsDemux が出力した遅延時間の正負を反転させ、映像を遅らせるようにするとうまく処理されます。

{% highlight shell_session %}
$ MP4Box.exe -fps 29.97002997002997 -add "[映像ファイル名].m2v"#video:par=4:3:delay=[遅延ms] -add "[音声ファイル名].aac"#audio -chap "[チャプターファイル名].txt" -new "[出力ファイル名].mpg"
{% endhighlight %}

### たどり着いた結果

0. TsSplitter でいらないデータを落とす
1. BonTsDemux で TS を m2v と aac に demux
2. m2v を元に [logoGuillo](http://loggialogic.blogspot.com/2011/11/cm-logoguillo.html){:target="_blank"} で CM 検出し、.chapters.txt を生成
3. [MP4Box](https://gpac.wp.mines-telecom.fr/mp4box/){:target="_blank"} で m2v, aac, .chapters.txt を mux

録画マシンのスペックが低いためこのような形になりました。

### まとめ

いかがでしたでしょうか。
結局 MP4 に入れてしまいましょうという普通の結論になってしまいましたが、録画マシン運用の参考になれば幸いです。


[DTV Advent Calendar 2016](http://www.adventar.org/calendars/1429){:target="_blank"} 20 日目の記事は [kanreisa](https://twitter.com/kanreisa){:target="_blank"} さんです。
{:.well}
{:style="margin-top:3em;"}
