# Build contact sheets per site: desktop frames 0-3 and 4-7 as 2x2 grids, phone frames 0-5 as a 3x2 grid.
import sys, glob, os
from PIL import Image, ImageDraw

root = sys.argv[1]
def grid(files, cols, cell_w, out):
    if not files: return
    ims = [Image.open(f).convert('RGB') for f in files]
    w0, h0 = ims[0].size
    cell_h = int(h0 * cell_w / w0)
    rows = (len(ims) + cols - 1) // cols
    sheet = Image.new('RGB', (cols * cell_w + (cols - 1) * 6, rows * cell_h + (rows - 1) * 6), (128, 128, 128))
    for i, im in enumerate(ims):
        im = im.resize((cell_w, int(im.size[1] * cell_w / im.size[0])))
        x, y = (i % cols) * (cell_w + 6), (i // cols) * (cell_h + 6)
        sheet.paste(im.crop((0, 0, cell_w, cell_h)), (x, y))
        ImageDraw.Draw(sheet).text((x + 4, y + 4), os.path.basename(files[i]), fill=(255, 0, 80))
    sheet.save(out, 'JPEG', quality=70)

for d in sorted(glob.glob(os.path.join(root, '*/'))):
    dk = sorted(glob.glob(d + 'desktop-0*.jpg'))
    ph = sorted(glob.glob(d + 'phone-0*.jpg'))
    grid(dk[:4], 2, 720, d + 'sheet-desktop-a.jpg')
    grid(dk[4:8], 2, 720, d + 'sheet-desktop-b.jpg')
    grid(ph[:6], 3, 260, d + 'sheet-phone.jpg')
print('sheets done')
