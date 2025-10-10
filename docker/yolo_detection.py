
"""
YOLO Human Detection Test Script
"""

import cv2
from ultralytics import YOLO
import os
import numpy as np

def main():
    print("YOLOv8モデルをロード中...")
    model = YOLO('yolov8n.pt')  # nano版（軽量）
    
    # 入力画像のパス
    input_image = "/app/human.jpg"
    output_dir = "/app/out"
    
    # 出力ディレクトリを作成
    os.makedirs(output_dir, exist_ok=True)
    
    # 画像が存在するかチェック
    if not os.path.exists(input_image):
        print(f"エラー: {input_image} が見つかりません")
        return
    
    print(f"画像を読み込み: {input_image}")
    
    # 検出実行
    print("YOLO検出を実行中...")
    results = model(input_image, save=False, conf=0.25)
    
    # 結果を画像に描画
    annotated_img = results[0].plot()
    
    # 結果を保存
    output_path = os.path.join(output_dir, "detected_human.jpg")
    cv2.imwrite(output_path, annotated_img)
    print(f"検出結果を保存: {output_path}")
    
    # 検出された物体の情報を表示
    print("\n=== 検出結果 ===")
    for r in results:
        boxes = r.boxes
        if boxes is not None:
            for i, box in enumerate(boxes):
                # クラス名を取得
                class_id = int(box.cls[0])
                class_name = model.names[class_id]
                confidence = float(box.conf[0])
                
                # バウンディングボックスの座標
                x1, y1, x2, y2 = box.xyxy[0].tolist()
                
                print(f"オブジェクト {i+1}:")
                print(f"  クラス: {class_name}")
                print(f"  信頼度: {confidence:.2f}")
                print(f"  座標: ({x1:.0f}, {y1:.0f}) - ({x2:.0f}, {y2:.0f})")
                print()
        else:
            print("検出されたオブジェクトはありません")
    
    # 人間（personクラス）の検出数をカウント
    person_count = 0
    if results[0].boxes is not None:
        for box in results[0].boxes:
            class_id = int(box.cls[0])
            class_name = model.names[class_id]
            if class_name == 'person':
                person_count += 1
    
    print(f"検出された人数: {person_count}人")
    
    # 元画像の情報も表示
    original_img = cv2.imread(input_image)
    height, width, channels = original_img.shape
    print(f"\n=== 画像情報 ===")
    print(f"画像サイズ: {width} x {height}")
    print(f"チャンネル数: {channels}")

if __name__ == "__main__":
    main()