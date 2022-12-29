# flask-vercel

### Flask app URL: https://vercel.com/sreegithub19/flask-vercel-1

### Flask app name: flask-vercel-1

This repo is to test the deploy to Vercel

## Test local

```
Mac:
- virtualenv ~/.ve/vercel
- source ~/.ve/vercel/bin/activate
Windows:


Most important commands to run the project:
- - pip install -r requirements.txt
- - FLASK_APP=index.py flask run


# 🚀 go to http://localhost:5000
```

## Push to github and Deploy to vercel

- Create an account at https://vercel.com/
- Install the Vercel CLI: `npm i -g vercel`
- Mac:
  - git add . && git commit -m "Changes" && git push origin master
  - git add . ; git commit -m "Changes" ; git push origin master
- Then, inside your repo folder, run `vercel`.

```
For the first time:

(vercel) ➜  flask-vercel$ vercel
Vercel CLI 23.0.1
? Set up and deploy “~/workspace/workon/flask-vercel”? [Y/n] y
? Which scope do you want to deploy to? your-vercel-account
? Link to existing project? [y/N] n
? What’s your project’s name? flask-vercel
? In which directory is your code located? ./
...
```

```
Next time onwards:

$ vercel
Vercel CLI 28.7.2
? Set up and deploy “~/Desktop/vercel_flask_app”? [Y/n] y
? Which scope do you want to deploy to? sreegithub19
? Link to existing project? [y/N] y
? What’s the name of your existing project? flask-vercel-1
🔗  Linked to sreegithub19/flask-vercel-1 (created .vercel)
🔍  Inspect: https://vercel.com/sreegithub19/flask-vercel-1/8UmoRDJ9VKJeemi9kJixHP66XKgv [11s]
✅  Preview: https://flask-vercel-1-sreegithub19.vercel.app [24s]
📝  To deploy to production (flask-vercel-1-sand.vercel.app), run `vercel --prod`
❗️  Due to `builds` existing in your configuration file, the Build and Development Settings defined in your Project Settings will not apply. Learn More: https://vercel.link/unused-build-settings
```

Done! You should access your very simple flask app running on Vercel
