# faster-whisper-test
[<img src="https://img.shields.io/github/stars/mimisukeMaster/faster-whisper-test">](https://github.com/mimisukeMaster/faster-whisper-test/stargazers)
[<img  src="https://img.shields.io/github/license/mimisukeMaster/faster-whisper-test">](/LICENSE)
[<img src="https://img.shields.io/badge/issues-welcome-orange">](https://github.com/mimisukeMaster/faster-whisper-test/issues)<br>
<img src="https://img.shields.io/github/repo-size/mimisukeMaster/faster-whisper-test?color=ff69b4&logo=gitlfs">
[<img src="https://img.shields.io/static/v1?label=&message=Open%20in%20Visual%20Studio%20Code&color=007acc&style=flat">](https://github.dev/mimisukeMaster/faster-whisper-test)

A sample project to test and demonstrate [faster-whisper](https://github.com/guillaumekln/faster-whisper).


## About

[faster-whisper](https://github.com/guillaumekln/faster-whisper) のテストと動作確認を目的としたサンプルプロジェクトです。

faster-whisperは、高速な音声認識推論を実現するライブラリです。このプロジェクトでは、実際にYoutubeのリンクからその動画の文字起こし(STT処理)を行います。

## Requirements and Models
- 必要なパッケージは以下の通りです。（実行するタイミングは下方参照）<br>
バージョンはあくまで自機で動作確認済みのものです。
    ```cmd
    yt-dlp==2025.3.21 
    faster_whisper==1.1.1
    ffmpeg==4.3.1
    cudnn==9.1.1.17
    ```

- GPUでの推論の場合、動かすモデルに対応するスペック以上のGPUが必要です。<br>
実行時間は5~6倍かかりますが、CPUで動かすことも可能です。

    |モデル|パラメータ数|推奨VRAM|
    |:----:|:----:|:----:|
    |tiny|32M|1GB以上|
    |base|74M|2GB以上|
    |small|244M|4GB以上|
    |medium|769M|6GB以上|
    |large, large-v3|1550M|10GB以上|

    また、GPUはFP16（半精度浮動小数点）計算に対応しており、CUDA Compute Capability 6.0以上（Pascal世代以降）が推奨です。
    ※GPUの性能が対象のモデルに見合わない場合、推論が正常に行われず、音声の一部が変換されなかったり`out-of-memory`エラーにより処理が中断される可能性があります。

  - 2025/3現在、公式のHugging Faceでは`large`モデル以外を使う場合、より軽量・高速化した蒸留モデル`distil-large-v3`の使用が推奨されています([参照](https://huggingface.co/distil-whisper))が、日本語の推論はサポートされていないことをご注意ください。


## Get Started

### 1. conda環境の作成

[Anaconda](https://www.anaconda.com/)を使用してPythonの実行環境を用意します。<br>**環境作成にvenvを用いると、ffmpeg, cudnnを手動で入れる手間が生じるので、condaの使用を推奨します。**

Anaconda Prompt から、新しいconda環境を作成します。
```cmd
conda create -n [環境名] python==3.11
```
その環境内で、以下のコマンドを実行して必要なパッケージをインストールしてください。

```cmd
pip install yt-dlp
pip install faster_whisper
conda install -c conda-forge ffmpeg
conda install -c conda-forge cudnn
```

### 2. 実行方法
実行方法は2通りあります:

1. **VSCode から実行する場合:**
   - VSCode でこのプロジェクトを開きます。
   - 右下の `インタプリタの選択` から先ほど作成したconda環境を選択します。
   - `main.py` を実行してください。

2. **Anaconda Prompt から実行する場合:**
   - 作成した環境をactivateさせたAnaconda Prompt から、`main.py` が存在するディレクトリに移動します。
   - 以下のコマンドを実行してください:
     ```bash
     python main.py
     ```

## References

- このプロジェクトはこちらの記事をもとに作成しました:<br>
    https://zenn.dev/tsuzukia/articles/1381e6c9a88577
- faster-whisper Hugging Face:<br>
    https://huggingface.co/models?search=openai/whisper
- 推論時の量子化処理の程度と必要なスペック:<br>
    https://opennmt.net/CTranslate2/quantization.html


## License
faster-whisper-test is under the [MIT](/LICENSE) license.