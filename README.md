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
### Managing container
We started with docker. For installing required packages run   
```pip install docker```
### TDD
- According to TDD principle, a test section added that required functions will be defined there.   
- All tests are in `test` directory. There is an example of unit test for container creat/delete in `test/unit/platform`.    
- For running tests run    
```python -m test.unit.platform.container -v```    
`-m` is for declaring python modules and `-v` is for enabling verbose mode.
### Structure
- In accordance with clean architecture, functions related to infrastructure will be put in `src/infrastructure`. For now docker-sdk added to this section.
- Our main functions are in `src/core/application`. We have started our work with crudContainer.

## Contribution
Any type of contribution is appreciated.