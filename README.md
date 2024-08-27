# CreamTracker - System Summary

**Purpose:**  
CreamTracker is a personal system designed to help track the usage of hair creams. It records which cream was used last and allows the user to update this information when a new cream is used. The primary goal of the system is to assist users in remembering which cream they used most recently, making it easier to manage their hair care routine.

**Features:**
- Load and save cream usage data from a JSON file.
- Identify the last cream used.
- Update the usage status when a new cream is applied, ensuring only one cream is marked as "used" at a time.

**Intended Use:**  
This system is designed for personal use and is not intended to be deployed as a web service. It is a lightweight, standalone script that manages cream usage locally.

**Future Improvements:**  
Potential future enhancements could include adding a user interface, implementing reminders for when to switch creams, or tracking additional details like usage frequency.

## Data Flow Diagram (DFD)

```mermaid
graph TD
    A[User] -->|Load data| B[Load data from JSON]
    B --> C[Data loaded]
    A -->|Update usage| D[Update usage status]
    D --> E[Save data to JSON]
    E --> C
    A -->|Check last used| F[Get last used cream]
    F --> C
    C --> G[Display information to user]
