# GitHub Actions Workflows

This directory contains automated CI/CD workflows for faststrap-community.

## Workflows

### 1. Tests (`tests.yml`)

**Triggers:**
- Push to `main` or `develop` branches
- Pull requests to `main` or `develop`
- Manual workflow dispatch

**What it does:**
- Runs on Ubuntu, Windows, and macOS
- Tests Python 3.10, 3.11, and 3.12
- Checks code formatting with Black
- Lints code with Ruff
- Runs all tests with Pytest
- Type checks with Mypy
- Uploads coverage to Codecov

**Status Badge:**
```markdown
![Tests](https://github.com/Faststrap-org/faststrap-community/workflows/Tests/badge.svg)
```

### 2. Publish to PyPI (`publish.yml`)

**Triggers:**
- When a GitHub release is published
- Manual workflow dispatch (with TestPyPI option)

**What it does:**
- Builds the package
- Validates the build
- Publishes to PyPI automatically (on release)
- Can publish to TestPyPI for testing

**Setup Required:**
1. Enable trusted publishing on PyPI:
   - Go to https://pypi.org/manage/account/publishing/
   - Add publisher: `Faststrap-org/faststrap-community`
   - Workflow: `publish.yml`
   - Environment: leave blank

**Manual Publish:**
```bash
# Trigger workflow manually from GitHub Actions tab
# Check "Publish to TestPyPI" for testing
```

### 3. Deploy Documentation (`docs.yml`)

**Triggers:**
- Push to `main` branch (when docs/ changes)
- When a GitHub release is published
- Manual workflow dispatch

**What it does:**
- Deploys documentation to GitHub Pages
- Creates redirect from root to docs/
- Copies README, CHANGELOG, CONTRIBUTING
- Configures Jekyll theme

**Setup Required:**
1. Enable GitHub Pages:
   - Go to repository Settings → Pages
   - Source: GitHub Actions
   - Save

**Documentation URL:**
https://faststrap-org.github.io/faststrap-community/

## Setup Instructions

### 1. Enable GitHub Pages

1. Go to: https://github.com/Faststrap-org/faststrap-community/settings/pages
2. **Source:** GitHub Actions
3. Click "Save"

### 2. Configure PyPI Trusted Publishing

1. Go to: https://pypi.org/manage/account/publishing/
2. Click "Add a new publisher"
3. Fill in:
   - **PyPI Project Name:** `faststrap-community`
   - **Owner:** `Faststrap-org`
   - **Repository:** `faststrap-community`
   - **Workflow name:** `publish.yml`
   - **Environment name:** (leave blank)
4. Click "Add"

### 3. Add Secrets (Optional)

For Codecov (optional):
1. Go to: https://github.com/Faststrap-org/faststrap-community/settings/secrets/actions
2. Add `CODECOV_TOKEN` if you want coverage reports

## Usage

### Running Tests

Tests run automatically on every push and pull request. To run manually:

1. Go to: https://github.com/Faststrap-org/faststrap-community/actions
2. Select "Tests" workflow
3. Click "Run workflow"

### Publishing to PyPI

**Automatic (Recommended):**
1. Create a new release on GitHub
2. Workflow automatically publishes to PyPI

**Manual:**
1. Go to Actions → "Publish to PyPI"
2. Click "Run workflow"
3. Check "Publish to TestPyPI" for testing
4. Click "Run workflow"

### Deploying Documentation

Documentation deploys automatically when:
- You push changes to `docs/` on main branch
- You create a new release

**Manual:**
1. Go to Actions → "Deploy Documentation"
2. Click "Run workflow"

## Workflow Status

Check workflow status at:
https://github.com/Faststrap-org/faststrap-community/actions

## Troubleshooting

### Tests Failing

1. Check the workflow run logs
2. Run tests locally: `pytest tests/ -v`
3. Fix issues and push again

### PyPI Publish Failing

1. Verify trusted publishing is configured
2. Check version number is unique
3. Ensure `pyproject.toml` is valid

### Docs Not Deploying

1. Check GitHub Pages is enabled
2. Verify workflow completed successfully
3. Wait 2-3 minutes for deployment
4. Check: https://faststrap-org.github.io/faststrap-community/

## Best Practices

1. **Always create releases through GitHub UI**
   - This triggers automatic PyPI publishing
   - Creates proper changelog
   - Tags the release

2. **Test on TestPyPI first**
   - Run publish workflow manually
   - Check "Publish to TestPyPI"
   - Verify installation works

3. **Update docs with code changes**
   - Documentation deploys automatically
   - Keep docs in sync with code

4. **Monitor workflow runs**
   - Check Actions tab regularly
   - Fix failing workflows promptly

## Release Process

With these workflows, your release process is simple:

1. **Prepare Release:**
   ```bash
   # Update version in pyproject.toml
   # Update CHANGELOG.md
   # Commit changes
   git add pyproject.toml CHANGELOG.md
   git commit -m "Prepare v0.1.0 release"
   git push origin main
   ```

2. **Create Release:**
   - Go to: https://github.com/Faststrap-org/faststrap-community/releases/new
   - Tag: `v0.1.0`
   - Title: `v0.1.0 - Initial Release`
   - Description: Copy from CHANGELOG.md
   - Click "Publish release"

3. **Automatic Actions:**
   - ✅ Tests run
   - ✅ Package builds
   - ✅ Publishes to PyPI
   - ✅ Deploys documentation

4. **Verify:**
   - Check PyPI: https://pypi.org/project/faststrap-community/
   - Check docs: https://faststrap-org.github.io/faststrap-community/
   - Test install: `pip install faststrap-community`

That's it! Everything else is automated. 🚀
