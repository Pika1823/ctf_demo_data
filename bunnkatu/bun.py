import cv2
import os

def split_image_into_n_parts(image_path, rows, cols, output_dir='output_split'):
    """
    指定した画像をrows行とcols列に分割し、個別の画像ファイルとして保存する。

    Args:
        image_path (str): 分割したい画像のパス。
        rows (int): 分割する行数。
        cols (int): 分割する列数。
        output_dir (str): 分割した画像を保存するディレクトリ名。
    """
    # 出力ディレクトリが存在しなければ作成
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # 画像を読み込み
    img = cv2.imread(image_path)
    if img is None:
        print(f"エラー: 画像が見つかりません - {image_path}")
        return

    # 画像の高さと幅を取得
    height, width, _ = img.shape

    # 分割する各ピースの高さと幅を計算
    piece_height = height // rows
    piece_width = width // cols

    print(f"画像を{rows}行 x {cols}列に分割します。")
    print(f"元の画像サイズ: {width}x{height} ピクセル")
    print(f"各ピースのサイズ: {piece_width}x{piece_height} ピクセル")

    # 画像をループで分割
    count = 0
    for i in range(rows):
        for j in range(cols):
            # 各ピースの開始座標と終了座標を計算
            start_y = i * piece_height
            end_y = (i + 1) * piece_height
            start_x = j * piece_width
            end_x = (j + 1) * piece_width

            # 画像からピースを切り出し
            piece = img[start_y:end_y, start_x:end_x]

            # ファイル名を生成し、保存
            count += 1
            output_path = os.path.join(output_dir, f'piece_{count}.png')
            cv2.imwrite(output_path, piece)
            print(f"  - '{output_path}' を保存しました。")

    print(f"合計 {count} 個の画像ピースが '{output_dir}' ディレクトリに保存されました。")

# 使用例
input_image_path = 'input_image.png'  # 分割したい画像ファイル
rows_to_split = 5
cols_to_split = 6
total_pieces = rows_to_split * cols_to_split
print(f"画像を合計 {total_pieces} 分割します。")

# 関数を実行
split_image_into_n_parts(input_image_path, rows_to_split, cols_to_split)