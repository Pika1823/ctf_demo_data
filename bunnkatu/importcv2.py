# import cv2
# from PIL import ImageFont, ImageDraw, Image
# import numpy as np

# # 入力画像パス、出力画像パス、書き込む文字列
# input_path = 'input.png'
# output_path = 'output.png'
# text = 'flag{InTo_The_Image_flag}'

# # OpenCVで画像読み込み
# img = cv2.imread(input_path)
# if img is None:
#     print(f"Error: Could not read image from {input_path}")
#     exit()

# # BGR→RGB変換
# img_pil = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

# # フォント設定（日本語対応フォントパスを指定）
# # macOSのフォントパス例: '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc'
# # Windowsのフォントパス例: 'C:/Windows/Fonts/meiryo.ttc'
# # Linuxのフォントパス例: '/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc'
# font_path = '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc'
# font_size = 32

# try:
#     font = ImageFont.truetype(font_path, font_size)
# except IOError:
#     print(f"Error: The font file {font_path} was not found. Using default font.")
#     font = ImageFont.load_default()

# draw = ImageDraw.Draw(img_pil)

# # draw.textsize()は非推奨・削除されたため、代わりに draw.textbbox() を使用
# # textbbox()は (left, top, right, bottom) の座標を返す
# left, top, right, bottom = draw.textbbox((0, 0), text, font=font)

# # バウンディングボックスからテキストの幅と高さを計算
# text_w = right - left
# text_h = bottom - top

# # 右下に配置（余白10px）
# x = img_pil.width - text_w - 10
# y = img_pil.height - text_h - 10

# # テキストを描画
# draw.text((x, y), text, font=font, fill=(255, 0, 0))  # 赤色

# # PIL→OpenCV形式に戻して保存
# img_result = cv2.cvtColor(np.array(img_pil), cv2.COLOR_RGB2BGR)
# cv2.imwrite(output_path, img_result)

# print(f"Image saved to {output_path}")

def append_to_image_binary(image_path, text_to_append):
    """
    画像のバイナリデータの末尾に入力文字列を追記する関数。
    """
    # 追記する文字列をバイト列にエンコード
    # ファイルに書き込むため、文字列をバイト列に変換する必要があります
    # '.encode()'は、文字列をUTF-8形式のバイト列に変換します
    text_bytes = text_to_append.encode('utf-8')

    try:
        # 'rb+'モードでファイルを開く
        # 'r'は読み込み、'b'はバイナリモード、'+'は追記・書き込みを可能にします
        with open(image_path, 'rb+') as f:
            # ファイルの末尾にカーソルを移動
            f.seek(0, 2)
            # バイト列をファイルに書き込む
            f.write(text_bytes)

        print(f"ファイルの末尾に「{text_to_append}」を追記しました。")
        print(f"対象ファイル: {image_path}")
    except FileNotFoundError:
        print(f"エラー: 指定されたファイルが見つかりません - {image_path}")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

# 使用例
input_file = 'input.png'  # 書き換えたい画像ファイル
my_text = 'flag{in_The_iMage_comment}'  # 追記したい文字列

append_to_image_binary(input_file, my_text)