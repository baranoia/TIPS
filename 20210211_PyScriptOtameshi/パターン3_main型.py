import os
import datetime
import shutil
from pathlib import Path

#######################################
def get_file_mod_datetime(file_path):
    mod_ts = os.path.getmtime(str(file_path))
    mod_dt = datetime.datetime.fromtimestamp(mod_ts)
    return mod_dt

def datetime_to_yyyy_mm(dt):
    return dt.strftime("%Y_%m")

def copy_file_to_dir(date_dir, file_path):
    date_dir.mkdir(exist_ok=True)
    shutil.copy2(str(file_path), str(date_dir))

#######################################

# 本体処理部分をmainに閉じ込めることで
# 同名変数のわずらわしさを失くす
def main():
    current_dir = Path("./")
    origin_imgs_dir = Path("./origin_imgs")
    
    rslt_dir = Path("./rslt_imgs")
    if os.path.exists(rslt_dir):
        shutil.rmtree(rslt_dir)
    rslt_dir.mkdir()
        
    for f in origin_imgs_dir.glob("*.jpg"):
        
        # 更新日時の取得
        print(f)
        # mod_ts = os.path.getmtime(str(f))
        # mod_dt = datetime.datetime.fromtimestamp(mod_ts)
        mod_dt = get_file_mod_datetime(f)
    
        # 年月フォルダの作成
        #dir_name = mod_dt.strftime("%Y_%m")
        #date_dir = rslt_dir / dir_name
        dir_name = datetime_to_yyyy_mm(mod_dt)
        date_dir = rslt_dir / dir_name
        #date_dir.mkdir(exist_ok=True)
        print(" rslt_dir:", rslt_dir)
        print(" date_dir:", date_dir)
        print(" f       :", f)
        
        # ファイルコピー
        #shutil.copy2(str(f), str(date_dir))
        copy_file_to_dir(date_dir, f)

#######################################
# mainを実行
main()