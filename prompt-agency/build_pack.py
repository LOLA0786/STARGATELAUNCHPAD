import zipfile, os

os.makedirs("dist", exist_ok=True)
with zipfile.ZipFile("dist/pack.zip", "w") as z:
    z.write("packs/arabic.md")

print("Pack built!")
