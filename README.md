# Exercise 11 — Pure Functions vs Side Effects

## What you'll learn
- What makes a function "pure"
- What a "side effect" is
- Why pure functions are easier to test and reason about

## Your task

This exercise has two parts:

**Part A** — Read the broken/impure functions and rewrite them as pure functions.

**Part B** — Implement new pure functions from scratch.

## How to run the tests

```bash
pytest
```

## Key concepts

### Pure function
- Always returns the same output for the same input
- Does NOT modify anything outside itself (no global state, no mutation of arguments)
- Does NOT do I/O (no print, no file writing, no network calls)

### Side effect
- Modifying a list/dict that was passed in
- Changing a global variable
- Printing to screen
- Writing to a file

## Example of impure → pure

```python
# IMPURE — modifies the list that was passed in!
def add_item(lst, item):
    lst.append(item)

# PURE — returns a new list instead
def add_item(lst, item):
    return lst + [item]
```
