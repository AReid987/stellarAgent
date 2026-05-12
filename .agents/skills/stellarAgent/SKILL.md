```markdown
# stellarAgent Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `stellarAgent` repository, a TypeScript project built with the Next.js framework. You'll learn about file naming, import/export styles, commit message habits, and how to write and locate tests. While no explicit workflows were detected, this guide provides best practices and suggested commands for common development tasks.

## Coding Conventions

### File Naming
- Use **camelCase** for file and folder names.
  - Example: `userProfile.ts`, `apiRoutes/index.ts`

### Import Style
- Use **relative imports** for internal modules.
  - Example:
    ```typescript
    import { fetchData } from '../utils/apiHelpers';
    ```

### Export Style
- Prefer **named exports** over default exports.
  - Example:
    ```typescript
    // Good
    export const getUser = () => { ... };

    // Avoid
    export default function getUser() { ... }
    ```

### Commit Messages
- Freeform style, sometimes with prefixes.
- Average commit message length: ~38 characters.
  - Example: `fix: update user profile fetch logic`

## Workflows

_No explicit workflows detected in the repository. Below are suggested workflows for common development tasks._

### Running the Development Server
**Trigger:** When starting local development
**Command:** `/dev-start`

1. Open your terminal.
2. Run:
    ```bash
    npm run dev
    ```
3. Visit `http://localhost:3000` in your browser.

### Creating a New Module
**Trigger:** When adding new features or utilities
**Command:** `/create-module`

1. Create a new file using camelCase, e.g., `featureLogic.ts`.
2. Use named exports for all functions or constants.
    ```typescript
    export const newFeature = () => { ... };
    ```
3. Import using relative paths where needed.

### Writing Tests
**Trigger:** When adding or updating code
**Command:** `/add-test`

1. Create a test file alongside the module, following the `*.test.*` pattern.
    - Example: `featureLogic.test.ts`
2. Write tests using your preferred testing framework (unspecified).
    ```typescript
    // Example with Jest-style syntax
    import { newFeature } from './featureLogic';

    test('newFeature works', () => {
      expect(newFeature()).toBeTruthy();
    });
    ```

## Testing Patterns

- **File Pattern:** Test files are named with the `*.test.*` convention, e.g., `apiHelpers.test.ts`.
- **Framework:** Not explicitly specified; use the project's existing setup or consult the team.
- **Placement:** Test files are typically located alongside the modules they test.

## Commands

| Command        | Purpose                              |
|----------------|--------------------------------------|
| /dev-start     | Start the local development server    |
| /create-module | Scaffold a new module with conventions|
| /add-test      | Create a test file for a module       |
```