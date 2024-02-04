<h1 align="center">
  We Hide Infrastructure
</h1>

## Description

WHI is a framework for hiding different infrastuctures. The infrastructure can be various container engines, IaaS providers and even virtual networks that we need to manage our platforms.

WHI is reponsible for providing an abstract layer that translates requests to manage container/vm to the real container/vm provider. For this we should prepare different infrastructure workflows for WHI to use.

## Philosophy

You know why there is a programming technique called Dependecy Injection (DI) and aware of its great effect that enables you to replace dependencies without changing the class that uses them. Then why not we use DI in another level, to decouple infrastructure from our code.    
Here is where WHI enters, WHI provide an abstract layer that hide underneath with its interface.

## Getting started

- This project is just started. We start with designing interface first, then we focus on adding different infrastructures. We will update this section ASAP.
## Contribution
Any type of contribution is appreciated.