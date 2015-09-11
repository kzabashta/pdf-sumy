#!/bin/bash
rm lint_report.txt
pylint summarizer > lint_report.txt
