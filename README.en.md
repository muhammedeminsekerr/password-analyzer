# Password Analyzer

A tool that measures how strong a password is.

## What Does It Do?

It does the opposite of Hash Cracker: instead of cracking passwords, it analyzes how resistant a password is. It checks length, character variety, and common weak patterns to assign a strength score.

## Features

- Length check
- Character variety (lowercase/uppercase, digits, special characters)
- Common weak password detection
- Strength level and improvement suggestions

## Usage

    python password_analyzer.py

## How It Works

It scores each criterion, sums them up, and classifies the password as weak/medium/strong. Long passwords with varied characters score high because brute-force cracking becomes exponentially harder.

## Author

Muhammed Emin Şeker — Computer Engineering Student
GitHub: https://github.com/muhammedeminsekerr
