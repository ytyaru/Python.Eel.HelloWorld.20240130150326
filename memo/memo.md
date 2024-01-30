Eelを使ってみる。

　Eelを使ってみる。

<!-- more -->

# ブツ

* [リポジトリ][]

[リポジトリ]:https://github.com/ytyaru/Python.Eel.HelloWorld.20240130150326
[DEMO]:https://ytyaru.github.io/Python.Eel.HelloWorld.20240130150326/

## 実行

```sh
NAME='Python.Eel.HelloWorld.20240130150326'
git clone https://github.com/ytyaru/$NAME
cd $NAME/src
./run.py
./test.py
```

# コード抜粋

```python
#!/usr/bin/env python3
# coding: utf8
```

* [PythonでEelを使ってUbuntuのGUIを開発する方法][]

[PythonでEelを使ってUbuntuのGUIを開発する方法]:https://zenn.dev/chaomiosoft/scraps/879d9ebdb80a06

```python
def gui_init():
  eel.init("web")
  eel.start("index.html", port=8080)

if __name__ == '__main__':
  gui_process = Process(target=gui_init)
  gui_process.start()
```
```python
eel.start("index.html", port=8080, cmdline_args=['--kiosk', '--disable-gpu'])
```

