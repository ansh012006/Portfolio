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
for sec in ['id="skills"','id="projects"','id="experience"','id="education"','id="achievements"','id="certifications"','id="contact"']:
    assert sec in idx, f"section {sec} missing"
for kw in ["Equinox","LeetCode","HackerRank","Patent","SRMS CET","St. Francis","Bug War","CTF","Python Pro Bootcamp","Java Masterclass"]:
    assert kw in idx, f"keyword {kw} missing"
assert 'src="http' not in idx, "no external JS allowed"
assert "fonts.googleapis" not in idx and "cdn." not in idx, "no external assets allowed"
assert "linear-gradient" in idx, "gradient styling missing"
assert all(ord(c) < 0x2600 for c in idx), "no emojis allowed"
assert "#f59e0b" in idx, "new amber scheme missing"
assert "22c55e" not in idx, "old neon green must go"
assert "viewport" in idx, "responsive meta missing"
print("check.py PASS")
