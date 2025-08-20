import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, font_path, font_size, output_path, width=800, height=200):
    """
    黒い文字で文章を書いた画像を生成する関数。

    Args:
        text (str): 画像に書き込む文字列。
        font_path (str): 使用するフォントファイルのパス。
        font_size (int): フォントサイズ。
        output_path (str): 生成した画像の保存パス。
        width (int): 画像の幅（ピクセル）。
        height (int): 画像の高さ（ピクセル）。
    """
    # 1. 白い背景の画像を生成 (PILのRGB形式: (R, G, B))
    # 255, 255, 255 は白、(width, height) は画像のサイズ
    img_pil = Image.new('RGB', (width, height), color=(255, 255, 255))
    
    # 画像に描画するためのオブジェクトを作成
    draw = ImageDraw.Draw(img_pil)

    # 2. フォントを設定
    try:
        # 指定されたフォントパスからフォントをロード
        font = ImageFont.truetype(font_path, font_size)
    except IOError:
        print(f"警告: フォントファイルが見つかりません: {font_path}")
        print("デフォルトフォントを使用します。")
        font = ImageFont.load_default()
    
    # 3. テキストのサイズと位置を計算
    # draw.textbbox() はテキストのバウンディングボックス (left, top, right, bottom) を返す
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]

    # 画像の中央にテキストを配置するための座標を計算
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # 4. テキストを描画 (0, 0, 0 は黒色)
    draw.text((x, y), text, font=font, fill=(0, 0, 0))

    # 5. PILの画像をOpenCV形式（BGR）に変換
    # np.array() でPIL画像をNumPy配列に変換
    # cv2.cvtColor() でRGBからBGRに変換（OpenCVの標準形式）
    img_cv2 = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
    
    # 6. 画像をファイルに保存
    cv2.imwrite(output_path, img_cv2)
    print(f"画像が '{output_path}' に保存されました。")

# 使用例
if __name__ == "__main__":
    # 使用するフォントのパスを指定
    # macOS: '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc' など
    # Windows: 'C:/Windows/Fonts/meiryo.ttc' など
    # Linux: '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc' など
    font_file = '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc'
    
    # 画像に書き込む文章
    my_text = "flag{s3p@r@te_imAgE_puzzle}"
    
    # 出力ファイル名
    output_image = 'text_image.png'
    
    # 関数を実行
    create_image_with_text(my_text, font_file, 50, output_image)