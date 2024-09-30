---
title: "Getting Started: The Basics of Jenkins Pipeline"
---
What is CI/CD? Continuous Integration & Continuous Delivery

# What is Continuous Integration?

**Continuous Integration** is a software development method where team members integrate their work at least once a day. In this method, every integration is checked by an automated build to detect errors. This concept was first introduced over two decades ago to avoid "integration hell," which happens when integration is put off till the end of a project.

In Continuous Integration after a code commit, the software is built and tested immediately. In a large project with many developers, commits are made many times during a day. With each commit code is built and tested. If the test is passed, build is tested for deployment. If the deployment is a success, the code is pushed to Production. This commit, build, test, and deploy is a continuous process, and hence the name continuous integration/deployment.

In this CI tutorial, you will learn:

- What is Continuous Integration?
- Development without CI vs. Development with CI
- Difference between Compilation and Continuous Integration
- What do you need to conduct CI process?
- How Continuous integration work?
- Features of CI
- Why Use CI?
- Best practices of using CI
- Disadvantages of CI
- Tools for CI process

# Development without CI vs. Development with CI

Here are key differences between development using CI or without CI.

| **Development without CI** | **Development with CI** |
| --- | --- |
| Lots of Bugs | Fewer bugs |

| Infrequent commits | Regular commits |
| --- | --- |
| Infrequent and slow releases | Regular working releases |
| Difficult integration | Easy and Effective Integration |
| Testing happens late | Continuous Integration testing happens early and often. |
| Issue raised are harder to fix | Find and fix problems faster and more efficiently. |
| Poor project visibility | Better project visibility |

Activities in Continuous Integration

While compilation only compiles a code, CI does the following activities

## DB integration

- Ensure DB and code in sync
- Automated creation of DB and test data.

## Code Inspection

- Ensures a healthy codebase
- Identifies problems early and applies best practices

## Automated Deployment

- Allows you to release product anytime
- Continually demo-able state and it is works on any machine

## Document generation

- Ensure documentation is current
- Removes burned from the developer
- Produces build reports and metrics

## Compilation

Compilation is the process the computer takes to convert a high-level programming language code into a machine language that the computer able to understand. It ensures a code compiler on every target platform.

## When do I build?

- At every check-in
- Every time a dependency changes

