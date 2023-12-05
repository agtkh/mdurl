# mdurl

#markdown, #scraping, #python3, #tool

## 概要
このコードは、入力されたURLからタイトルを取得し、Markdown形式で出力するプログラムです。

## 使い方
```
$ python3 mdurl.py
```

と実行すると、標準入力からURLを入力できます。

また、引数にURLを指定することもできます。

```
$ python3 mdurl.py https://qiita.com/
```

と実行すると、Qiitaのトップページのタイトルが取得されます。

## 出力形式
出力形式は、引数で指定できます。

`-l` または `--list` を指定すると、箇条書き形式で出力されます。

`-n` または `--number` を指定すると、番号付きリスト形式で出力されます。

