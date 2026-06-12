# Random Rush 🌩️

[![Python](https://img.shields.io/badge/python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/) [![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?logo=flask&logoColor=white)](https://flask.palletsprojects.com/) [![Faker](https://img.shields.io/badge/Faker-40.19.1-ff6f00)](https://faker.readthedocs.io/) [![Jinja2](https://img.shields.io/badge/Jinja2-3.1.6-ff5722)](https://palletsprojects.com/p/jinja/) [![Requests](https://img.shields.io/badge/Requests-2.34.2-4c8bf5)](https://docs.python-requests.org/) [![pytest](https://img.shields.io/badge/pytest-9.0.3-000000?logo=pytest&logoColor=white)](https://docs.pytest.org/) [![Jenkins](https://img.shields.io/badge/CI-Jenkins-blue?logo=jenkins&logoColor=white)](https://www.jenkins.io/) [![Elastic Beanstalk](https://img.shields.io/badge/AWS-Elastic%20Beanstalk-232f3e?logo=amazon-aws&logoColor=white)](https://aws.amazon.com/elasticbeanstalk/) [![virtualenv](https://img.shields.io/badge/virtualenv-env-green)](https://virtualenv.pypa.io/)

![Random Rush](./static/randomrush.png) 

## 📌 Overview

`Random Rush` is a Flask-based web application that generates random data using the `Faker` library. It delivers a simple UI to select random content categories, request multiple items, and download results as CSV.

This project is currently deployed to AWS Elastic Beanstalk at:

[Random Rush](http://randomrush-env.eba-597ha33i.us-east-1.elasticbeanstalk.com) Try it out!

---

## 🚀 Features

- Generate random data for categories such as:
  - `name`, `address`, `date`, `text`, `credit_card`, `email`, `phone_number`, `colors`, `company`
- Support for localized fake data via Faker locales
- Download generated results as a CSV file
- Flask templates for a polished front-end experience
- CI/CD pipeline skeleton using Jenkins

---

## 🧱 Project Structure

- `application.py` — Flask application entry point
- `templates/` — Jinja2 HTML templates for UI and results
- `static/` — CSS and static assets
- `requirements.txt` — Python package dependencies
- `Jenkinsfile` — simple Jenkins pipeline for build/deploy automation

---

## 📦 Dependencies

This project uses the following Python packages:

| Package | Version |
|--------|---------|
| Flask | 3.1.3 |
| Faker | 40.19.1 |
| pytest | 9.0.3 |

---

## 🌐 Application Routes

- `/` — Main landing page
- `/allow/<selection>` — Selection page for a content category
- `/allow/<results>/<int:digit>/<locale>` — Generate `digit` fake items for `results` using the specified locale
- `/allow/<results>/<int:digit>/<start>/<end>/` — Generate `digit` random dates between `start` and `end`
- `/download/<params>/` — Download JSON-encoded results as CSV

Example:

```text
/allow/first_name/3/en
```

---

## ☁️ AWS Elastic Beanstalk Deployment

This application is designed to run on AWS Elastic Beanstalk with a Python environment.

### Recommended steps

1. Initialize your EB application and environment:
   ```bash
   eb init -p python-3.13 randomrush
   eb create randomrush-env
   ```
2. Deploy the application:
   ```bash
   eb deploy
   ```
3. Verify the environment and logs:
   ```bash
   eb logs
   ```

---

## 🔧 Jenkins Pipeline Overview

The included `Jenkinsfile` defines a basic pipeline with:

- `Build` stage — prints build info
- `Deploy` stage — conditional execution based on environment variables and parameters
- `aws rds describe-db-instances` command as a placeholder for AWS interaction

> Note: This pipeline currently uses AWS CLI and a profile named `danielitosso`. Update the profile and region before use.

---

## � GitHub Actions Workflow

The repository includes a GitHub Actions workflow at `.github/workflows/main.yml` that automates deployment to AWS Elastic Beanstalk.

What it does:

- Checks out the repository code using `actions/checkout`
- Sets up Python 3.13 with `actions/setup-python`
- Runs Snyk dependency and source scans for security issues using `snyk/actions/python`
- Packages the app into `deploy-package.zip`, excluding `.git`, `.github`, `venv`, and `__pycache__`
- Configures AWS credentials from GitHub Secrets (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`)
- Deploys the package to Elastic Beanstalk using `einaregilsson/beanstalk-deploy`

> Make sure to update `application_name` and `environment_name` in the workflow to match your AWS Elastic Beanstalk application and environment.

---

## �🧪 Testing

The project includes `pytest` as a dependency. Add tests under a `tests/` folder and run:

```bash
pytest
```

---

## 💡 Notes

- The app uses `Faker` locale support for localized random data.
- The route configuration must match the URL exactly.
- If deploying to Elastic Beanstalk, ensure the Python runtime and dependencies are correctly specified.

---

## 📝 License

This repository is ready for extension and production hardening. Add your license details here if needed.



