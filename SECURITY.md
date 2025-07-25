# 🔐 Security Policy

## Supported Versions

We maintain the latest main branch of this repository. Security updates are provided for the current stable release. Contributions that introduce new features must not introduce known security vulnerabilities.

| Version        | Supported |
|----------------|-----------|
| main / latest  | ✅ Yes     |
| legacy         | ❌ No      |

---

## 📢 Reporting a Vulnerability

If you discover a security vulnerability, please **do not open a public issue**.

Instead, report it privately to the maintainer:

- 🛡️ GitHub Security Advisory: [Submit Report](https://github.com/bylickilabs/SciPy-Data-Analyzer-Suite/securit/advisories)

Please include:
- A clear description of the issue
- Steps to reproduce (if applicable)
- A proposed fix or recommendation (if available)

---

## 🔒 Responsible Disclosure

We follow a coordinated disclosure process. If a vulnerability is confirmed:
- We will acknowledge your report within **48 hours**
- A fix will be issued within **14 days**, unless complexity requires more time
- You will be credited (if desired) in the security advisory

---

## ✅ Security Best Practices

This project adheres to the following principles:
- No use of insecure functions or legacy APIs
- Input validation and safe handling of external data (e.g., CSV files)
- Dependencies reviewed and updated regularly via GitHub Dependabot
- Use of Python virtual environments recommended

---

## 🧪 Recommended Security Tools

We suggest using:
- `bandit` – Python security linter
- `safety` – Check for known vulnerabilities in dependencies
- `pip-audit` – Python dependency vulnerability scanner

---

## 📄 License & Disclaimer

This software is provided **as-is** without any warranties. Users are responsible for running the software in secure environments and updating dependencies.

---

**© 2025 BYLICKILABS – Security matters. Always.**
