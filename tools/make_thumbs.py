from pathlib import Path
from PIL import Image

SRC = Path("assets/photos")
DST = Path("assets/photos/_thumb")

# 缩略图长边上限（建议 900~1400）
MAX_EDGE = 1200
JPEG_QUALITY = 78

def is_img(p: Path) -> bool:
    return p.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp", ".gif"}

def make_thumb(src: Path, dst: Path):
    dst.parent.mkdir(parents=True, exist_ok=True)
    with Image.open(src) as im:
        im = im.convert("RGB")
        w, h = im.size
        scale = MAX_EDGE / max(w, h)
        if scale >= 1:
            # 原图已经不大，仍然生成一份以保证统一路径
            out = im
        else:
            out = im.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
        out.save(dst, format="JPEG", quality=JPEG_QUALITY, optimize=True, progressive=True)

def main():
    for p in SRC.rglob("*"):
        if not p.is_file():
            continue
        if "_thumb" in p.parts:
            continue
        if not is_img(p):
            continue
        rel = p.relative_to(SRC)
        out = DST / rel
        out = out.with_suffix(".jpg")  # 统一输出 jpg
        # 如果已存在且比源文件新，就跳过
        if out.exists() and out.stat().st_mtime >= p.stat().st_mtime:
            continue
        make_thumb(p, out)

if __name__ == "__main__":
    main()
