import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
import random

def create_random_red_image_with_text(text, font_path, font_size, width, height):
    """
    文字を赤色で描き、背景をランダムな赤系色で埋めた画像を生成する関数。
    """
    # 背景の画像を生成 (OpenCVのBGR形式: (B, G, R))
    # ランダムな赤色で初期化
    img = np.zeros((height, width, 3), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            # ランダムな青色成分を生成 (200から244の間)
            # OpenCVではBGR形式なので、赤色は一番右の要素
            red_component = random.randint(253, 254)
            img[y, x] = [0, 0, red_component]

    # Pillowに変換してテキストを描画
    img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(img_pil)

    try:
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"警告: フォントファイルが見つかりません。デフォルトフォントを使用します。")
        font = ImageFont.load_default()

    # 文字のバウンディングボックスを取得
    left, top, right, bottom = draw.textbbox((0, 0), text, font=font)
    text_width = right - left
    text_height = bottom - top

    # 文字を画像の中央に配置
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    # 真の赤色で文字を描画 (PILのRGB形式: (R, G, B))
    draw.text((text_x, text_y), text, font=font, fill=(255, 0, 0))

    # PILからOpenCV形式に戻す
    img_result = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)

    return img_result

# 使用例
text = "flag{red_iMage_Find_Flag}"
font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc'  # フォントパスを環境に合わせて変更
output_file_1 = 'secret_image.png'
generated_image = create_random_red_image_with_text(text, font_path, 40, 600, 200)

cv2.imwrite(output_file_1, generated_image)
print(f"画像が '{output_file_1}' に保存されました。")