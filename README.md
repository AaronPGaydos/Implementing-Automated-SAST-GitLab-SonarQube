# Implementing-Automated-SAST-GitLab-SonarQube
Reference implementation for automated SAST in CI/CD. Includes an intentionally vulnerable Flask app, GitLab CI integration, and SonarQube scanning to enforce pipeline gates, produce actionable reports, and drive secure remediation in production-grade DevSecOps workflows.

## 1. Create a deliberately insecure sample application
This simulates a development scenario where security flaws might be overlooked. By introducing known vulnerabilities, we can create a safe environment to explore how automated static application security testing (SAST) can detect issues before they reach production.

<img width="674" height="301" alt="image" src="https://github.com/user-attachments/assets/70ef71df-13ea-4eef-94f9-090725eb1bec" />

📚 Learning Bite: “SAST helps find flaws before attackers do.”

## 2. Vulnerable App Pipeline
In this step, we demonstrate how insecure code can flow through CI/CD pipelines when security scans are not enforced. The vulnerable Flask app from Step 1 has been pushed to GitLab, and the minimal pipeline (build + test) executes successfully. While the pipeline passes and artifacts are technically “deployable,” the app contains unmitigated vulnerabilities such as SQL injection.

Key Details

Repository: GitLab project contains app.py and .gitlab-ci.yml

Pipeline: Minimal CI pipeline with build and test stages only

Outcome: All jobs complete successfully (green checkmarks), but no security analysis occurs

<img width="992" height="54" alt="image" src="https://github.com/user-attachments/assets/e1dccf9c-4f7b-4e15-b3c6-b71f2559f5c8" />
📚 Learning Bite: “This is how insecure code sneaks into prod.”

## 3. Root Cause Analysis

Using SonarQube through docker container, I ran a local analysis with SonarScanner showing issuues on the SonarQube dashboard. Understanding and configuring sonar-project.properties helps control which files are analyzed, how issues are categorized, and where the results appear on the dashboard.

<img width="834" height="784" alt="image" src="https://github.com/user-attachments/assets/34c4073c-606e-4bc3-a5ad-0c89f57b8b6f" />

<img width="380" height="281" alt="image" src="https://github.com/user-attachments/assets/2732aa52-68a7-4a34-8890-fdebb70eaebe" />

## 4. Rememdiation and Automation
Open .gitlab-ci.yml in your project directory and add the following:

```
stages:
  - build
  - test
  - sast

# Optional build stage (if you have Docker build or tests)
build:
  stage: build
  script:
    - echo "Build stage placeholder"

# Optional test stage
test:
  stage: test
  script:
    - echo "Test stage placeholder"

# SAST scan stage
sast_scan:
  stage: sast
  image: sonarsource/sonar-scanner-cli:latest
  variables:
    SONAR_HOST_URL: "http://10.0.2.15:9000"
    SONAR_LOGIN: "$SONAR_TOKEN"  # store token as GitLab CI/CD variable
  script:
    - sonar-scanner -Dsonar.projectKey=myapp -Dsonar.sources=.
  allow_failure: false  # enforce failing pipeline on critical issues
  artifacts:
    reports:
      sast: gl-sast-report.json
```
This step adds a SAST stage to .gitlab-ci.yml.
```
allow_failure: false    # enforces the SonarQube policies.
```

<img width="997" height="305" alt="image" src="https://github.com/user-attachments/assets/ea7d11ad-8414-4bed-ad79-43694622d792" />

📚 Tool Tip: Artifacts (sast report) show up in GitLab’s Security Dashboard.
💡 Learning Bite: This is the “fail fast” approach — insecure code cannot reach production without being caught.

## 5. Monitoring, Alerting, & Hardening

- Enable GitLab Security Dashboard for your repo.

- Configure quality gates in SonarQube (e.g., fail if > 1 critical issue).

- (Advanced) Add Slack webhook for failed scans.

📚 Design Insight: “Fail fast, fail loud, fail usefully.”
