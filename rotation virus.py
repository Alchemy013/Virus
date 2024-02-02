import time,rotatescreen as rs
pd=rs.get_primary_display()
l=[90,180,270,0]
for i in range(10):
    for x in l:
        pd.rotate_to(x)
        time.sleep(0.2)
        