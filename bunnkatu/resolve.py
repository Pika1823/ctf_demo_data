def get_last_n_bytes(file_path, n=100):
    """
    ファイルの末尾から指定したバイト数を取得し、文字列としてデコードする関数。
    """
    try:
        # 'rb'モード（読み込み専用、バイナリ）でファイルを開く
        with open(file_path, 'rb') as f:
            # ファイルサイズを取得
            f.seek(0, 2)
            file_size = f.tell()

            # ファイルサイズがnバイトより小さい場合は、ファイル全体を読み込む
            if file_size < n:
                n = file_size

            # ファイル末尾からnバイト手前にカーソルを移動
            f.seek(-n, 2)
            
            # データを読み込む
            last_bytes = f.read(n)

            # バイト列を文字列にデコードして返す
            # エンコーディングが不明な場合は 'utf-8' が一般的
            return last_bytes.decode('utf-8', errors='ignore')

    except FileNotFoundError:
        print(f"エラー: 指定されたファイルが見つかりません - {file_path}")
        return None
    except Exception as e:
        print(f"エラーが発生しました: {e}")
        return None

# 使用例
input_file = 'input.png'  # 末尾の文字列を取得したいファイル
last_100_chars = get_last_n_bytes(input_file, 100)

if last_100_chars is not None:
    print("ファイルの末尾100バイト:")
    print(last_100_chars)