# Contributing

## Adding translations

To translate the letter, copy `index.md` into `_translation/`
and name it `index_lang.md` where `lang` is language code you are going to translate into.

Then you can start translating this file.

To display translation in the translations list, simply add `emoji` attribute to the document as follows:

For example: `_translations/index_de.md`

```md
---
layout: signed
...
emoji: 🇩🇪
---

2021-03-23

Richard M. Stallman, ...
```

There are lots of translation already, if you feel lost, be sure to check out how its done in other ones.

When you translated the text, added emoji attribut you can commit your change and make pull request.
