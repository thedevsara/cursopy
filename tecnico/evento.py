duration = int(input().strip())

hours = duration // 3600
minutes = (duration % 3600) // 60
seconds = duration % 60

print(f"{hours:.0f}:{minutes:.0f}:{seconds:02d}")