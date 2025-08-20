import cv2
import numpy as np

def reveal_text_from_image(input_image_path):
    """
    画像中の(0,0,255)ピクセル以外を白色に変換し、文字を浮かび上がらせる関数。
    """
    # 画像を読み込む
    img = cv2.imread(input_image_path)
    if img is None:
        print("エラー: 画像を読み込めませんでした。")
        return None

    # 出力用の白画像を作成
    white_image = np.full(img.shape, 255, dtype=np.uint8)

    # 特定の色のピクセルを抽出 (OpenCVのBGR形式: (B, G, R))
    # ここでは真の赤色 (255,0,0) を抽出
    # BGR形式で表現すると (0, 0, 255)
    # np.all()を使用して、3つのチャンネル全てが一致するピクセルを特定
    target_color = np.array([0, 0, 255], dtype=np.uint8)
    
    # マスクを作成
    mask = np.all(img == target_color, axis=-1)

    # マスクを使って白色の画像に文字を貼り付け
    white_image[mask] = img[mask]

    return white_image

# 使用例
input_file_to_decode = 'secret_image.png'
output_file_2 = 'revealed_image.png'

# 1つ目の関数で生成した画像を入力として使用
decoded_image = reveal_text_from_image(input_file_to_decode)

if decoded_image is not None:
    cv2.imwrite(output_file_2, decoded_image)
    print(f"解読された画像が '{output_file_2}' に保存されました。")