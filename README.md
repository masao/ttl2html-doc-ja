## リソースファイルの追加方法

新しい翻訳対象ファイルが追加された場合のみ、一回だけ、以下の手順で追加する必要がある。
以下では、`xlsx2shape.rst`ファイルが追加になった場合を例にした編集手順を示す。

1. `docs/.tx/config`ファイルを更新する

末尾に、新しいファイル分のエントリを追加する。他のエントリをコピペして対象ファイル名だけ変えたもので良い。

例: https://github.com/masao/ttl2html-doc-ja/commit/ff2e86a34f519e8c64d37284c8de5312697e6bac

2. すべての更新内容をコミットする

```bash
git add xlsx2shape.rst locales/ja/LC_MESSAGES/xlsx2shape.po
```

## 翻訳内容の更新、同期方法

Transifex https://app.transifex.com/ttl2html/ttl2html/ 上で実際の翻訳内容を確認しながら、全ての文章を翻訳、更新していく。

元の英語文書が変更になった場合、および、翻訳が完成したら、以下のコマンドを実行して、その内容を同期更新すること。

```bash
cd docs/
make
```

最後にコミットして GitHub 上に push すれば、翻訳内容が公開される。
