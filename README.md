# 環境構築手順

##  1. Fork
リポジトリ上部のForkから、自分のリモートリポジトリにコピーを作成します。

## 2. 自分のPCにクローン

### ※ターミナルで実行

```bash
# 自分のForkをクローン
git clone https://github.com/ユーザー名/Project_OccluSense.git

# ディレクトリに移動
cd Project_OccluSense
```

## 3. Dockerを起動

ターミナルで以下を入力：

```bash
# Dockerディレクトリに移動
cd docker

# Dockerイメージをビルド(時間かかります)
docker compose build

#プログラムを実行(とても時間かかります)
docker compose up -d

#Docker内にはいる
docker exec -it occdet_demo bash
```