# CI GitHub Actions Demo

This repository contains sample GitHub Actions workflows for learning Continuous Integration (CI).

## Workflows Implemented

1. **Basic CI Workflow**  
   - Trigger: On push to `main`.  
   - Steps: Checks out the code and runs Python unit tests using the `unittest` library.  
   - Demonstrates setting up Python and verifying code with automated tests.

2. **Scheduled Workflow**  
   - Trigger: Runs daily at midnight UTC (via cron).  
   - Steps: Checks out the code and prints `Scheduled build completed successfully!` in the logs.  
   - Demonstrates scheduled jobs in GitHub Actions.

3. **Matrix Build Workflow**  
   - Trigger: On push and pull requests to `main`.  
   - Strategy: Runs the test suite across multiple Python versions (`3.7`, `3.8`, `3.9`, `"3.10"`).  
   - Demonstrates running jobs in parallel with different environments.
   - 
### Bonus: Self-Hosted Runner

A self-hosted runner was set up on a Rocky Linux VM and linked to this repository.  
The `selfhosted.yml` workflow targets it with `runs-on: self-hosted` and runs the unit tests using the system’s already installed Python 3.9.
