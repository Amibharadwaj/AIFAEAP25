# Repository Synchronization Setup

## Overview

Your repository `AIFAEAP25` is now configured to automatically synchronize with the source repository:
- **Source Repository**: `neerajverma101/finance-coach-ai`
- **Target Repository**: `Amibharadwaj/AIFAEAP25`
- **Sync Frequency**: Daily at 2:00 AM UTC (7:30 AM IST)

---

## 📋 Workflows Configured

### 1. **Sync from Source** (`sync-from-source.yml`)
**Purpose**: Automatically pulls changes from the source repository and merges them into your main branch.

**Schedule**:
- Runs daily at 2:00 AM UTC
- Can also be triggered manually via GitHub Actions UI

**How it works**:
1. Checks out your repository
2. Adds the source repository as a remote
3. Fetches latest changes from source/main branch
4. Merges changes into your main branch
5. Pushes merged changes back to your repository

**Location**: `.github/workflows/sync-from-source.yml`

---

### 2. **Notify on Sync** (`notify-on-sync.yml`)
**Purpose**: Sends notifications whenever the sync workflow completes successfully.

**How it works**:
1. Triggers on every push to main branch
2. Detects if push was from Sync Bot (sync workflow)
3. Extracts commit details (hash, timestamp, message)
4. Creates GitHub notifications
5. Posts sync completion to repository issues (if available)

**Location**: `.github/workflows/notify-on-sync.yml`

---

## 🚀 How to Use

### Manual Sync Trigger
If you don't want to wait for the scheduled sync:

1. Go to your repository → **Actions** tab
2. Click on **"Sync from Source Repository"** workflow
3. Click **"Run workflow"** button
4. Select the branch (main) and click **"Run workflow"**

### Monitor Sync Status
1. Go to your repository → **Actions** tab
2. Check the workflow run status (green ✅ = success, red ❌ = failed)
3. Click on a run to see detailed logs

### View Sync History
1. Go to your repository → **Commits**
2. Look for commits from "Sync Bot"
3. Each sync is tracked as a separate commit

---

## 📊 Sync Workflow Details

### Source Repository
- **URL**: https://github.com/neerajverma101/finance-coach-ai
- **Branch Synced**: `main`
- **Strategy**: Merge (preserves history)

### Merge Strategy
- Uses `--no-edit` flag (automated commit message)
- Allows unrelated histories (`--allow-unrelated-histories`)
- Continues on error to prevent workflow failures

### Sync Bot Configuration
- **Name**: Sync Bot
- **Email**: noreply@github.com
- **Permissions**: Write access to repository contents

---

## 🔔 Notifications

### Where You'll Get Notifications

1. **GitHub Actions Log** (Visible in Actions tab)
   - Shows sync status and any errors
   - Detailed commit information

2. **Repository Issues** (If Issue #1 exists)
   - Comments posted on sync completion
   - Include commit hash and timestamp

3. **GitHub Desktop/CLI**
   - Will show new commits from Sync Bot

### Customize Notifications
To receive email/Slack/webhook notifications:

1. **Email Notifications**:
   - Go to GitHub Settings → Notifications
   - Enable workflow notifications
   - Set your notification preferences

2. **Slack Integration** (Optional):
   - Add a Slack webhook step to the workflow
   - Requires Slack webhook URL in repository secrets

3. **GitHub Discussions**:
   - Check repository discussions for sync status

---

## ⚙️ Configuration

### Change Sync Schedule

Edit `.github/workflows/sync-from-source.yml` and modify the cron schedule:

```yaml
on:
  schedule:
    - cron: '0 2 * * *'  # Current: Daily at 2 AM UTC
    # Alternatives:
    # - cron: '0 * * * *'  # Every hour
    # - cron: '0 0 * * 0'  # Weekly on Sunday
    # - cron: '0 2 * * 1-5' # Weekdays at 2 AM
```

**Cron Format**: `minute hour day month day-of-week`

### Change Sync Source

Edit `.github/workflows/sync-from-source.yml` and update the repository URL:

```yaml
- name: Add remote for source repo
  run: |
    git remote add source https://github.com/YOUR_USERNAME/YOUR_REPO.git || true
    git remote set-url source https://github.com/YOUR_USERNAME/YOUR_REPO.git
```

---

## 🛠️ Troubleshooting

### Sync Failed
1. Check the Actions tab for error logs
2. Common issues:
   - Network connectivity
   - Source repository is private (needs authentication token)
   - Merge conflicts (manual resolution needed)

### No Notifications Appearing
1. Ensure GitHub Actions is enabled in repository settings
2. Check your GitHub notification settings
3. Verify workflows are not disabled

### Merge Conflicts
If there are conflicts:
1. The workflow will fail
2. You'll need to manually resolve in a new branch
3. Create a pull request with resolved conflicts

---

## 📈 Monitoring

### Check Last Sync
```bash
git log --author="Sync Bot" -1 --oneline
```

### View Sync Activity
1. Repository → **Insights** → **Network**
2. Repository → **Actions** → **Sync from Source Repository**

---

## 🔐 Security

- Uses GitHub's default `GITHUB_TOKEN` for authentication
- Token has write access only to repository contents
- No sensitive credentials stored in workflow files
- Sync Bot cannot access other repositories or personal data

---

## 📞 Support & Next Steps

### First Sync
The workflow will automatically run at its scheduled time. You can manually trigger it now:
1. Go to Actions tab
2. Select "Sync from Source Repository"
3. Click "Run workflow"

### Future Customization
You can modify workflows anytime by editing the YAML files in `.github/workflows/`

### Additional Resources
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Cron Scheduling Help](https://crontab.guru/)
- [Git Merge Documentation](https://git-scm.com/docs/git-merge)
