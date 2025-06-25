# ChatGPT 자동파일분류.py
import os
import shutil

# 다운로드 폴더 경로
DOWNLOADS_DIR = r"C:\Users\idk82\Downloads"

# 이동할 폴더 경로
IMAGES_DIR = r"C:\work\images"
DATA_DIR = r"C:\work\data"
DOCS_DIR = r"C:\work\docs"
ARCHIVE_DIR = r"C:\work\archive"

# 확장자별로 이동할 폴더 매핑
dest_map = {
    ('.jpg', '.jpeg'): IMAGES_DIR,
    ('.csv', '.xlsx'): DATA_DIR,
    ('.txt', '.doc', '.pdf'): DOCS_DIR,
    ('.zip',): ARCHIVE_DIR
}

# 폴더가 없으면 생성
def ensure_dir(path):
    if not os.path.exists(path):
        os.makedirs(path)

for exts, folder in dest_map.items():
    ensure_dir(folder)

# 파일 이동
def move_files():
    for filename in os.listdir(DOWNLOADS_DIR):
        src = os.path.join(DOWNLOADS_DIR, filename)
        if not os.path.isfile(src):
            continue
        ext = os.path.splitext(filename)[1].lower()
        for exts, dest in dest_map.items():
            if ext in exts:
                dst = os.path.join(dest, filename)
                shutil.move(src, dst)
                print(f"Moved: {filename} -> {dest}")
                break

if __name__ == "__main__":
    move_files()
