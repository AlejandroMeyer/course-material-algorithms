# Branch Workflow Documentation

## Branch Structure

- **main**: Student-facing branch with starter code (exercises/, tests/)
- **solutions**: Instructor branch with complete implementations (solutions/, tests_solutions/)

## Workflow for Adding New Exercises

### 1. Work on `main` branch first (starter code)

```bash
git checkout main

# Create new exercise files in exercises/
# Add TODO comments and function signatures
# Create corresponding tests in tests/

git add exercises/ tests/
git commit -m "Add new exercise: [exercise-name]"
git push origin main
```

### 2. Merge `main` into `solutions` and add solutions

```bash
git checkout solutions

# Pull latest changes from main
git merge main

# Now add the complete solution
# Create solution files in solutions/
# Create solution tests in tests_solutions/

git add solutions/ tests_solutions/
git commit -m "Add solution for: [exercise-name]"
git push origin solutions
```

## Key Points

✅ **main** is the base - always update exercises here first
✅ **solutions** extends main - merge main, then add solution files
✅ Only difference between branches: `solutions/` and `tests_solutions/` directories
✅ Never merge solutions back into main!

## Quick Commands

```bash
# Update main with new exercise
git checkout main
# ... make changes ...
git add . && git commit -m "New exercise"
git push

# Bring solutions in sync and add solution
git checkout solutions
git merge main
# ... add solution files ...
git add solutions/ tests_solutions/
git commit -m "Solution for [exercise]"
git push
```

## Handling Merge Conflicts

If conflicts occur during merge:
1. Check which files conflict: `git status`
2. Resolve conflicts manually
3. `git add <resolved-files>`
4. `git commit` to complete merge

Most conflicts should be minimal since main only has exercises/ and solutions only has solutions/.
