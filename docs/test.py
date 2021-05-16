import os
for x in range(10, 31):
    with open(f"写作打卡/5.{x}日写作打卡.md", 'w') as f:
        f.write(f"# 5.{x}日写作打卡")