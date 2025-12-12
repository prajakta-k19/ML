# Basic Python CLI Example

This is a tiny, beginner-friendly Python project you can upload to GitHub.

Files:
- `basic_app.py` — a simple CLI that greets a user (`--name`, `--shout`).
- `.gitignore` — common Python ignores.

How to run locally:

```powershell
cd c:\Users\KIIT0001\Desktop\Coding\python\ML
python basic_app.py --name Alice
python basic_app.py -n Alice -s
```

How to push to GitHub (create a new repo on GitHub first):

```powershell
cd c:\Users\KIIT0001\Desktop\Coding\python\ML
git init
git add .
git commit -m "Add basic Python CLI example"
git branch -M main
# replace <your-repo-url> with the repo URL from GitHub
git remote add origin <your-repo-url>
git push -u origin main
```

License: choose one (MIT/Apache/None) before publishing if needed.
