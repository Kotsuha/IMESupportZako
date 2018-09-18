# IMESupportZako

Ever since I started to use [Origami](https://github.com/SublimeText/Origami) I found that [IMESupport](https://github.com/chikatoike/IMESupport) isn't working well with it. The IME composition window isn't displayed at correct position. This is a **personal repo where I try to fix it for myself**.

### Disclaimer

I have no experience in both Python and Sublime Text plugin creation and I find it hard to understand all the original code. Instead of making modification to the original IMESupport plugin or other forks, it's easier for me to create a new plugin, copy-paste and modify only the code I think is needed. That's why many codes and files are gone comparing to the original version. Currently it's not working perfectly but enough for me.

If you have the same problem and happen to have the same environment as me, maybe you can try this. Nothing is promised though.

## Environment

* Sublime Text Version 3.1.1, Build 3176 x64
* Windows 8.1 64-bit
    - Chinese (Traditional) - Microsoft Bopomofo → OK
    - Japanese - Microsoft IME → OK

## Screenshot

![](img/img1.png)

## Known Issue

* cursor 在 [widget (dialog)](http://docs.sublimetext.info/en/latest/reference/settings.html?highlight=is_widget#system-and-miscellaneous-settings) 裡的情況有時候定位不準。
* 切換顯示或隱藏 Side Bar 的時候定位不準 — as mentioned by [zcodes](https://github.com/zcodes/IMESupport)。

以上情況似乎都是讓 selection 更新 (例如隨便打個英文字) 就好了。目前沒去研究問題出在哪。

* Chinese (Simplified) - Microsoft Pinyin 定位不準