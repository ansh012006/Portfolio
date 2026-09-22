import pathlib, re, sys
p = pathlib.Path(__file__).parent
idx = (p / "index.html").read_text(encoding="utf-8")
res = (p / "resume.html").read_text(encoding="utf-8")
assert "Ansh Agarwal" in idx
assert "ansh012006@gmail.com" in idx
assert "github.com/ansh012006" in idx
for repo in ["Inventory_Management","job-application-tracker","weather_app","Movie_Explorer","EduTech","makan_mitr_backend","Kisan_Mitra","agrisetu-backend"]:
    assert repo in idx
    assert repo in res or repo.replace("_"," ") in res or repo.replace("_","-") in res
for live in ["inventorymanagement-ashy-two.vercel.app","job-application-tracker-eta-seven.vercel.app","weather-app-one-delta-60.vercel.app","movie-explorer-blond-xi.vercel.app"]:
    assert live in idx
print("check.py PASS")
