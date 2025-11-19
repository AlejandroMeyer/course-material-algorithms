# Getting Course Updates

This repository is regularly updated throughout the semester with new exercises and materials.

## One-Time Setup

Add the original repository as an "upstream" remote:

```bash
git remote add upstream https://github.com/digital-business-lectures/course-material-algorithms.git
```

Verify it was added successfully:

```bash
git remote -v
```

You should now see:
```
origin    https://github.com/[your-classroom-repo].git (fetch)
origin    https://github.com/[your-classroom-repo].git (push)
upstream  https://github.com/digital-business-lectures/course-material-algorithms.git (fetch)
upstream  https://github.com/digital-business-lectures/course-material-algorithms.git (push)
```

## Getting Updates

When new exercises or materials are available, follow these steps:

### 1. Make sure your changes are saved

```bash
# Check your current status
git status

# If you have unsaved changes, commit them:
git add .
git commit -m "My work before update"
```

### 2. Fetch the updates

```bash
# Fetch the latest changes from the original repo
git fetch upstream

# Merge the updates into your main branch
git pull upstream main
```

### 3. Push the updates to your Classroom repo

```bash
git push origin main
```

## Handling Conflicts

If you've edited files that were also changed in the update, merge conflicts may occur:

```bash
# Git will show you which files have conflicts
# Open the files and resolve the conflicts manually
# Look for markers like:
# <<<<<<< HEAD
# your code
# =======
# new code
# >>>>>>> upstream/main

# After resolving:
git add .
git commit -m "Merge upstream updates"
git push origin main
```

## Tip: Getting Only New Exercises

If you only want specific new files (e.g., new exercises):

```bash
# Get specific files from upstream
git fetch upstream
git checkout upstream/main -- exercises/new_exercise/
git commit -m "Add new exercise"
git push origin main
```

## Questions?

If you have problems with updates:
1. Make sure all your own changes are committed
2. Try `git pull upstream main --no-rebase`
3. Contact the instructor if conflicts cannot be resolved

## Notifications

To be notified about new updates:
1. Go to https://github.com/digital-business-lectures/course-material-algorithms
2. Click "Watch" → "Custom" → "Releases"
3. You'll receive an email when new updates are available
