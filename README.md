# Implementing-Automated-SAST-GitLab-SonarQube
Reference implementation for automated SAST in CI/CD. Includes an intentionally vulnerable Flask app, GitLab CI integration, and SonarQube scanning to enforce pipeline gates, produce actionable reports, and drive secure remediation in production-grade DevSecOps workflows.

## 1. Create a deliberately insecure sample application
This simulates a development scenario where security flaws might be overlooked. By introducing known vulnerabilities, we can create a safe environment to explore how automated static application security testing (SAST) can detect issues before they reach production.

<img width="502" height="298" alt="image" src="https://github.com/user-attachments/assets/6fe56706-00ea-4258-8977-4fe2164d6e60" />

📚 Learning Bite: “SAST helps find flaws before attackers do.”

## 2. Vulnerable App Pipeline
In this step, we demonstrate how insecure code can flow through CI/CD pipelines when security scans are not enforced. The vulnerable Flask app from Step 1 has been pushed to GitLab, and the minimal pipeline (build + test) executes successfully. While the pipeline passes and artifacts are technically “deployable,” the app contains unmitigated vulnerabilities such as SQL injection.

Key Details

Repository: GitLab project contains app.py and .gitlab-ci.yml

Pipeline: Minimal CI pipeline with build and test stages only

Outcome: All jobs complete successfully (green checkmarks), but no security analysis occurs

<img width="992" height="54" alt="image" src="https://github.com/user-attachments/assets/e1dccf9c-4f7b-4e15-b3c6-b71f2559f5c8" />
📚 Learning Bite: “This is how insecure code sneaks into prod.”
