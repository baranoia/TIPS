import os
import datetime
import shutil
from pathlib import Path

current_dir = Path("./")
current_dir

origin_imgs_dir = Path("./origin_imgs")
origin_imgs_dir

#datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
rslt_dir = Path("./rslt_imgs")
if os.path.exists(rslt_dir):
    shutil.rmtree(rslt_dir)
rslt_dir.mkdir()

for f in origin_imgs_dir.glob("*.jpg"):
    
    # 更新日時の取得
    print(f)
    mod_ts = os.path.getmtime(str(f))
    #print(mod_ts)
    mod_dt = datetime.datetime.fromtimestamp(mod_ts) # 1517316813.1418388
    #print(mod_dt) # 2018-01-30 21:53:33.141839
    
    # 年月フォルダの作成
    dir_name = mod_dt.strftime("%Y_%m")
    #print(dir_name) # 2018_01
    date_dir = rslt_dir / dir_name # origin_imgs\2018_01
    #print(date_dir) # rslt_imgs\2018_01
    date_dir.mkdir(exist_ok=True)
    
    # ファイルコピー
    shutil.copy2(str(f), str(date_dir))